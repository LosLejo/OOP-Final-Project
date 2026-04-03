from json import tool
import matplotlib
matplotlib.use('module://pygame_matplotlib.backend_pygame')
import numpy as np
import matplotlib.pyplot as plt
import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from Assets import backButton
from Assets import Sound

#   initialize pygame
pygame.init()

#   set FPS
clock = pygame.time.Clock()
FPS = 60

#   transition declaration (pygame.SRCALPHA)
trans = pygame.Surface((1280, 720), pygame.SRCALPHA)

#   transition function
def draw_trans():
    pygame.draw.rect(trans, (0, 0, 0, 40), [0, 0, 1280, 720])


def runGraph(title, surface):
    run = True
    bk = False
    active = False
    tooLarge = False
    input = False
    update = False
    drawvalue = False
    user_inp = ''
    shadow = pygame.Color("#b77d74")
    color = pygame.Color("#fdaa99")
    boxcolor = ""
    filter = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    count = 0
    maxx = 0
    val = 0
    val1 = 0
    
    #   load background image
    bg = pygame.image.load("Assets\\backgrounds\\cramers bg.png").convert_alpha()
    bg_width = bg.get_width()
    scroll = 0
    
    #   load boxes
    graphbg = pygame.image.load("Assets\\boxes\\bg graph.png").convert_alpha()
    box1 = pygame.image.load("Assets\\boxes\\box.png").convert_alpha()
    sliderbox = pygame.image.load("Assets\\boxes\\slider box.png").convert_alpha()
    shdw = pygame.image.load("Assets\\slider\\sshadow.png").convert_alpha()

    #   set amplitude and frequency of graph
    amp = 1.0
    freq = 1.0

    #   set graph surface \ figure
    fig, ax = plt.subplots(figsize = (6, 3), facecolor = "#fdaa99", linewidth = 10)
    plt.subplots_adjust(bottom = 0.15)

    #   x axis \ time
    t = np.linspace(0.0, 2 * np.pi, 1000)

    #   sin curve
    s = amp * np.sin(freq * t)

    #   line
    l, = ax.plot(t / 6, s, linewidth = 10, color = '#fdaa99')
    plt.xlabel("Time", fontweight = 'bold')
    ax.set_facecolor("#fdeacc")
    

    #   slider pygame
    slider = Slider(surface, 100, 650, 700, 40, min = 1, max = maxx, step = 0.1, colour = (253, 170, 153), handleColour = (253, 234, 204), handleRadius = int((40 / 1.3) - 9))
    
    text_box = pygame.Rect(900, 100, 50, 80)
    
    #   load font
    font2 = pygame.font.Font("Assets\\fonts\\upheavtt.ttf", 70)
    font3 = pygame.font.Font("Assets\\fonts\\upheavtt.ttf", 55)
    
    def drawt(text,  xx, yy):
        
        #   declares text
        img = font2.render(text, False, color)
        img2 = font2.render(text, False, shadow)        
        
        #   displays text
        surface.blit(img2, (xx + 2, yy + 2))
        surface.blit(img, (xx, yy))
    
    #   draw text function
    def drawtt(text,  xx, yy):
        
        #   declares text
        img = font3.render(text, False, color)
        img2 = font3.render(text, False, shadow)        
        
        #   displays text
        surface.blit(img2, (xx + 2, yy + 2))
        surface.blit(img, (xx, yy))
    
    while run:
        #   set fps
        clock.tick(FPS)
        
        #   set title
        title = pygame.display.set_caption("Discrete Time Signals: Graph")
        
        #   set transition to black
        surface.blit(trans, (0, 4))
        draw_trans()
        
        #   set momentarily delay
        if count <= 53:
            count += 1
        
        if count == 54:
            
            #   display scrolling bg
            for i in range(0, 4):
                surface.blit(bg, (i * bg_width + scroll, 0))
            
            #   set scroll speed
            scroll -= 1
            
            #   reset scroll
            if abs(scroll) > bg_width:
                scroll = 0
                       
            if input:
                slider.setValue(1)
                slider.max = maxx
                update = True
                input = False
        
            if update:
                drawvalue = True
                pygame_widgets.update(event)
            
            val1 = slider.getValue()
            val = int(val1)
            
            #   changes frequency value depending on slider
            freq = slider.getValue()
            l.set_ydata(amp * np.sin(freq * t))
            
            #   displays graph
            surface.blit(graphbg, (40, 5))
            fig.canvas.draw()
            surface.blit(fig, (160, 130))
            surface.blit(box1, (900, 450))
            
            if drawvalue:
                drawt(str(val), 935, 475)
                drawtt("# of waves : ", 900, 395)
                
            
            if tooLarge:
                drawtt("Too Large!", 900, 60)
            
            #   changes textbox color
            if active:
                boxcolor = color
                if user_inp == "type here!" or user_inp == "click me!":
                    user_inp = ''
            else:
                boxcolor = shadow
                user_inp = "type here!"
            
             #   display text box 
            pygame.draw.rect(surface, boxcolor, text_box, 6)
            
            #   updates user input
            im = font3.render(user_inp, False, color)
            im2 = font3.render(user_inp, False, shadow)
            
            #   display user input in textbox
            surface.blit(im2, (text_box.x + 22, text_box.y + 12))
            surface.blit(im, (text_box.x + 20, text_box.y + 10))
            
            #   adjusts textbox length based on input
            text_box.w = max(100, im2.get_width() + 30)
            
            #   display back button
            if backButton.bk_btn(surface):
                Sound.play_click()
                bk = True
                return backButton.bk_btn(surface)
            
        #   event handler
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
                
            if bk == True:
                run = False
                bk = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            
            #   check if a key is pressed
            if event.type ==  pygame.KEYDOWN:
                if active:
                    #   checks if backspace is pressed
                    if event.key == pygame.K_BACKSPACE:
                        user_inp = user_inp[:-1]
                        tooLarge = False
                        
                    else:
                        #   check if key pressed is number
                        if event.unicode in filter:
                        #   add key pressed in string input
                            user_inp += event.unicode
                            tooLarge = False
                    
                    if event.key == pygame.K_RETURN:
                        if int(user_inp) <= 10:
                            maxx = int(user_inp)
                            user_inp = ''
                            input = True
                            update = False
                        else:
                            tooLarge = True
                                

            
        pygame.display.update()
        

