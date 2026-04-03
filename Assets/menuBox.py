import pygame, sys
from pygame import mixer
from Assets import buttonGame
from Assets import Sound
from Assets import rockPaperScissors

#   initialize pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()


#   set FPS
clock = pygame.time.Clock()
FPS = 60


def menu(title, surface, user):
    result = user
    runMenu = True
    bk = False
    trans = 0
    temp = 0
    
    title = pygame.display.set_caption("ARE YO SURE ABOUT THAT?")
    
    surf = pygame.Surface([1280, 720], pygame.SRCALPHA, 32)
    
    def draw_trans():
        pygame.draw.rect(surf, (255, 255, 255, 3), [0, 0, 1280, 720])
    
        #   load confirmation box
    confirm = pygame.image.load("Assets\\gametext\\confirmation box.png").convert_alpha()
    yes = pygame.image.load("Assets\\gametext\\yes.png").convert_alpha()
    yesh = pygame.image.load("Assets\\gametext\\yes hover.png").convert_alpha()
    no = pygame.image.load("Assets\\gametext\\naur.png").convert_alpha()
    noh = pygame.image.load("Assets\\gametext\\no hover.png").convert_alpha()
    
        #   create confirm buttons
    yes_btn = buttonGame.Buttons(445, 370, yes, yesh, 3)
    no_btn = buttonGame.Buttons(650, 370, no, noh, 3)
        
    while runMenu:
        clock.tick(FPS)
        trans += 1

        if trans < 30:
            surface.blit(surf, (0, 0))
            draw_trans()
        
        surface.blit(confirm, (349, 205))
        yes_btn.playHover(surface)
        if yes_btn.draw(surface):
            Sound.play_click()
            return result
            runMenu = False
            
        if no_btn.draw(surface):
            Sound.play_click()
            result = 0
            return result
            runMenu = False
        no_btn.playHover(surface)
        
        #   event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if bk == True:
                runMenu = False
                
        pygame.display.update()
        
        
    