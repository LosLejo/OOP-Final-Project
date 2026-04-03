import pygame
import time
from pygame import *
from Assets import backButton
from Assets import buttonGame
from Assets import Sound
from Assets import cramerSolve

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
    
#   main function
def runCramers(title, surface):
    bk = False
    runC = True
    tooLarge = False
    input = False
    what = False
    full = False
    dis = False
    solved = False
    count = 0
    D = 0
    Dx = 0
    Dy = 0
    Dz = 0
    x = 0
    y = 0
    z = 0
    shadow = pygame.Color("#b77d74")
    color = pygame.Color("#fdaa99")
    boxcolor = ""
    user_inp = ''
    var = {}
    inp = 0
    c = -1
    filter = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']
    active = False
    list = []
    
    #   backspace
    back = pygame.image.load("Assets\\numButtons\\backspace.png").convert_alpha()
    backh = pygame.image.load("Assets\\numButtons\\backspace hover.png").convert_alpha()
    
    #   enter
    enter = pygame.image.load("Assets\\numButtons\\ent.png").convert_alpha()
    enterh = pygame.image.load("Assets\\numButtons\\ent hover.png").convert_alpha()
    
    #  load boxes
    box = pygame.image.load("Assets\\boxes\\boxlong.png").convert_alpha()
    
    #   load font
    font2 = pygame.font.Font("Assets\\fonts\\upheavtt.ttf", 70)
    font3 = pygame.font.Font("Assets\\fonts\\upheavtt.ttf", 55)
    font4 = pygame.font.Font("Assets\\fonts\\upheavtt.ttf", 40)
    
    #   load background image
    bg = pygame.image.load("Assets\\backgrounds\\cramers bg.png").convert_alpha()
    bg_width = bg.get_width()
    scroll = 0
    
    #   text function
    def drawt(text,  xx, yy):
        
        #   declares text
        img = font2.render(text, False, color)
        img2 = font2.render(text, False, shadow)        
        
        #   displays text
        surface.blit(img2, (xx + 2, yy + 2))
        surface.blit(img, (xx, yy))
    
    def drawtt(text,  xx, yy):
        
        #   declares text
        img = font3.render(text, False, color)
        img2 = font3.render(text, False, shadow)        
        
        #   displays text
        surface.blit(img2, (xx + 2, yy + 2))
        surface.blit(img, (xx, yy))
        
    def drawttt(text,  xx, yy):
        
        #   declares text
        img = font4.render(text, False, color)
        img2 = font4.render(text, False, shadow)        
        
        #   displays text
        surface.blit(img2, (xx + 2, yy + 2))
        surface.blit(img, (xx, yy))
    
    
    #   create buttons
    back_btn = buttonGame.Buttons(850, 170, back, backh, 6)
    enter_btn = buttonGame.Buttons(850, 310, enter, enterh, 6)
    text_box = pygame.Rect(850, 75, 50, 80)
          
    #   window loop (updates based on FPS)
    while runC:
        #   set fps
        clock.tick(FPS)
        
        #   set title
        title = pygame.display.set_caption("Matrices : Cramer's Rule (3x3)")
        
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
                
            #   display boxes
            #   row 1
            surface.blit(box, (20 + (205 * 0), 70))
            surface.blit(box, (20 + (205 * 1), 70))
            surface.blit(box, (20 + (205 * 2), 70))
            surface.blit(box, (20 + (205 * 3), 70))
            
            #   row 2
            surface.blit(box, (20 + (205 * 0), 190))
            surface.blit(box, (20 + (205 * 1), 190))
            surface.blit(box, (20 + (205 * 2), 190))
            surface.blit(box, (20 + (205 * 3), 190))
            
            #   row 3
            surface.blit(box, (20 + (205 * 0), 310))
            surface.blit(box, (20 + (205 * 1), 310))
            surface.blit(box, (20 + (205 * 2), 310))
            surface.blit(box, (20 + (205 * 3), 310))
            
            #   display enter button only when full
            if str(var.get(11)) != "None" and c == 11:
                if enter_btn.draw(surface):
                    Sound.play_click()
                    
                    #   solves the matrix
                    D, Dx, Dy, Dz, x, y, z = cramerSolve.solve(var.get(0), var.get(1), var.get(2), var.get(3), var.get(4), var.get(5), var.get(6), var.get(7), var.get(8), var.get(9), var.get(10), var.get(11))
                    #   resets the error messages and values
                    dis = False
                    solved = True
                    input = False
                    full = False
                    what = False
                    user_inp = ''
                    c = -1
                
            #   displays back button
            if back_btn.draw(surface) and solved == False:
                Sound.play_click()
                if str(var.get(0)) != "None":
                    c -= 1
                    list.pop()
                    var.popitem()
                    what = False
                    full = False
            
            #   displays answers when not clicked in text box
            if solved == True and (user_inp == "click me!" or len(user_inp) < 1 or user_inp == "type here!"):
                if D != -9999:
                    drawtt(f"D = {str(D)}", 50 + (225 * 3), 420)
                
                    drawtt(f"Dx = {str(Dx)}", 50 + (225 * 0), 420 + (45 * 0))
                    drawtt(f"Dy = {str(Dy)}", 50 + (225 * 0), 420 + (45 * 1))
                    drawtt(f"Dz = {str(Dz)}", 50 + (225 * 0), 420 + (45 * 2))
                
                    drawtt(f"x = {str(x)}", 50 + (250 * 0), 570 + (45 * 0))
                    drawtt(f"y = {str(y)}", 50 + (250 * 0), 570 + (45 * 1))
                    drawtt(f"z = {str(z)}", 50 + (250 * 0), 570 + (45 * 2))
                else:
                    drawtt("ERROR, DETERMINANT IS ZERO!", 50 + (225 * 0), 440)
            
            #   resets matrix
            if solved == True and len(user_inp) == 1:
                list.clear()
                var.clear()
                solved = False
                
            #   display what error
            if what:
                drawtt("What?", 850, 15)
            
            #   display full error
            if full:
                drawtt("Matrix Full!", 850, 15)
            
            # display too large error
            if tooLarge:
                drawtt("Too Large!", 850, 15)
            
            #   displays x y z = c at the top    
            drawtt("X    +   Y    +   Z    =    C", 100, 15)
            
            #   row 1 values
            if str(var.get(0)) != "None":
                drawtt(str(var.get(0)), 50 + (205 * 0), 85)     
            if str(var.get(1)) != "None":
                drawtt(str(var.get(1)), 50 + (205 * 1), 85)
            if str(var.get(2)) != "None":
                drawtt(str(var.get(2)), 50 + (205 * 2), 85)
            if str(var.get(3)) != "None":
                drawtt(str(var.get(3)), 50 + (205 * 3), 85)
            
            #   row 2 values
            if str(var.get(4)) != "None":
                drawtt(str(var.get(4)), 50 + (205 * 0), 210)
            if str(var.get(5)) != "None":
                drawtt(str(var.get(5)), 50 + (205 * 1), 210)
            if str(var.get(6)) != "None":
                drawtt(str(var.get(6)), 50 + (205 * 2), 210)
            if str(var.get(7)) != "None":
                drawtt(str(var.get(7)), 50 + (205 * 3), 210)
            
            
            #   row 3 values
            if str(var.get(8)) != "None":
                drawtt(str(var.get(8)), 50 + (205 * 0), 325)
            if str(var.get(9)) != "None":
                drawtt(str(var.get(9)), 50 + (205 * 1), 325)
            if str(var.get(10)) != "None":
                drawtt(str(var.get(10)), 50 + (205 * 2), 325)
            if str(var.get(11)) != "None":
                drawtt(str(var.get(11)), 50 + (205 * 3), 325)
            
        
            #   changes textbox color
            if active:
                boxcolor = color
                if user_inp == "type here!" or user_inp == "click me!":
                    user_inp = ''
                
            else:
                boxcolor = shadow
                if len(user_inp) == 0:
                    if dis == False and solved == True:
                        user_inp = "click me!"
                    else:
                        user_inp = "type here!"
                    drawtt(user_inp, text_box.x + 20, text_box.y + 5)
            
            #   display text box 
            pygame.draw.rect(surface, boxcolor, text_box, 6)
            
            #   updates user input
            im = font2.render(user_inp, False, color)
            im2 = font2.render(user_inp, False, shadow)
            
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if bk == True:
                runC = False
                bk = False
            
            #   check if user is clicked on the textbox
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
 
                    #   set text box to active
                    active = True
                    
                    #   see if matrix is full
                    if str(var.get(11)) != "None":
                        #   displays answers
                        dis = True
                else:
                    #   removes error display when unclicked
                    active = False
                    full = False
                    what = False
            
            #   check if a key is pressed
            if event.type ==  pygame.KEYDOWN:
                if active:
                    #   checks if backspace is pressed
                    if event.key == pygame.K_BACKSPACE:
                        #   removes last input and error messages
                        user_inp = user_inp[:-1]
                        tooLarge = False
                        what = False
                        full = False
                    else:
                        #   check if key pressed is number
                        if event.unicode in filter:
                            #   add key pressed in string input
                            user_inp += event.unicode
                            what = False
                            tooLarge = False
                            full = False
                            
                    #   check if enter is pressed
                    if event.key == pygame.K_RETURN:
                        #   checks if matrix is full
                        if c < 11: 
                            try:
                                inp = int(user_inp)
                                what = False
                                
                                #   checks if value is below 1000
                                if inp < 1000:
                                    list.append(inp)
                                    tooLarge = False
                                    input = True
                                    inp = 0
                                    user_inp = ''
                                    c += 1

                                else:
                                    tooLarge = True
                                    
                            except:
                                if c < 11:
                                    what = True
                        
                        elif c >= 11:
                            if len(user_inp) != 0:
                                full = True
                            else:
                                what = True

                                
            #   iterates all 12 values
            if input:
                var[c] = list[c] 
                input = False

        pygame.display.update()