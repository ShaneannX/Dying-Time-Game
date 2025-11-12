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
        return self.screen
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
                manager.switch_screen("start")


class StartGame(BaseScreen):
    def __init__(self, colour, manager):
        super().__init__()
        self.colour = colour
        self.manager = manager
        # Initialises Player. 
        self.player = Player("Jessica", 24)
        # Draws doors in each screeen. 
        self.doors = [
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "start"),
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "unlock_door")
            
        ]
        # self.countdown = Countdown(self.manager)

    # Handles movement logic for player
    def handle_event(self, event, manager):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.player.advance()

    def update(self):
        # Checks each door if the player collides with it. Stops players movement if True. Let's player move if D key is pressed if False.
        for door in self.doors:
            if door.stops_player(self.player.player_collision_rect):
                self.player.stop()
            elif not door.is_locked and not door.stops_player(self.player.player_collision_rect):
                self.handle_event()

            if door.is_locked and door.stops_player(self.player.player_collision_rect):
                print("swtich screen!!!!!")
                print(door.target_screen)
                # self.manager.switch_screen(door.target_screen)
            
            # self.time_ran_out(self.manager, self.countdown.check_time())

    # Draws player onto screen. 
    def draw(self, surface):
        surface.fill(self.colour)
        for door in self.doors:
            door.draw(surface)
        self.player.draw(surface)
        # self.countdown.draw(surface)
                        

class UnlockDoor(StartGame):
    def __init__(self, colour,manager, question_number = 1):
        super().__init__(manager=manager, colour=colour)
        self.hunter = Hunter("Unknown", 20)
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
    def update(self):
        pass
    

    def handle_event(self, event, manager):
        super().handle_event(event, manager)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.input_rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                answer = self.user_input.strip()
                if self.questions.check_answer(self.question_number, answer):
                    # Unlock door to 'start' screen
                    for door in self.doors:
                        if door.target_screen == 'start':
                            door.unlock()
                else:
                    self.hunter.advance_to_player()
                self.user_input = ''
            else:
                self.user_input += event.unicode

        self.textbox_colour = self.colour_active if self.active else self.colour_passive

    def draw(self, surface):
        # super().draw(surface)
        surface.blit(self.question_text, (250, 100))
        self.hunter.draw(surface)
        pygame.draw.rect(surface, self.textbox_colour, self.input_rect)
        text_surface = self.base_font.render(self.user_input, True, (255, 255, 255))
        surface.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width() + 10)

class GameOver(BaseScreen):
    def __init__(self, manager, colour, time_id=None, title_text=None, restart_text=None, player = None, hunter = None, door=None, countdown = None):
        super().__init__()

        if title_text is None:
            self.title_text = self.font.render("GAME OVER!", True, (255, 255, 255))
        else:
            self.title_text = title_text
        if restart_text is None: 
            self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        else:
            self.restart_text = restart_text
        if player is None:
            self.player = Player("Jessica", 24)
        else:
            self.player = player
        if door is None:
            self.door = Door((300,270), pygame.image.load("graphics\door\door.png").convert_alpha(), "start")
        else:
            self.door = door
        if hunter is None:
            self.hunter = Hunter("Unknown", 20)
        else:
            self.hunter = hunter
        if time_id is None:
            self.TIMER_EVENT_ID = pygame.USEREVENT + 1
        else:
            time_id = time_id
        if countdown is None:
            self.countdown = Countdown(manager)
        else:
            self.countdown = countdown

        self.manager = manager

        self.colour = colour
    def update(self):
        pass

    def draw(self,surface):
        surface.fill(self.colour)
        surface.blit(self.title_text, (425, 150))
        surface.blit(self.restart_text, (50, 400))

    def handle_event(self, event, manager):
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.player.reset()
                self.hunter.reset()
                self.door.reset()
                manager.switch_screen('start')
            elif event.key == pygame.K_SPACE:
                self.player.reset()
                self.hunter.reset()
                self.door.reset()
                manager.switch_screen('menu')


class Escaped(GameOver):
    def __init__(self, colour, manager):
        super().__init__(colour, manager, title_text=None, restart_text=None)
        self.title_text = self.font.render("WINNER!", True, (255, 255, 255))
        self.restart_text = self.font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
        self.change_bg_colour(colour)
    def draw(self, surface):
        super().draw(surface)
# import pygame

# class Menu():
#     def __init__(self,colour):
#         super().__init__()
#         self.colour = colour
#         self.play_button_surface = pygame.image.load('graphics\start_menu\play_button.png')
#         self.start_button_rect = self.play_button_surface.get_rect(topleft = (450,200))
#         self.title_text = self.font.render(self.game_caption, True, (255, 255, 255))

#     def draw(self, surface):
#         surface.fill(self.colour)
#         surface.blit(self.title_text, (425, 150))
#         surface.blit(self.play_button_surface, self.start_button_rect)

#     def update(self):
#         pass

#     def handle_event(self, event, manager):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if self.start_button_rect.collidepoint(event.pos):
#                 manager.switch_screen("start")

# class StartGame():
#     def __init__(self):
#         pass

    