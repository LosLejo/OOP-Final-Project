import pygame

class Slider():
    def __init__(self, pos : tuple, size: tuple, inival : float, min : int, max: int,):
        self.pos = pos
        self.size = size
        
        #   determine left, right, center and top of slider
        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)
        
        #   store min and max values
        self.min = min
        self.max = max
        
        #   percetange of slider
        self.inival = (self.slider_right_pos - self.slider_left_pos) * inival
        
        #   main rectangle
        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        
        #   button rectangle
        self.button_rect = pygame.Rect(self.slider_left_pos + self.inival - 5, self.slider_top_pos, 10, self.size[1])
        
        def render(self, surface):
            pygame.draw.rect(surface, "darkgray", self.container_rect)
            pygame.draw.rect(surface.surface, "blue", self.button_rect)
        
    
        pass