import pygame
from Classes.Characters import Player, Hunter
from Classes.Door import Door
from Classes.Questions import TriviaQuestions
from Classes.Time import Countdown
from abc import ABC, abstractmethod
import random
# Parent class for screen customisation

class BaseScreen(ABC):
    def __init__(self):
        self.font = pygame.font.Font('font/Pixeltype.ttf',50)
        pygame.display.set_caption("Dying Time")

    @abstractmethod
    def draw(self,surface : object):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def handle_event(self, event : object, manager :object):
        pass

# Inherits BaseScreen for attribute
class Menu(BaseScreen):
    def __init__(self,colour : tuple):
        super().__init__()
        # For background colour
        self.colour = colour
        # Play button surface and rect to place on screen.
        self.play_button_surface = pygame.image.load('graphics\start_menu\play_button.png')
        self.start_button_rect = self.play_button_surface.get_rect(topleft = (450,200))
        # Game title to display on screen
        self.title_text = self.font.render("Dying Time", True, (0, 0, 0))
    # Displays on screen method.
    def draw(self, surface : object):
        surface.fill(self.colour)
        surface.blit(self.title_text, (425, 150))
        surface.blit(self.play_button_surface, self.start_button_rect)

    def update(self):
        pass
    # To handle event for when the player presses the Start button
    def handle_event(self, event : object, manager : object):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                # Calls game manager method to reset the game
                manager.reset_game()
                # Calls game manager method to switch screen to start game
                manager.switch_screen("start")

# Inherits BaseScreen for attributes
class StartGame(BaseScreen):
    def __init__(self, player : object, doors : object, colour : tuple, manager : object):
        super().__init__()
        # Sgets player and door, colour, safezone and game manager from arguments.
        self.player = player
        self.doors = doors
        self.colour = colour
        self.manager = manager
        self.safezone = self.doors[2]

    # Handles movement logic for player
    def handle_event(self, event : object, manager : object):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                # Only when 'd' key is pressed the player will move to the right
                self.player.move()

    # Update method for conditional checks and screen management. 
    def update(self):
        
        for door in self.doors:
            is_door_locked = door.get_door_state()
            # Checks each door if the player collision rect collides with the door with it.
            if door.stops_player(self.player.collision_rect):
                # Stop player from moving forward showing the door is locked.
                self.player.stop()

            # Condition to check if door is locked and player is colliding with the door.
            if is_door_locked and door.stops_player(self.player.collision_rect):
                # Call game manager method to switch screen for player to try and unlock the door.
                self.manager.switch_screen("unlock_door")
        # Condition to check if player reached safezone
        if self.safezone.check_collision(self.player.collision_rect):
            # Call game manager method to switch to winner screen. 
            self.manager.switch_screen("escaped")

    # Draws player and doors onto screen. 
    def draw(self, surface):
        surface.fill(self.colour)
        for door in self.doors:
            door.draw(surface)
        self.player.draw(surface)
                        
# Inherits from BaseScreen for attributes
class UnlockDoor(BaseScreen):
    def __init__(self, hunter : object ,player : object, doors : object, manager : object, countdown : object):
        super().__init__()
        # Retrieves initalised classes passed in from arguments. 
        self.player= player
        self.hunter = hunter
        self.doors = doors
        self.countdown = countdown
        self.questions = TriviaQuestions()
        self.question_number = random.randint(0, 4)
        # Sets user input, input box, question with customisations
        self.user_input = ''
        self.input_rect = pygame.Rect(350,150,140,32)
        self.colour_active = pygame.Color('grey')
        self.colour_passive = pygame.Color('chartreuse4')
        self.textbox_colour = self.colour_passive
        self.base_font = pygame.font.Font(None, 32)
        self.active = False
        self.question_text = self.base_font.render(self.questions.get_question(self.question_number), True, (255, 255, 255))
        # Sets answer to inital user input
        self.answer = self.user_input
        # initalise game manager from the argument.
        self.manager = manager
        # Condition for drawing the hunter at a specific position behind the player.
        self.first_initalised = True

    # Method to check whilst game is running.
    def update(self):
        self.question_text = self.base_font.render(self.questions.get_question(self.question_number), True, (255, 255, 255))
        # Only runs if answer is given
        if len(self.answer) > 0:
            # Method from questions class to check if answer is correct. 
            if self.questions.check_answer(self.question_number, self.answer):
                # Unlock door to 'start' screen
                for door in self.doors:
                    # Door method is called to unlock the door.
                    door.unlock()
                # Resets the answer back to inital state.
                self.answer = self.user_input
                # Sets state back to True for the next door or when game restarts.
                self.first_initalised = True
                # Invokes player method to allow player movement again.
                self.player.unlocked_door()
                # countdown class method is invoked to add 10 seconds to the timer.
                self.countdown.add_time(10)
                # Game manager method is invoked to switch back to the game screen.
                self.question_number = random.randint(0, 4)
                self.manager.switch_screen("start")
            else:
                # If answer is incorrect, the hunter will move closer to the player. 
                self.hunter.move()
                # Answer is returned to inital state. 
                self.answer = self.user_input
        # Checks if hunter has collided with the player
        if self.hunter.captured_player(self.player.collision_rect):
            # If true then manager method is invoked to change to game over screen.
            self.user_input = '' 
            self.question_number = random.randint(0, 4)
            self.manager.switch_screen("game_over")
    
    # Handles if certain events happens whilst the game is running. 
    def handle_event(self, event : object, manager : object):
        # Checks if players mouse clicked on the input text box.
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set self.active to True or False.
            self.active = self.input_rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # If backspace key is pressed, it will remove the character at the end of the user input
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                # If the enter key is pressed, it will save the users input to self.answer.
                self.answer = self.user_input.strip()
                # reinstates user input to an empty string
                self.user_input = ''
            else:
                # Else returns an empty space.
                self.user_input += event.unicode
        # Assigns textbox_colour to the respective colour if active is true or false.
        self.textbox_colour = self.colour_active if self.active else self.colour_passive
    # Method to draw the hunter to the screen.
    def draw(self, surface : object):
        # Condition so that hunter is drawn correctly.
        if self.first_initalised:
            # Invoke hunter method to get starting position
            self.hunter.start_position(self.player.position)
            # Set to False
            self.first_initalised = False
        # Draws the background colour
        surface.fill((255,0,0))
        # redraw previous screen surface from StartGame
        for door in self.doors:
            door.draw(surface)
        self.player.draw(surface)
        # displays the hunter at starting position.
        self.hunter.draw(surface)
        # Draws the question and textbox
        surface.blit(self.question_text, (250, 100))
        pygame.draw.rect(surface, self.textbox_colour, self.input_rect)
        text_surface = self.base_font.render(self.user_input, True, (255, 255, 255))
        surface.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width() + 10)

# Inherits from BaseScreen for attributes. Also Escaped will be a subclass of this.
class GameOver(BaseScreen):
    def __init__(self, manager : object, colour=None, restart_text = None, title_text=None):
        super().__init__()
        # Allows to override attributes of parent class. 
        # If None then assigns the defaults.
        if title_text is None:
            self.title_text = self.font.render("GAME OVER!", True, (255, 255, 255))
        else:
            self.title_text = title_text
        if restart_text is None: 
            self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        else:
            self.restart_text = restart_text
        self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        # gets the game manager from argument. 
        self.manager = manager
        # Colour should default to Red.
        if colour is None:
            self.colour = (255,0,0)
        else:
            self.colour = colour
        
        self.manager = manager
    def update(self):
        pass
    
    # Method to display onto screen.
    def draw(self,surface : object):
        # Draws the background to remove previous drawings - Don't want to show the countdown, player, doors or hunter when on this screen. 
        surface.fill((255,0,0))
        # Draws game over text and information how to restart/ return to main menu
        surface.blit(self.title_text, (425, 150))
        surface.blit(self.restart_text, (50, 400))

    # To handle events when game is running on this screen.
    def handle_event(self, event : object, manager: object):
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # If ENTER is pressed, the game will reset
                manager.reset_game()
                # manager method is invoked to switch to the game screen. 
                manager.switch_screen('start')
            elif event.key == pygame.K_SPACE:
                # Invokes the manager method to return to main menu. 
                manager.switch_screen('menu')

# Subclass that inherits GameOver for attributes and methods. 
class Escaped(GameOver):
    def __init__(self, colour : tuple, manager : object):
        super().__init__(manager, colour=None, title_text=None, restart_text=None)
        # Overrides the parents colour, title_text and restart_text.
        self.title_text = self.font.render("WINNER!", True, (255, 255, 255))
        self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        self.colour = colour
    # Displays on screen.
    def draw(self, surface):
        # Draws the background colour to remove previous drawings.
        surface.fill(self.colour)
        # Displays the winners infromation. 
        surface.blit(self.title_text, (425, 150))
        surface.blit(self.restart_text, (50, 400))

    # Due to inheriting GameOver, it inherits the handle event which will be the same for this screen. 
    