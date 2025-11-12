import pygame
class Characters:
    def __init__(self, name=None, age=None):
        if name is None: 
            self.name = "Default"
        else:
            self.name = name
        if age is not None:
            self.age = age
        self.__countdown = 100
        # Movement logic
        self.moving = False
        self.Clock = pygame.time.Clock()
        self.delta_time = self.Clock.tick(60) / 1000 
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.DEFAULT_IMAGE_SIZE = (100,100)
    def get_countdown(self):
        return self.__countdown
    
    def add_countdown(self,value):
        if value <= self.__countdown:
            self.__countdown += value

    def subtract_countdown(self, value):
        if value <= self.__countdown:
            self.__countdown -= value

class Player(Characters):
    def __init__(self, name, age):
        super().__init__(name=None, age=None)
        self.name = name
        self.age = age
        self.player = pygame.image.load('graphics\Player\player_static.png').convert_alpha()
        self.player = pygame.transform.scale(self.player, self.DEFAULT_IMAGE_SIZE)
        self.player_rect = self.player.get_rect(topleft = (0, 200))
        self.player_collision_rect = pygame.Rect(0, 0, 50, 50)
        self.player_collision_rect.center = self.player_rect.center
        self.stop_player = False
        self.player_position = self.get_player_position()
        
    def draw(self, surface):
        surface.blit(self.player,self.player_rect)
    
    def advance(self):
        if self.stop_player == False:
            self.player_rect.x += 200 * self.delta_time
            self.player_collision_rect.center = self.player_rect.center

    def stop(self):
        self.stop_player = True

    def get_player_position(self):
        """
        Returns players position
        """
        return self.player_rect
    
    def set_position(self, position_x):
        self.player_rect = self.player.get_rect(topleft = (position_x))

    def reset(self):
        self.rect = self.player.get_rect(topleft = (0, 200))
        self.player_rect.x = 0


class Hunter(Player):
    def __init__(self, name, age):
        super().__init__(name=None, age=None)
        self.name = name
        self.age = age
        self.hunter = pygame.image.load('graphics\Hunter\hunter_static.png').convert_alpha()
        self.hunter = pygame.transform.scale(self.hunter, self.DEFAULT_IMAGE_SIZE)
        self.hunter_rect = self.hunter.get_rect(topleft = (0, 200))
        self.hunter_collision_rect = pygame.Rect(0, 0,50,50)
        self.hunter_collision_rect.center = self.hunter_rect.center

    def draw(self, surface):
        surface.blit(self.hunter,self.hunter_rect)
        self.hunter_collision_rect.center = self.hunter_rect.center
    
    def captured_player(self):
        return self.player_collision_rect.colliderect(self.hunter_collision_rect)

    def advance_to_player(self):
        self.hunter_rect.x += 2
    
    def pos_from_player(self):
        player_pos = self.get_player_position()
        self.hunter_rect.x = player_pos - 30

    def reset(self):
        self.hunter_rect = self.hunter.get_rect(topleft = (0, 200))
