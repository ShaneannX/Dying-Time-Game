import pygame
from Classes.Characters import Player, Hunter
from Classes.Door import Door
from Classes.Questions import Questions
from Classes.Time import Countdown
class BaseScreen:
    def __init__(self, background_colour = None):
        if background_colour is None:
            self.colour = (255,255,255)
        else:
            self.colour = background_colour
        self.screen =  pygame.display.set_mode((1000, 600))
        self.font = pygame.font.Font('font/Pixeltype.ttf',50)
        pygame.display.set_caption("Dying Time")

    def change_bg_colour(self,colour):
        self.colour = colour
        self.screen.fill(self.colour)

class Menu(BaseScreen):
    def __init__(self,colour):
        super().__init__()
        self.colour = colour
        self.play_button_surface = pygame.image.load('graphics\start_menu\play_button.png')
        self.start_button_rect = self.play_button_surface.get_rect(topleft = (450,200))
        self.title_text = self.font.render("Dying Time", True, (0, 0, 0))

    def draw(self, surface):
        surface.fill(self.colour)
        surface.blit(self.title_text, (425, 150))
        surface.blit(self.play_button_surface, self.start_button_rect)

    def update(self):
        pass

    def handle_event(self, event, manager):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                manager.reset_game()
                manager.switch_screen("start")


class StartGame(BaseScreen):
    def __init__(self, player, doors, colour, manager):
        super().__init__()
        self.player = player
        self.doors = doors
        self.colour = colour
        self.manager = manager
        self.safezone = self.doors[2]
    # Handles movement logic for player
    def handle_event(self, event, manager):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.player.advance()
            if event.key == pygame.K_SPACE:
                self.player.reset()

    def update(self):
        # Checks each door if the player collides with it. Stops players movement if True. Let's player move if D key is pressed if False.
        for door in self.doors:
            print(door.is_locked)
            print(self.player.stop_player)
            if door.stops_player(self.player.player_collision_rect):
                self.player.stop()
            elif not door.is_locked and door.stops_player(self.player.player_collision_rect):
                self.player.unlock_door()

            if door.is_locked and door.stops_player(self.player.player_collision_rect):
                self.player.unlocked_door()
                print("swtich screen!!!!!")
                print(door.target_screen)
                self.manager.switch_screen("unlock_door")

        if self.safezone.check_collision(self.player.player_collision_rect):
            print("Winner!")
            self.manager.switch_screen("escaped")

    # Draws player and doors onto screen. 
    def draw(self, surface):
        surface.fill(self.colour)
        for door in self.doors:
            door.draw(surface)
        self.player.draw(surface)
        # self.countdown.draw(surface)
                        

class UnlockDoor(BaseScreen):
    def __init__(self, hunter,player, doors, manager, question_number = 1):
        super().__init__()
        self.player= player
        self.hunter = hunter
        self.doors = doors
        self.questions = Questions()
        self.user_input = ''
        self.input_rect = pygame.Rect(350,150,140,32)
        self.colour_active = pygame.Color('grey')
        self.colour_passive = pygame.Color('chartreuse4')
        self.textbox_colour = self.colour_passive
        self.active = False
        self.base_font = pygame.font.Font(None, 32)
        self.question_number = question_number
        self.question_text = self.base_font.render(self.questions.get_question(question_number), True, (255, 255, 255))
        self.answer = self.user_input
        self.manager = manager
        self.first_initalised = True

    def update(self):
        if len(self.answer) > 0:
            if self.questions.check_answer(self.question_number, self.answer):
                # Unlock door to 'start' screen
                for door in self.doors:
                    door.unlock()
                self.answer = ''
                self.first_initalised = True
                self.manager.switch_screen("start")
            else:
                self.hunter.advance_to_player()
                self.answer = ''

        if self.hunter.captured_player(self.player.player_collision_rect):
            self.manager.switch_screen("game_over")
    

    def handle_event(self, event, manager):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.input_rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.answer = self.user_input.strip()
                self.user_input = ''
            else:
                self.user_input += event.unicode

        self.textbox_colour = self.colour_active if self.active else self.colour_passive

    def draw(self, surface):
        if self.first_initalised:
            self.hunter.start_position(self.player.position)
            self.first_initalised = False
        surface.fill((255,0,0))
        for door in self.doors:
            door.draw(surface)
        self.player.draw(surface)
        self.hunter.draw(surface)
        surface.blit(self.question_text, (250, 100))
        pygame.draw.rect(surface, self.textbox_colour, self.input_rect)
        text_surface = self.base_font.render(self.user_input, True, (255, 255, 255))
        surface.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width() + 10)

class GameOver(BaseScreen):
    def __init__(self, manager, colour=None, restart_text = None, title_text=None):
        super().__init__()

        if title_text is None:
            self.title_text = self.font.render("GAME OVER!", True, (255, 255, 255))
        else:
            self.title_text = title_text
        if restart_text is None: 
            self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        else:
            self.restart_text = restart_text
        self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        self.manager = manager

        if colour is None:
            self.colour = (255,0,0)
        else:
            self.colour = colour
        
        self.manager = manager
    def update(self):
        pass

    def draw(self,surface):
        surface.fill((255,0,0))
        surface.blit(self.title_text, (425, 150))
        surface.blit(self.restart_text, (50, 400))

    def handle_event(self, event, manager):
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                manager.reset_game()
                manager.switch_screen('start')
            elif event.key == pygame.K_SPACE:
                manager.switch_screen('menu')


class Escaped(GameOver):
    def __init__(self, colour, manager):
        super().__init__(manager, colour=None, title_text=None, restart_text=None)
        self.title_text = self.font.render("WINNER!", True, (255, 255, 255))
        self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        self.colour = colour

    def draw(self, surface):
        surface.fill(self.colour)
        surface.blit(self.title_text, (425, 150))
        surface.blit(self.restart_text, (50, 400))
    