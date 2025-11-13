import pygame
from abc import ABC, abstractmethod

class DoorInterface(ABC):
    @abstractmethod
    def lock(self):
        pass

    @abstractmethod
    def unlock(self):
        pass

    @abstractmethod
    def draw(self, surface : object):
        pass

    @abstractmethod
    def get_door_state(self):
        pass

    @abstractmethod
    def reset(self): 
        pass
class AbstractDoor(ABC):
    def __init__(self, is_locked=True):
        self.is_locked = is_locked

    def lock(self):
        self.is_locked = True
    
    def unlock(self):
        self.is_locked = False

    def get_door_state(self):
        return self.is_locked
    
    def reset(self):
        self.is_locked = True

    @abstractmethod
    def draw(self, surface):
        pass
        
class Door(AbstractDoor):
    def __init__(self, position : tuple, image : str, target_screen : str, is_locked = True):
        """
        Creates Door object
        position -  Where to place the object
        image - Door object image/sprite
        target_screen - Screen where to draw the object
        is_locked - If door is locked or not
        """
        self.door = image
        self.door = pygame.transform.scale(self.door, (300,270))
        self.door_rect = self.door.get_rect(topleft=(position))
        self.collision_rect = pygame.Rect(0, 0, 20, 90)
        self.collision_rect.center = self.door_rect.center
        self.target_screen = target_screen

    # Method that returns a boolean to check if door is locked and player is trying to walk through it. 
    def stops_player(self, player_position : object):
        return self.is_locked and self.collision_rect.colliderect(player_position)
    
    # Method to return a boolean if there is a collision with the player and the door
    def check_collision(self, player_position):
        return self.collision_rect.colliderect(player_position)
    # Draws the door on the screen
    def draw(self, surface : object):
        surface.blit(self.door, self.door_rect)

# Subclass of door, inheriting the parent class but overriding the is_lock attribute o False
class SafeZone(Door):
    def __init__(self, position : tuple, image : str, target_screen : str, is_locked=False):
        super().__init__(position, image, target_screen, is_locked=is_locked)


            
    
