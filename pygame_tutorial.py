import pygame
from sys import exit

pygame.init() # Initialize Pygame

# Set up display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Let's go")

Clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/Ground.png')
text_surface = test_font.render('My game', False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png')

snail_movement = 750
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements here
    # update everything

    screen.blit(sky_surface,(0,0)) # Block image transfer
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_movement -= 4
    if snail_movement < -100: snail_movement = 800
    screen.blit(snail_surface,(snail_movement,275))

    pygame.display.update()  # Update the display
    Clock.tick(60) # Max frameRate