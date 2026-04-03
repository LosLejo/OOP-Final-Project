import pygame
from pygame import *
from Assets import Sound

#   button class
class Buttons():
    def __init__(self, x, y, image, imageOn, elevation):
        self.image = image
        self.imageOn = imageOn
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.playH = False
        self.elevation = elevation
        
        
    def checkHover(self, surface):
        pos = pygame.mouse.get_pos()
        
        while self.rect.collidepoint(pos):
            return True
    

        return False
    
    def playHover(self, surface):
        count = 0
        
        #   get mouse pos
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos) and self.playH == False:
            self.playH = True
            count += 1
    
        if self.playH == True and count == 1:
            Sound.play_hover()
        
        if self.rect.collidepoint(pos) == False:
            self.playH = False
            count = 0

    def draw(self, surface):
        action = False
        
        #   get mouse pos
        pos = pygame.mouse.get_pos()
        
        #   check if mouse hover button
        if self.rect.collidepoint(pos):
            surface.blit(self.imageOn, (self.rect.x, self.rect.y - self.elevation))
            #   check for mouse click
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True 
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        
        #   makes button clickable again
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #   draw button on class
        
        return action