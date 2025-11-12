import pygame


class Countdown:
    """
    Takes 3 arguments
    screen - game screen
    timer event id
    font - for countdown text
    colour - for countdown text
    """
    def __init__(self,manager):
        self.colour = "green"
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.start_timer = pygame.time.get_ticks()
        self.duration = 60000
        self.manager = manager
        self.elapsed_time = pygame.time.get_ticks() - self.start_timer
        self.countdown = (self.duration - self.elapsed_time) / 1000
        self.inital_countdown = self.countdown
        self.countdown_text_colour = pygame.Color(self.colour)
        self.countdown_text = self.font.render(str(self.countdown), True, self.countdown_text_colour)
        self.text_rect = self.countdown_text.get_rect(topleft = (10, 50))
    
    def draw(self, surface):
        surface.blit(self.countdown_text, self.text_rect)

    def tick(self):
        self.elapsed_time = pygame.time.get_ticks() - self.start_timer
        self.countdown = (self.duration - self.elapsed_time) / 1000
        if self.elapsed_time < self.duration:
            print(self.elapsed_time)
            self.countdown = (self.duration - self.elapsed_time) / 1000
            self.countdown_text = self.font.render(str(self.countdown), True, self.countdown_text_colour)

        
    def add_time(self, time):
        self.countdown += time

    def game_over(self):
        if self.elapsed_time >= self.duration:
            return False
        else:
            return True

    def reset(self):
        self.start_timer = pygame.time.get_ticks()
        self.elapsed_time = pygame.time.get_ticks() - self.start_timer
        self.countdown = (self.duration - self.elapsed_time) / 1000


        