import pygame

pygame.init()


class health():

    def __init__(self):
        self.health = 3
        self.max_health = 3
        
    def getDmg(self):
        if self.health > 0:
            self.health -= 1
            
    def getHealth(self):
        if self.health < self.max_health:
            self.health += 1
            
    def update(self):
        pass
    
    def draw(self, surface):
        
        emptyh = pygame.image.load("Assets\\hearts\\empty heart.png").convert_alpha()
        halfh = pygame.image.load("Assets\\hearts\\half heart.png").convert_alpha()
        fullh = pygame.image.load("Assets\\hearts\\full heart.png").convert_alpha()
        hpbox = pygame.image.load("Assets\\hearts\\hp box.png").convert_alpha()
        
        x = 205
        for heart in range(self.max_health):
            if heart < self.health:
                surface.blit(fullh, (heart + x, 43))
            else: 
                surface.blit(emptyh, (heart + x, 43))
            x += 80
    
    def drawOp(self, surface):
        
        emptyh = pygame.image.load("Assets\\hearts\\empty heart.png").convert_alpha()
        halfh = pygame.image.load("Assets\\hearts\\half heart.png").convert_alpha()
        fullh = pygame.image.load("Assets\\hearts\\full heart.png").convert_alpha()
        hpbox = pygame.image.load("Assets\\hearts\\hp box.png").convert_alpha()
        
        xx = 975
        for heart in range(self.max_health):
            if heart < self.health:
                surface.blit(fullh, (xx - heart, 43))
            else:
                surface.blit(emptyh, (xx - heart, 43))
            xx -= 80
        