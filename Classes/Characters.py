import pygame
from abc import ABC, abstractmethod

#Characters Interface as a pure contract

class CharacterInterface(ABC):
    @abstractmethod
    def draw(self, surface : object):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def reset(self):
        pass


class AbstractCharacters(CharacterInterface):
    def __init__(self, name=None, age=None):
        # Conditions if attributes needs to be overriden
        if name is None: 
            self.name = "Default"
        else:
            self.name = name
        if age is None:
            self.age = 20
        else:
            self.age = age
        # Movement logic
        self.Clock = pygame.time.Clock()
        self.delta_time = self.Clock.tick(60) / 1000
        # Customisation
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.DEFAULT_IMAGE_SIZE = (100,100)
        # Characters positions
        self.inital_position = (0,200)
        self.position = pygame.Rect(0,200,50,50)
        self.collision_rect = pygame.Rect(0,0,50,50)
        self.collision_rect.center = self.position.center
        self.stop_player = False

    # Methods to pass to subclasses
    def move(self):
        if self.stop_player == False:
            self.position.x += 1000 * self.delta_time
            self.collision_rect.center = self.position.center

    # Retrieves the players position.
    def get_player_position(self):
        """
        Returns players position
        """
        return self.position.x
    
    # Stops player from moving
    def stop(self):
        self.stop_player = True

    # Method to unlock door which allows the player to move again. 
    def unlocked_door(self):
        self.stop_player = False

    # Abstract methods that subclasses must have. 
    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def reset(self):
        pass




# Subclass of Characters.
class Player(AbstractCharacters):
    def __init__(self, name : str, age: int):
        super().__init__(name=None, age=None)
        # Overides parent attribue
        self.name = name
        self.age = age
        # set up player
        self.player = pygame.image.load('graphics\Player\player_static.png').convert_alpha()
        self.player = pygame.transform.scale(self.player, self.DEFAULT_IMAGE_SIZE)
        self.position = self.player.get_rect(topleft = self.inital_position)

    # Method to draw player onto the screen
    def draw(self, surface : object):
        surface.blit(self.player,self.position)
        self.collision_rect.center = self.position.center

     # Allows to set the players position.
    def set_position(self, position_x):
        self.position = self.player.get_rect(topleft = (position_x))

    # Resets the class to its inital states.
    def reset(self):
        self.position = self.player.get_rect(topleft=self.inital_position)
        self.collision_rect.center = self.position.center
        self.stop_player = False

# Subclass of Characters
class Hunter(AbstractCharacters):
    def __init__(self, name : str, age : int):
        super().__init__(name=None, age=None)
        # Overides parent attribue
        self.name = name
        self.age = age
        # Sets up hunter
        self.hunter = pygame.image.load('graphics\Hunter\hunter_static.png').convert_alpha()
        self.hunter = pygame.transform.scale(self.hunter, self.DEFAULT_IMAGE_SIZE)
        self.position = self.hunter.get_rect(topleft = (0, 200))

    # Displays hunter on the screen
    def draw(self, surface: object):
        surface.blit(self.hunter,self.position)
        self.collision_rect.center = self.position.center
    # Returns a boolean if hunter has captured player.
    def captured_player(self, player_pos):
        return self.collision_rect.colliderect(player_pos)
    # Sets up hunters position to be a certain distance from the player when initalised.
    def start_position(self, player_pos : object):
        self.position.x = player_pos.x - 150
    # Reset Hunter class to its inital states. 
    def reset(self):
        self.position.x = 0
        self.collision_rect.center = self.position.center

