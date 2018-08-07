import pygame
pygame.init()

screen = pygame.display.set_mode([800, 500])
pygame.display.set_caption('Super Skills Art Soundboard')

top_left_sound = pygame.mixer.Sound("whirl.ogg")
bottom_left_sound = pygame.mixer.Sound("blip.ogg")
top_right_sound = pygame.mixer.Sound("charm.ogg")
bottom_right_sound = pygame.mixer.Sound("sleep.ogg")

background_position = [0, 0]
background_image = pygame.image.load("art.jpg").convert()

soundboard_end = False                                      

while not soundboard_end:                                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            soundboard_end = True                           
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_position = pygame.mouse.get_pos()
            x = player_position[0]                          
            y = player_position[1]                          
            if x < 400:     # left side
                if y < 250:     # top
                    top_left_sound.play()                   
                    print ('Top Left Click', x , y)
                else:           # bottom
                    bottom_left_sound.play()                
                    print ('Bottom Left Click', x , y)
            else:           # right side
                if y < 250:     # top
                    top_right_sound.play()                  
                    print ('Top Right Click', x , y)
                else:           # bottom
                    bottom_right_sound.play()               
                    print ('Bottom Right Click', x , y)

    screen.blit(background_image, background_position)
    pygame.display.flip()

pygame.quit()
