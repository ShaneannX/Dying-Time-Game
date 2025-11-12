import pygame
from Classes.Screen import BaseScreen, StartGame, Menu, UnlockDoor, Escaped, GameOver
from Classes.Characters import Player, Hunter
from Classes.Door import Door, SafeZone
from Classes.Time import Countdown
import random
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 600))

        # Set up classes
        self.player = Player("Player 1", 20)
        self.hunter = Hunter("Unknown", 28)
        self.doors = [
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "start"),
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "unlock_door"),
            SafeZone((500,150), pygame.image.load("graphics\door\safezone.png").convert_alpha(), "start"),
        ]
        self.countdown = Countdown(self)
        # To randomise the questions
        self.question_number = random.randint(0, 2)
        self.screens = {
            'menu': Menu((128, 128, 128)),
            'start': StartGame(self.player, self.doors, (255,255,255), self),
            'game_over': GameOver(255,0,0),
            'escaped': Escaped((0,255,0), self),
            'unlock_door': UnlockDoor(self.hunter,self.player,self.doors,self, self.question_number)
        }

        self.current_screen = self.screens["menu"]

    def reset_game(self):
        print("Resetting game!")
        self.player.reset()
        self.hunter.reset()
        for door in self.doors:
            door.reset()
        self.countdown.reset()

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

            self.current_screen.update()
            self.current_screen.draw(self.screen)
            if not isinstance(self.current_screen, (Menu, GameOver, Escaped)):
                self.countdown.tick()
                self.countdown.draw(self.screen)
            pygame.display.flip()
            Clock.tick(60)

