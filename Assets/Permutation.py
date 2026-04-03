import pygame, sys
import time
from pygame import *
from Assets import buttonGame
from Assets import Sound
from Assets import backButton
from Assets import permuSolve

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
def runPermu(title, surface):
    bk = False
    runP = True
    first = False
    printN = False
    printR = False
    solved = False
    temp = ""
    inp = []
    x = 760
    y = 90
    count = 0
    button = 0
    val = 0
    n = 0
    r = 0
    result = 0
    tt = 0
    rformat = ""
    shadow = pygame.Color("#b77d74")
    color = pygame.Color("#fdaa99")
    
    #   load font
    font = pygame.font.Font("Assets\\fonts\\upheavtt.ttf", 100)
    font2 = pygame.font.Font("Assets\\fonts\\upheavtt.ttf", 80)
    
    
    #   load number images
    num1 = pygame.image.load("Assets\\numButtons\\num 1.png").convert_alpha()
    num2 = pygame.image.load("Assets\\numButtons\\num 2.png").convert_alpha()
    num3 = pygame.image.load("Assets\\numButtons\\num 3.png").convert_alpha()
    num4 = pygame.image.load("Assets\\numButtons\\num 4.png").convert_alpha()
    num5 = pygame.image.load("Assets\\numButtons\\num 5.png").convert_alpha()
    num6 = pygame.image.load("Assets\\numButtons\\num 6.png").convert_alpha()
    num7 = pygame.image.load("Assets\\numButtons\\num 7.png").convert_alpha()
    num8 = pygame.image.load("Assets\\numButtons\\num 8.png").convert_alpha()
    num9 = pygame.image.load("Assets\\numButtons\\num 9.png").convert_alpha()
    num0 = pygame.image.load("Assets\\numButtons\\num 0.png").convert_alpha()
    
    one = pygame.image.load("Assets\\numButtons\\1.png").convert_alpha()
    two = pygame.image.load("Assets\\numButtons\\2.png").convert_alpha()
    three = pygame.image.load("Assets\\numButtons\\3.png").convert_alpha()
    four = pygame.image.load("Assets\\numButtons\\4.png").convert_alpha()
    five = pygame.image.load("Assets\\numButtons\\5.png").convert_alpha()
    six = pygame.image.load("Assets\\numButtons\\6.png").convert_alpha()
    seven = pygame.image.load("Assets\\numButtons\\7.png").convert_alpha()
    eight = pygame.image.load("Assets\\numButtons\\8.png").convert_alpha()
    nine = pygame.image.load("Assets\\numButtons\\9.png").convert_alpha()
    zero = pygame.image.load("Assets\\numButtons\\0.png").convert_alpha()

    #   hover images
    num1h = pygame.image.load("Assets\\numButtons\\num 1 h.png").convert_alpha()
    num2h = pygame.image.load("Assets\\numButtons\\num 2 h.png").convert_alpha()
    num3h = pygame.image.load("Assets\\numButtons\\num 3 h.png").convert_alpha()
    num4h = pygame.image.load("Assets\\numButtons\\num 4 h.png").convert_alpha()
    num5h = pygame.image.load("Assets\\numButtons\\num 5 h.png").convert_alpha()
    num6h = pygame.image.load("Assets\\numButtons\\num 6 h.png").convert_alpha()
    num7h = pygame.image.load("Assets\\numButtons\\num 7 h.png").convert_alpha()
    num8h = pygame.image.load("Assets\\numButtons\\num 8 h.png").convert_alpha()
    num9h = pygame.image.load("Assets\\numButtons\\num 9 h.png").convert_alpha()
    num0h = pygame.image.load("Assets\\numButtons\\num 0 h.png").convert_alpha()
    
    #   backspace
    back = pygame.image.load("Assets\\numButtons\\backspace.png").convert_alpha()
    backh = pygame.image.load("Assets\\numButtons\\backspace hover.png").convert_alpha()
    
    #   board
    board = pygame.image.load("Assets\\numButtons\\board.png").convert_alpha()
    board2 = pygame.image.load("Assets\\numButtons\\board2.png").convert_alpha()
    
    #   enter
    enter = pygame.image.load("Assets\\numButtons\\ent.png").convert_alpha()
    enterh = pygame.image.load("Assets\\numButtons\\ent hover.png").convert_alpha()
    
    #   n and r values
    nval = pygame.image.load("Assets\\numButtons\\n.png").convert_alpha()
    rval = pygame.image.load("Assets\\numButtons\\r.png").convert_alpha()
    eq = pygame.image.load("Assets\\numButtons\\eq.png").convert_alpha()
    
    
    #   create button
    num1_btn = buttonGame.Buttons(100, 100, num1, num1h, 6)
    num2_btn = buttonGame.Buttons(230, 100, num2, num2h, 6)
    num3_btn = buttonGame.Buttons(360, 100, num3, num3h, 6)
    num4_btn = buttonGame.Buttons(100, 245, num4, num4h, 6)
    num5_btn = buttonGame.Buttons(230, 245, num5, num5h, 6)
    num6_btn = buttonGame.Buttons(360, 245, num6, num6h, 6)
    num7_btn = buttonGame.Buttons(100, 390, num7, num7h, 6)
    num8_btn = buttonGame.Buttons(230, 390, num8, num8h, 6)
    num9_btn = buttonGame.Buttons(360, 390, num9, num9h, 6)
    num0_btn = buttonGame.Buttons(230, 530, num0, num0h, 6)
    back_btn = buttonGame.Buttons(510, 100, back, backh, 6)
    enter_btn = buttonGame.Buttons(510, 245, enter, enterh, 6)
    
    #   load background image
    bg = pygame.image.load("Assets\\backgrounds\\permu bg.png").convert_alpha()
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    scroll = 0
    
    #   window loop (updates based on FPS)
    while runP:
        #   set fps
        clock.tick(FPS)
        
        #   set title
        title = pygame.display.set_caption("Counting Principle : Permutation")
        
        
        #   set transition to black
        surface.blit(trans, (0, 0))
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
                
            
            #   play click when hovered
            num0_btn.playHover(surface)
            num1_btn.playHover(surface)
            num2_btn.playHover(surface)
            num3_btn.playHover(surface)
            num4_btn.playHover(surface)
            num5_btn.playHover(surface)
            num6_btn.playHover(surface)
            num7_btn.playHover(surface)
            num8_btn.playHover(surface)
            num9_btn.playHover(surface)
            back_btn.playHover(surface)
            enter_btn.playHover(surface)
            
            #   display board
            surface.blit(board2, (795, y - 5))
            
            
            #   updates r and n value
            text1 = font.render(f"{n}", False, color)
            text2 = font.render(f"{r}", False, color)
            sh1 = font.render(f"{n}", False, shadow)
            sh2 = font.render(f"{r}", False, shadow)
            textr = font2.render(f"{rformat}", False, color)
            shr = font2.render(f"{rformat}", False, shadow)
     
            if printN:
                #    display n value
                surface.blit(nval, (850, 245))
                surface.blit(eq, (920, 270))
                surface.blit(sh1, (995, 255))
                surface.blit(text1, (1000, 250))

                #   display r input
                surface.blit(rval, (x - 100, y))
                surface.blit(eq, (x - 23, y + 15))
            
            if printR:
                #   display n value
                surface.blit(nval, (850, 245))
                surface.blit(eq, (920, 270))
                surface.blit(sh1, (995, 255))
                surface.blit(text1, (1000, 250))
                
                #   display r value
                surface.blit(rval, (850, 345))
                surface.blit(eq, (920, 370))
                surface.blit(sh2, (995, 355))
                surface.blit(text2, (1000, 350))
                
                #   display upcoming n input
                surface.blit(nval, (x - 100, y))
                surface.blit(eq, (x - 23, y + 15))
                
                if solved == True:
                    surface.blit(eq, (535, 560))
                    surface.blit(board, (600, 530))
                    surface.blit(shr, (660 - 5, 560 + 5))
                    surface.blit(textr, (660, 560))
                    
                
            
            if printR == False and printN == False:
                #   display n input
                surface.blit(nval, (x - 100, y))
                surface.blit(eq, (x - 23, y + 15))
            
            
            #   display numbers
            if num0_btn.draw(surface):
                val = 10
            if num1_btn.draw(surface):
                val = 1
            if num2_btn.draw(surface):
                val = 2
            if num3_btn.draw(surface):
                val = 3
            if num4_btn.draw(surface):
                val = 4
            if num5_btn.draw(surface):
                val = 5
            if num6_btn.draw(surface):
                val = 6
            if num7_btn.draw(surface):
                val = 7
            if num8_btn.draw(surface):
                val = 8
            if num9_btn.draw(surface):
                val = 9
            
            #   if user press backspace
            if back_btn.draw(surface):
                Sound.play_click()
                if button > 0:
                    button -= 1
                    inp.pop()


            #   checks if button has been pressed
            if val != 0:
                Sound.play_click()
                if button < 4:
                    button += 1
                
                    #   checks if value is zero
                    if val == 10:
                        inp.append(0)
                    else:
                        inp.append(val)
                    
                #   resets value
                val = 0
                
            if button >= 1:
                if inp[0] == 1:
                    surface.blit(one, (x + (100 * 1), y))
                if inp[0] == 2:
                    surface.blit(two, (x + (90 * 1), y))
                if inp[0] == 3:
                    surface.blit(three, (x + (90 * 1), y))
                if inp[0] == 4:
                    surface.blit(four, (x + (90 * 1), y))
                if inp[0] == 5:
                    surface.blit(five, (x + (90 * 1), y))
                if inp[0] == 6:
                    surface.blit(six, (x + (90 * 1), y))
                if inp[0] == 7:
                    surface.blit(seven, (x + (90 * 1), y))
                if inp[0] == 8:
                    surface.blit(eight, (x + (90 * 1), y))
                if inp[0] == 9:
                    surface.blit(nine, (x + (90 * 1), y))
                if inp[0] == 0:
                    surface.blit(zero, (x + (90 * 1), y))
                
            if button >= 2:
                if inp[1] == 1:
                    surface.blit(one, (x + (100 * 2), y))
                if inp[1] == 2:
                    surface.blit(two, (x + (90 * 2), y))
                if inp[1] == 3:
                    surface.blit(three, (x + (90 * 2), y))
                if inp[1] == 4:
                    surface.blit(four, (x + (90 * 2), y))
                if inp[1] == 5:
                    surface.blit(five, (x + (90 * 2), y))
                if inp[1] == 6:
                    surface.blit(six, (x + (90 * 2), y))
                if inp[1] == 7:
                    surface.blit(seven, (x + (90 * 2), y))
                if inp[1] == 8:
                    surface.blit(eight, (x + (90 * 2), y))
                if inp[1] == 9:
                    surface.blit(nine, (x + (90 * 2), y))
                if inp[1] == 0:
                    surface.blit(zero, (x + (90 * 2), y))
                    
            if button >= 3:
                if inp[2] == 1:
                    surface.blit(one, (x + (100 *3), y))
                if inp[2] == 2:
                    surface.blit(two, (x + (90 * 3), y))
                if inp[2] == 3:
                    surface.blit(three, (x + (90 * 3), y))
                if inp[2] == 4:
                    surface.blit(four, (x + (90 * 3), y))
                if inp[2] == 5:
                    surface.blit(five, (x + (90 * 3), y))
                if inp[2] == 6:
                    surface.blit(six, (x + (90 * 3), y))
                if inp[2] == 7:
                    surface.blit(seven, (x + (90 * 3), y))
                if inp[2] == 8:
                    surface.blit(eight, (x + (90 * 3), y))
                if inp[2] == 9:
                    surface.blit(nine, (x + (90 * 3), y))
                if inp[2] == 0:
                    surface.blit(zero, (x + (90 * 3), y))
                    
            if button >= 4:
                if inp[3] == 1:
                    surface.blit(one, (x + (100 * 4), y))
                if inp[3] == 2:
                    surface.blit(two, (x + (90 * 4), y))
                if inp[3] == 3:
                    surface.blit(three, (x + (90 * 4), y))
                if inp[3] == 4:
                    surface.blit(four, (x + (90 * 4), y))
                if inp[3] == 5:
                    surface.blit(five, (x + (90 * 4), y))
                if inp[3] == 6:
                    surface.blit(six, (x + (90 * 4), y))
                if inp[3] == 7:
                    surface.blit(seven, (x + (90 * 4), y))
                if inp[3] == 8:
                    surface.blit(eight, (x + (90 * 4), y))
                if inp[3] == 9:
                    surface.blit(nine, (x + (90 * 4), y))
                if inp[3] == 0:
                    surface.blit(zero, (x + (90 * 4), y))
                
            if enter_btn.draw(surface):
                Sound.play_click()
                
                if len(inp) != 0:
                
                    if solved == True:
                        n = 0
                        r = 0
                        result = 0
                        solved = False
                    
                    if first == False:
                        for i in inp:
                            temp += str(i)
                            
                        n = int(temp)
                        printN = True
                        printR = False
                        first = True
                    
                    if first == True and temp == "":
                        for i in inp:
                            temp += str(i)
                            
                        r = int(temp)
                        printR = True
                        printN = False
                        first = False     
                       
                    #   resets
                    inp.clear()
                    button = 0
                    space = 0
                    temp = ""
                    
            
            if solved == False and printR == True:
                result = permuSolve.solve(n, r)
                if result == -1:
                    rformat = "TOO LARGE!"
                elif result >= 1000000000:
                    tt = format(float(result), ".3E")
                    rformat = str(tt)
                else:
                    rformat = str(result)
                
                solved = True
                
                 
            #   display back button
            if backButton.bk_btn(surface):
                Sound.play_click()
                bk = True
                return backButton.bk_btn(surface)
        
        #   event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if bk == True:
                runC = False
                bk = False
        
        pygame.display.update()
        
    
    