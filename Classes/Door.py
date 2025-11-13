import pygame
class Door:
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
        self.is_locked = is_locked

    # Method that returns a boolean to check if door is locked and player is trying to walk through it. 
    def stops_player(self, player_position):
        return self.is_locked and self.collision_rect.colliderect(player_position)
    
    # Method to return a boolean if there is a collision with the player and the door
    def check_collision(self, player_position):
        return self.collision_rect.colliderect(player_position)
    # Draws the door on the screen
    def draw(self, surface):
        surface.blit(self.door, self.door_rect)

    # Method to unlock the door
    def unlock(self):
        self.is_locked = False
    # Method to reset the door to its inital state.
    def reset(self):
        self.is_locked = True
        
# Subclass of door, inheriting the parent class but overriding the is_lock attribute o False
class SafeZone(Door):
    def __init__(self, position, image, target_screen, is_locked=False):
        super().__init__(position, image, target_screen, is_locked=is_locked)


            
    
