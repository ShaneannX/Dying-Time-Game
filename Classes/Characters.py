import pygame
class Characters:
    def __init__(self, name=None, age=None):
        if name is None: 
            self.name = "Default"
        else:
            self.name = name
        if age is not None:
            self.age = age
        # Movement logic
        self.Clock = pygame.time.Clock()
        self.delta_time = self.Clock.tick(60) / 1000 
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.DEFAULT_IMAGE_SIZE = (100,100)

        self.inital_position = (0,200)
        self.position = self.inital_position

# Player - Position, hitbox, draw player with hitbox, move player forward, stop player from moving, get players position
class Player(Characters):
    def __init__(self, name, age):
        super().__init__(name=None, age=None)
        self.name = name
        self.age = age
        self.player = pygame.image.load('graphics\Player\player_static.png').convert_alpha()
        self.player = pygame.transform.scale(self.player, self.DEFAULT_IMAGE_SIZE)
        self.position = self.player.get_rect(topleft = self.inital_position)
        self.player_collision_rect = pygame.Rect(0, 0, 50, 50)
        self.player_collision_rect.center = self.position.center
        self.stop_player = False
        
    def draw(self, surface):
        surface.blit(self.player,self.position)
    
    def advance(self):
        if self.stop_player == False:
            self.position.x += 1000 * self.delta_time
            self.player_collision_rect.center = self.position.center

    def stop(self):
        self.stop_player = True
    
    def unlocked_door(self):
        self.stop_player = False

    def get_player_position(self):
        """
        Returns players position
        """
        return self.position.x
    
    def set_position(self, position_x):
        self.position = self.player.get_rect(topleft = (position_x))

    def reset(self):
        self.position = self.player.get_rect(topleft=self.inital_position)
        self.player_collision_rect.center = self.position.center
        self.stop_player = False



class Hunter(Characters):
    def __init__(self, name, age):
        super().__init__(name=None, age=None)
        self.name = name
        self.age = age
        self.hunter = pygame.image.load('graphics\Hunter\hunter_static.png').convert_alpha()
        self.hunter = pygame.transform.scale(self.hunter, self.DEFAULT_IMAGE_SIZE)
        self.position = self.hunter.get_rect(topleft = (0, 200))
        self.hunter_collision_rect = pygame.Rect(0, 0,50,50)
        self.hunter_collision_rect.center = self.position.center

    def draw(self, surface):
        surface.blit(self.hunter,self.position)
        self.hunter_collision_rect.center = self.position.center
    
    def captured_player(self, player_pos):
        return self.hunter_collision_rect.colliderect(player_pos)
    
    def start_position(self, player_pos):
        self.position.x = player_pos.x - 150

    def advance_to_player(self):
        self.position.x += 300 * self.delta_time

    def reset(self):
        self.position.x = 0
        self.hunter_collision_rect.center = self.position.center

