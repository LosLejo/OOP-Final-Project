from tkinter import Y
import pygame, sys
import time
from pygame import *
from Assets import menuBox
from Assets import backButton
from Assets import buttonGame
from Assets import Sound
from Assets import healthBar
from Assets import rockPaperScissors

#   initialize pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#   set FPS
clock = pygame.time.Clock()
FPS = 60

#   main function
def runGame(title, surface):
    
    #   function variables
    bk = False
    runC = True
    lose = False
    loseComputer = False
    flicker = True
    menu = False
    userPicked = False
    compPicked = False
    tie = False
    soundeffect = False
    youWin = False
    youLose = False
    w = False
    l = False
    count = 0
    ccount = 0
    opac = 255
    flick = 20
    user = 0
    temp = 0
    computer = 0
    animate = 0
    userDamage = 0
    compDamage = 0
    delay = 0
    cccount = 0
    trans = 0
    
    Sound.play_battle()
    hp = healthBar.health()
    comphp = healthBar.health()
    
    #   surface declaration (pygame.SRCALPHA)
    surf = pygame.Surface((1280, 720), pygame.SRCALPHA)
    
    surf2 = pygame.Surface([1280, 720], pygame.SRCALPHA, 32)
    
    #   function draw end screen transition
    def draw_end():
        pygame.draw.rect(surf2, (255, 255, 255, 3), [0, 0, 1280, 720])

    #   transition function
    def draw_trans():
        pygame.draw.rect(surf, (255, 255, 255, flick), [0, 0, 1280, 720])
    
    def flicker():
        pygame.draw.rect(surf, (255, 255, 255, opac), [0, 0, 1280, 720])
    
    #   load background image
    bg = pygame.image.load("Assets\\backgrounds\\game bg.png").convert_alpha()
    bg_width = bg.get_width()
    scroll = 0
    
    #   load rock, paper, scissors images
    rock = pygame.image.load("Assets\\rock paper scissors\\rock.png").convert_alpha()
    paper = pygame.image.load("Assets\\rock paper scissors\\paper.png").convert_alpha()
    scissors = pygame.image.load("Assets\\rock paper scissors\\scissors.png").convert_alpha()
    arrow = pygame.image.load("Assets\\rock paper scissors\\arrow.png").convert_alpha()
    
    rockh = pygame.image.load("Assets\\rock paper scissors\\rockh.png").convert_alpha()
    paperh = pygame.image.load("Assets\\rock paper scissors\\paperh.png").convert_alpha()
    scissorsh = pygame.image.load("Assets\\rock paper scissors\\scissorh.png").convert_alpha()

    #   load text images
    rr = pygame.image.load("Assets\\gametext\\user.png").convert_alpha()
    vs = pygame.image.load("Assets\\gametext\\vs.png").convert_alpha()
    cc = pygame.image.load("Assets\\gametext\\computer.png").convert_alpha()
    challenger = pygame.image.load("Assets\\gametext\\challenger.png").convert_alpha()
    Win = pygame.image.load("Assets\\gametext\\win.png").convert_alpha()
    Lose = pygame.image.load("Assets\\gametext\\lose.png").convert_alpha()
    
    #   load enemy images
    erock = pygame.image.load("Assets\\rock paper scissors\\Computer\\rock.png").convert_alpha()
    epaper = pygame.image.load("Assets\\rock paper scissors\\Computer\\paper.png").convert_alpha()
    escissors = pygame.image.load("Assets\\rock paper scissors\\Computer\\scissors.png").convert_alpha()
    earrow = pygame.image.load("Assets\\rock paper scissors\Computer\\arrow.png").convert_alpha()
    
    erockh = pygame.image.load("Assets\\rock paper scissors\\Computer\\rockh.png").convert_alpha()
    epaperh = pygame.image.load("Assets\\rock paper scissors\\Computer\\paperh.png").convert_alpha()
    escissorsh = pygame.image.load("Assets\\rock paper scissors\\Computer\\scissorh.png").convert_alpha()
    
    #   create buttons
    rock_btn = buttonGame.Buttons(215, 150, rock, rockh, 3)
    paper_btn = buttonGame.Buttons(215, 330, paper, paperh, 3)
    scissors_btn = buttonGame.Buttons(215, 530, scissors, scissorsh, 3)

        
    #   window loop (updates based on FPS)
    while runC:
        #   set fps
        clock.tick(FPS)
        
        #   set title
        title = pygame.display.set_caption("Test your luck!")
        
        #   set transition to white
        surface.blit(surf, (0, 0))
        draw_trans()
        
        #   set momentarily delay
        if count <= 53:
            count += 1
        
        if count == 54:
            
            while ccount <= 130:
                clock.tick(FPS)
                
                opac -= 5
                #   set to screen black momentarily
                surface.fill('black')
                #   set to white then fade
                surface.blit(surf, (0, 0))
                #   flicker function with opac variable
                flicker()    
                if opac <= 150:
                    opac = 255
                surface.blit(challenger, (190, 260))
            
                ccount += 1
                pygame.display.update()
                
            #   display scrolling bg
            for i in range(0, 3):
                surface.blit(bg, (i * bg_width + scroll, 0))
            #   set scroll speed
            scroll -= 1
    
            #   reset scroll
            if abs(scroll) > bg_width:
                scroll = 0
                    
             #   display hearts
            hp.draw(surface)
            
            #   display computer hearts
            comphp.drawOp(surface)
            
            #   user cursor
            if rock_btn.checkHover(surface):
                surface.blit(arrow, (110, 160))
            rock_btn.playHover(surface)
            
            if paper_btn.checkHover(surface):
                surface.blit(arrow, (110, 347))
            paper_btn.playHover(surface)
            
            if scissors_btn.checkHover(surface):
                surface.blit(arrow, (110, 540))
            scissors_btn.playHover(surface)

            #   display computer rock, paper, scissors buttons    
            surface.blit(erock, (900, 150))     
            surface.blit(epaper, (860, 330))   
            surface.blit(escissors, (860, 530))
            #   display user vs. computer
            surface.blit(vs, (560, 260))
            surface.blit(cc, (575, 293))
            surface.blit(rr, (470, 220))

            #   display back button
            if backButton.bk_btn(surface):
                Sound.stop_battle()
                Sound.play_click()
                bk = True
                return backButton.bk_btn(surface)

            #   set user choice
            if rock_btn.draw(surface):
                Sound.play_click()
                user = 1
                menu = True

            if paper_btn.draw(surface):
                Sound.play_click()
                user = 2
                menu = True
      
            if scissors_btn.draw(surface):
                Sound.play_click()
                user = 3
                menu = True
            
            #   display's confirmation Menu
            if menu:
                temp = menuBox.menu(title, surface, user)
                menu = False
            
            #   gets user input
            if temp != 0:
                userPicked = True
                user = temp
                temp = 0

            #   gets computer random input and triggers animation
            if compPicked == False and userPicked == True:
                temp = rockPaperScissors.randomChoice(computer)
                computer = temp
                temp = 0
                compPicked = True
                
            #   check who wins and resets
            if compPicked == True and userPicked == True:
                temp = rockPaperScissors.whoWin(user, computer)
                compPicked = False
                userPicked = False
            
                #   display's who wins and calculate damage
            if temp == 1:
                temp = 0
                tie = True
           
            if temp == 2:
                temp = 0
                loseComputer = True
            
            if temp == 3:
                temp = 0
                lose = True
                
            # sets delay
            if delay <= 10 and (loseComputer or lose or tie):
                delay += 1
            
            if delay == 11:
                
                Sound.play_click()
                soundeffect = True
                #   display computer cursor
                while animate <= 200:
                    clock.tick(FPS)
                    
                    #   display scrolling bg
                    for i in range(0, 3):
                        surface.blit(bg, (i * bg_width + scroll, 0))
                    #   set scroll speed
                    scroll -= 1
                    
                    #   reset scroll
                    if abs(scroll) > bg_width:
                        scroll = 0
                    
                     #   display hearts
                    hp.draw(surface)
            
                    #   display computer hearts
                    comphp.drawOp(surface)
                    
                    #   display computer vs user
                    if compDamage == 3 or userDamage == 3:
                        surface.blit(vs, (560, 260))
                        surface.blit(cc, (575, 293))
                        surface.blit(rr, (470, 220))
                
                    #   display user choice
                    if user == 1:
                        surface.blit(rockh, (215, 143))
                        surface.blit(arrow, (110, 160))
                        
                    if user == 2:
                        surface.blit(paperh, (215, 323)) 
                        surface.blit(arrow, (110, 347))
                        
                    if user == 3:
                        surface.blit(scissorsh, (215, 523))
                        surface.blit(arrow, (110, 540))
                        
                    
                    if computer == 1:
                        surface.blit(erockh, (900, 143)) 
                        surface.blit(earrow, (1090, 150))
                                    
                    if computer == 2:
                        surface.blit(epaperh, (860, 323))  
                        surface.blit(earrow, (1090, 330))

                
                    if computer == 3:
                        surface.blit(escissorsh, (860, 523))
                        surface.blit(earrow, (1090, 530))
                    
                    if soundeffect:
                        Sound.play_attack()
                        soundeffect = False
                        
                        
                    animate += 1
                    pygame.display.update()
                    
                #   Resets animation
                animate = 0
                delay = 0
                tie = False
                
                #   set damage
                if lose == True:
                    hp.getDmg()
                    userDamage += 1
                    lose = False
            
                #   set computer damage
                if loseComputer == True:
                    comphp.getDmg()
                    compDamage += 1
                    loseComputer = False
                
                user = 0
                computer = 0

            # if you lost 3 imes
            if userDamage == 3:
                print(userDamage)
                youLose = True
            
            #   if computer lose 3 times
            if compDamage == 3:
                print(compDamage)
                youWin = True
            
            #   activates end screen
            if youLose or youWin:
                
                while cccount <= 350:
                    clock.tick(FPS)
                    
                    
                    #   transition to white
                    trans += 1
                    if trans <= 300:
                        surface.blit(surf2, (0, 0))
                        draw_end()
                        
                    #   checks if you lose
                    if youLose:
                        Sound.stop_battle()
                        Sound.play_lose()
                        youLose = False
                        l = True
                    
                    #   checks if you win
                    if youWin:
                        Sound.stop_battle()
                        Sound.play_win()
                        youWin = False
                        w = True
                    
                    #   Display you win!
                    if w:
                        surface.blit(Win, (420, 250))
                    
                    #   Display you Lose!
                    if l:
                        surface.blit(Lose, (420, 250))
                        
                    cccount += 1
                    pygame.display.update()
            
            if cccount == 351:
                runGame = False
                bk = True
                
        #   event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if bk == True:
                runC = False
                bk = False

        pygame.display.update()
    
    
    