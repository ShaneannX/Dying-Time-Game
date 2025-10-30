import pygame
from sys import exit
pygame.init() # Initialize Pygame

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dying Time")
Clock = pygame.time.Clock()

door_click = False


closed_door = pygame.image.load('graphics/door/closed_door.png')
opened_door = pygame.image.load('graphics/door/opened_door.png')
button_rect = closed_door.get_rect(topleft = (300, 250))
button_close_rect = opened_door.get_rect(topleft = (300,250))
door_open = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print(f"open door")
                door_open = True
         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_CAPSLOCK:
                door_open = False

    # draw all our elements here
    # update everything
    screen.fill('grey')
    print(door_open)
    if door_open:
        screen.blit(opened_door, (300,250))
    else:
        screen.blit(closed_door, button_rect) # Block image transfer

    pygame.display.update()  # Update the display
    Clock.tick(60) # Max frameRate