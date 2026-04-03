import pygame
from Assets import buttonGame
from Assets import Sound
import sys


def bk_btn(surface):
    
    #   load images
    back = pygame.image.load("Assets\\buttons\\back button.png").convert_alpha()
    #   load hover images
    backhover = pygame.image.load("Assets\\buttons\\back hover.png").convert_alpha()
   
    back_btn = buttonGame.Buttons(1190, 620, back, backhover, 6)
    
    if back_btn.draw(surface):
        return True
    
    return False
    
    
    
    

