import pygame
from Classes.GameManager import GameManager
pygame.init() # Initialize Pygame

manager = GameManager()
manager.run()
# # Set up display
# screen = pygame.display.set_mode((1000, 600))
# pygame.display.set_caption("Dying Time")

# Clock = pygame.time.Clock()
# DEFAULT_IMAGE_SIZE = (100,100)
# ########### SURFACES ####################``
# test_font = pygame.font.Font('font/Pixeltype.ttf',50)
# play_button_surface = pygame.image.load('graphics\start_menu\play_button.png')
# player_static = pygame.image.load('graphics\Player\player_static.png').convert_alpha()
# player_dynamic = pygame.image.load('graphics\Player\player_dynamic.png')
# hunter_static = pygame.image.load('graphics\Hunter\hunter_static.png')
# hunter_dynamic = pygame.image.load('graphics\Hunter\hunter_dynamic.png').convert_alpha()
# door = pygame.image.load('graphics\door\door.png')
# safezone = pygame.image.load('graphics\door\safezone.png')

# ####### SCALE SURFACES #######################
# player_static = pygame.transform.scale(player_static, DEFAULT_IMAGE_SIZE)
# door = pygame.transform.scale(door, (300,270))
# door_two = pygame.transform.scale(door, (300,270))
# hunter_static = pygame.transform.scale(hunter_static, DEFAULT_IMAGE_SIZE)
# safezone = pygame.transform.scale(safezone, (300,270))

# ############### RECTS ########################
# player_rect = player_static.get_rect(topleft = (0, 200))
# hunter_rect = hunter_static.get_rect(topleft = (0, 200))
# door_rect = door.get_rect(topleft = (40, 150))
# door_two_rect = door.get_rect(topleft = (150, 150))
# safezone_rect = safezone.get_rect(topleft = (825, 150))

# font = pygame.font.Font('font/Pixeltype.ttf', 50)

# ####### MOVING LOGICS ###############
# moving = False
# delta_time = 0.1
# x = 0
# h_x = 0


# ############# HITBOXES ####################
# door_collision_rect = pygame.Rect(0, 0, 20, 90)
# door_collision_rect.center = door_rect.center

# door_two_collision_rect = pygame.Rect(0, 0, 20, 90)
# door_two_collision_rect.center = door_two_rect.center

# player_collision_rect = pygame.Rect(x,0,50,50)
# player_collision_rect.center = player_rect.center

# hunter_collision_rect = pygame.Rect(h_x, 0,50,50)
# hunter_collision_rect.center = hunter_rect.center

# safezone_collision_rect = pygame.Rect(0, 0, 20, 90)
# safezone_collision_rect.center = safezone_rect.center

# start_button_rect = play_button_surface.get_rect(topleft = (450,200))
# door_opened = False

# ############ GAME STATE MANAGEMENT #################

# game_state = 'play'
# game_state_two = 'stop'
# game_over = False

# ############## Time management ################

# countdown = 60
# inital_countdown = countdown
# countdown_text_colour = pygame.Color('green')

# TIMER_EVENT_ID = pygame.USEREVENT + 1
# pygame.time.set_timer(TIMER_EVENT_ID, 1000)

# countdown_text = font.render(str(countdown), True, countdown_text_colour)

# def start_menu():
#     running = True

#     while running:
#         screen.fill("grey")
#         title_text = font.render("Dying Time", True, (255, 255, 255))
#         screen.blit(title_text, (425, 150))
#         screen.blit(play_button_surface, start_button_rect)
#         pygame.display.update()

#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if start_button_rect.collidepoint(event.pos):
#                         return True
                    

# def winner():
#     screen.fill('green')
#     title_text = font.render("WINNER!", True, (255, 255, 255))
#     restart_text = font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
#     screen.blit(title_text, (425, 150))
#     screen.blit(restart_text, (50, 400))
#     pygame.display.flip()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     return 'restart'
#                 elif event.key == pygame.K_SPACE:
#                     return 'menu'

# def open_door_mode():
#         running = True
#         ########### TEXT BOX ###############
#         user_input = ''
#         input_rect = pygame.Rect(450,100,140,32)
#         colour_active = pygame.Color('grey')
#         colour_passive = pygame.Color('chartreuse4')
#         colour = colour_passive
#         active = False
#         screen.fill('red')
#         screen.blit(player_static,player_rect)
#         screen.blit(hunter_static,hunter_rect)
#         screen.blit(door, door_rect)
#         base_font = pygame.font.Font(None, 32)
        
#         while running:
            

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()
                
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if input_rect.collidepoint(event.pos):
#                         active = True
#                     else:
#                         active = False
                
#                 if event.type == pygame.KEYDOWN:

#                     if event.key == pygame.K_BACKSPACE:
#                         user_input = user_input[:-1]

#                     elif event.key == pygame.K_RETURN:
#                         answer = user_input
#                         if answer == "hey":
#                             return answer
#                         else:
#                             hunter_rect.x += 50 * delta_time
#                             hunter_collision_rect.x += 50 * delta_time
#                     else:
#                         user_input += event.unicode
                
#             if hunter_collision_rect.colliderect(player_collision_rect):
#                 return 'game over'
#             if active:
#                 colour = colour_active
#             else:
#                 colour = colour_passive

#             pygame.draw.rect(screen, colour, input_rect)

#             text_surface = base_font.render(user_input, True, (255, 255, 255))

#             screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
#             input_rect.w = max(100, text_surface.get_width()+10)
#             pygame.display.flip()
#             Clock.tick(60)

# def end_game():
#     screen.fill('red')
#     title_text = font.render("GAME OVER!", True, (255, 255, 255))
#     restart_text = font.render("Press ENTER to play again or SPACE to return to main menu", True, (255, 255, 255))
#     screen.blit(title_text, (425, 150))
#     screen.blit(restart_text, (50, 400))
#     pygame.display.flip()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     return 'restart'
#                 elif event.key == pygame.K_SPACE:
#                     return 'menu'

# start_menu()
# def start_game():
#     run_game = True
#     while run_game:
#         print(game_state)
        
#         if game_state == 'unlock_door':
#             answer = open_door_mode()
#             if answer is not 'game over' and not game_over:
#                 game_state = 'play'
#                 game_state_two = 'continue'
#             if answer is 'game over':
#                 game_over = True
#                 game_state_two = 'continue'
#                 game_state = end_game()
        
#         elif game_state == 'win':
#             game_state = winner()

#         elif game_state == 'restart':
#             # Reset variables

#             player_rect = player_static.get_rect(topleft = (0, 200))
#             player_collision_rect = pygame.Rect(x,0,50,50)
#             player_collision_rect.center = player_rect.center
#             hunter_rect.x = 0
#             hunter_collision_rect = pygame.Rect(h_x, 0,50,50)
#             hunter_collision_rect.center = hunter_rect.center
#             door_collision_rect = door_collision_rect
#             game_state_two = 'stop'
#             game_state = 'play'

#         elif game_state == 'menu':
#             player_rect = player_static.get_rect(topleft = (0, 200))
#             player_collision_rect = pygame.Rect(x,0,50,50)
#             player_collision_rect.center = player_rect.center
#             hunter_rect.x = 0
#             hunter_collision_rect = pygame.Rect(h_x, 0,50,50)
#             hunter_collision_rect.center = hunter_rect.center
#             door_collision_rect = door_collision_rect
#             game_state_two = 'stop'
#             start_again = start_menu()
#             if start_again:
#                 game_state = 'play'
            
#         elif game_state == 'play': 
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()
#                 if event.type == TIMER_EVENT_ID:
#                     if countdown > 0:
#                         countdown -= 1
#                         countdown_text = font.render(str(countdown), True, countdown_text_colour)
#                         if countdown == 0:
#                             pygame.time.set_timer(TIMER_EVENT_ID, 0)
#                             game_state = end_game()
                
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_d:
#                         moving = True
#                 if event.type == pygame.KEYUP:
#                     if event.key == pygame.K_d:
#                         moving = False

#                 if player_collision_rect.colliderect(door_collision_rect) and game_state_two == 'stop' or player_collision_rect.colliderect(door_two_collision_rect) and game_state_two == 'stop':
#                     print("COLLIDEED")
#                     moving = False
#                     game_state = 'unlock_door'

#                 if player_collision_rect.colliderect(safezone_collision_rect):
#                     game_state = 'win'
#                 screen.fill('grey') 
#                 text_rect = countdown_text.get_rect(center = screen.get_rect().center)
#                 screen.blit(countdown_text, text_rect)
#                 screen.blit(player_static,player_rect)
#                 screen.blit(door, door_rect)
#                 # screen.blit(door_two, door_two_rect)
#                 screen.blit(safezone, safezone_rect)
#                 pygame.draw.rect(screen, (0, 255, 0), player_collision_rect) 
#                 if moving:
#                     player_rect.x += 50 * delta_time
#                     player_collision_rect.x += 50 * delta_time

            

#         pygame.display.flip() # Update the display
#         Clock.tick(60) # Max frameRate