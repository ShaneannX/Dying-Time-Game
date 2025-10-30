import pygame
from sys import exit

pygame.init() # Initialize Pygame

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dying Time")

Clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

closed_door_surface = pygame.image.load('graphics\door\closed_door.png')
opened_door_surface = pygame.image.load('graphics\door\opened_door.png')
play_button_surface = pygame.image.load('graphics\door\start_menu\play_button.png')
font = pygame.font.Font('font/Pixeltype.ttf', 50)
closed_door_rect = closed_door_surface.get_rect(topleft=(100,100))
start_button_rect = play_button_surface.get_rect(topleft = (350,200))
door_opened = False

def start_menu():
    running = True

    while running:
        screen.fill((30,30,30))
        title_text = font.render("Dying Time", True, (255, 255, 255))
        screen.blit(title_text, (325, 100))
        screen.blit(play_button_surface, start_button_rect)
        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(event.pos):
                        running = False  # Exit menu and start game


start_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if closed_door_rect.collidepoint(event.pos):
                door_opened = True

        if event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_CAPS:
                door_opened = False
    # draw all our elements here
    # update everything

    screen.fill('grey') # Block image transfer
    
    if door_opened:
        screen.blit(opened_door_surface, (215,100))
    else:
        screen.blit(closed_door_surface, (215,100))

    pygame.display.update()  # Update the display
    Clock.tick(60) # Max frameRate