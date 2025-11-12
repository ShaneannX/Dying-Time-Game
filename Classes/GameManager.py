import pygame
from Classes.Screen import BaseScreen, StartGame, Menu, GameOver, Escaped, UnlockDoor
from Classes.Time import Countdown
class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 600))
        self.screens = {
            'menu': Menu((128, 128, 128)),
            'start': StartGame((255,255,255), self),
            # 'game_over': GameOver(255,0,0),
            # 'escaped': Escaped((0,255,0), self),
            # 'unlock_door': UnlockDoor((255,255,255), self)
        }

        self.current_screen = self.screens["menu"]
        self.countdown = Countdown(self)
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

