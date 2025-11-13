import pygame


class Countdown:
    """
    manager - GameManager class
    """
    def __init__(self,manager : object):
        self.manager = manager

        # Gets countdown time information
        # gets inital timer for when game starts
        self.start_timer = pygame.time.get_ticks()
        # Time player gets in miliseconds
        self.duration = 10000
        # Time from game started
        self.elapsed_time = pygame.time.get_ticks() - self.start_timer
        # Countdown time in seconds.
        self.countdown = (self.duration - self.elapsed_time) / 1000
        # inital countdown
        self.inital_countdown = self.countdown
        # Customisations for the countdown text
        self.colour = "green"
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.countdown_text_colour = pygame.Color(self.colour)

        # For rendering the countdown text onto the screen
        self.countdown_text = self.font.render(str(self.countdown), True, self.countdown_text_colour)
        self.text_rect = self.countdown_text.get_rect(topleft = (10, 50))
    # Displays countdown on the screen
    def draw(self, surface):
        surface.blit(self.countdown_text, self.text_rect)

    # Method to start countdown so it updates the elapsed time to get countdown.
    def tick(self):
        self.elapsed_time = pygame.time.get_ticks() - self.start_timer
        self.countdown = (self.duration - self.elapsed_time) / 1000
        if self.elapsed_time < self.duration:
            self.countdown = (self.duration - self.elapsed_time) / 1000
            self.countdown_text = self.font.render(str(self.countdown), True, self.countdown_text_colour)

    # Method to add time to countdown when player unlocks the door
    def add_time(self, time : str):
        # Need to convert the time in miliseconds
        self.duration += time * 1000
    # Checks if time has ran out, True if it has, False if not.
    def game_over(self):
        if self.elapsed_time >= self.duration:
            return True
        else:
            return False
    # Resets the time to initial states.
    def reset(self):
        self.start_timer = pygame.time.get_ticks()
        self.elapsed_time = pygame.time.get_ticks() - self.start_timer
        self.duration = 10000
        self.countdown = (self.duration - self.elapsed_time) / 1000


        