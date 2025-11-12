import pygame
class Door:
    def __init__(self, position, image, target_screen, is_locked=True):
        self.door = image
        self.door = pygame.transform.scale(self.door, (300,270))
        self.door_rect = self.door.get_rect(topleft=(position))
        self.collision_rect = pygame.Rect(0, 0, 20, 90)
        self.collision_rect.center = self.door_rect.center
        self.target_screen = target_screen
        # self.collided = False
        self.is_locked = is_locked

    # Method that returns a boolean to check if door is locked and player is trying to walk through it. 
    def stops_player(self, player_position):
        return self.is_locked and self.collision_rect.colliderect(player_position)
    
    def check_collision(self, player_position):
        return self.collision_rect.colliderect(player_position)

    def draw(self, surface):
        surface.blit(self.door, self.door_rect)

    def unlock(self):
        self.is_locked = False

    def reset(self):
        self.is_locked = True
        self.collided = False
            
    
