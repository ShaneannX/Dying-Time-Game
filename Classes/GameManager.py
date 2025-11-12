import pygame
from Classes.Screen import BaseScreen, StartGame, Menu, UnlockDoor, Escaped, GameOver
from Classes.Characters import Player, Hunter
from Classes.Door import Door, SafeZone
from Classes.Time import Countdown
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 600))

        # Set up classes
        self.player = Player("Player 1", 20)
        self.hunter = Hunter("Unknow", 28, self.player.get_player_position())
        self.doors = [
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "start"),
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "unlock_door"),
            SafeZone((500,150), pygame.image.load("graphics\door\safezone.png").convert_alpha(), "start"),
        ]
        self.countdown = Countdown(self)

        self.screens = {
            'menu': Menu((128, 128, 128)),
            'start': StartGame(self.player, self.doors, (255,255,255), self),
            'game_over': GameOver(255,0,0),
            'escaped': Escaped((0,255,0), self),
            'unlock_door': UnlockDoor(self.hunter,self.player,self.doors,self, 1)
        }

        self.current_screen = self.screens["menu"]
        self.countdown = Countdown(self)

    def reset_game(self):
        print("Resetting game!")
        self.player.reset()
        self.hunter.reset()
        for door in self.doors:
            door.reset()

    def switch_screen(self, name):
        self.current_screen = self.screens[name]

    def run(self):
        Clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                self.current_screen.handle_event(event, self)
            # self.screen.fill(self.get_background())
            self.countdown.tick()
            self.countdown.draw(self.screen)
            self.current_screen.update()
            self.current_screen.draw(self.screen)
            pygame.display.flip()
            Clock.tick(60)

