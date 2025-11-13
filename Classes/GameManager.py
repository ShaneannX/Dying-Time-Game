import pygame
from Classes.Screen import BaseScreen, StartGame, Menu, UnlockDoor, Escaped, GameOver
from Classes.Characters import Player, Hunter
from Classes.Door import Door, SafeZone
from Classes.Time import Countdown
import random
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 600))

        # Initalises Classes
        self.player = Player("Player 1", 20)
        self.hunter = Hunter("Unknown", 28)
        self.doors = [
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "start"),
            Door((150,150), pygame.image.load("graphics\door\door.png").convert_alpha(), "unlock_door"),
            SafeZone((500,150), pygame.image.load("graphics\door\safezone.png").convert_alpha(), "start"),
        ]
        self.countdown = Countdown(self)
        # To randomise the questions

        # Set up relative screens by initalising the screen classes
        self.screens = {
            'menu': Menu((128, 128, 128)),
            'start': StartGame(self.player, self.doors, (255,255,255), self),
            'game_over': GameOver(255,0,0),
            'escaped': Escaped((0,255,0), self),
            'unlock_door': UnlockDoor(self.hunter,self.player,self.doors,self, self.countdown)
        }

        # Makes sure to start off with the Menu screen
        self.current_screen = self.screens["menu"]

    # Method to reset all classes to their inital states. 
    def reset_game(self):
        # Calls reset() methods for each class
        self.player.reset()
        self.hunter.reset()
        for door in self.doors:
            door.reset()
        self.countdown.reset()
    # Method to switch to screen
    def switch_screen(self, name):
        self.current_screen = self.screens[name]
    # Run method to run the game
    def run(self):
        # Gets Clock to cap the game at 60 frames per second
        Clock = pygame.time.Clock()
        # While game is running
        while True:
            for event in pygame.event.get():
                # If the close button on the screen is pressed, will exit the game. 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Calls the screen class handle method
                self.current_screen.handle_event(event, self)
            # Calls the update method from the screen class
            self.current_screen.update()
            # Calls the screen draw method
            self.current_screen.draw(self.screen)
            # Countdown will only show if screen is start or unlock_door
            if not isinstance(self.current_screen, (Menu, GameOver, Escaped)):
                # Starts countdown
                self.countdown.tick()
                if self.countdown.game_over():
                    self.switch_screen('game_over')
                # Calls countdown draw method to show the countdown on the screen. 
                self.countdown.draw(self.screen)
                
            # updates display
            pygame.display.flip()
            Clock.tick(60)

