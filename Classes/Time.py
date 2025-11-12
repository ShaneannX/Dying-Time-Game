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
        self.countdown = 5
        self.manager = manager
        self.inital_countdown = self.countdown
        self.countdown_text_colour = pygame.Color(self.colour)
        self.countdown_text = self.font.render(str(self.countdown), True, self.countdown_text_colour)
        self.text_rect = self.countdown_text.get_rect(topleft = (10, 50))
        self.TIMER_EVENT_ID = pygame.USEREVENT + 1
        self.set_timer = pygame.time.set_timer(self.TIMER_EVENT_ID, 1000)
    
    def draw(self, surface):
        surface.blit(self.countdown_text, self.text_rect)

    def tick(self):
        if self.countdown > 0:
                    self.countdown -= 1
                    self.countdown_text = self.font.render(str(self.countdown), True, self.countdown_text_colour)
                    if self.countdown == 0:
                        pygame.time.set_timer(self.TIMER_EVENT_ID, 0)
                        
                    return self.countdown_text
        
    def add_time(self, time):
        self.countdown += time

    def check_time(self):
        if self.countdown == 0:
            return False
        else:
            return True

    def reset(self):
        if self.countdown == 0:
            self.countdown = self.inital_countdown
            self.countdown_text = self.font.render(str(self.countdown), True, self.countdown_text_colour)
            pygame.time.set_timer(self.TIMER_EVENT_ID, 1000)


        