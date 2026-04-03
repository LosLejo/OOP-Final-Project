import pygame
from pygame import mixer

#   initialize pygame, mixer, and sound
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

lofi = pygame.mixer.Sound("Assets\\Sounds\\lofi bg.wav")
lofi.set_volume(0.2)

click_sfx = pygame.mixer.Sound("Assets\\Sounds\\click sfx.wav")
click_sfx.set_volume(0.5)

battle = pygame.mixer.Sound("Assets\\Sounds\\game bg.wav")
battle.set_volume(0.1)

hover_sfx = pygame.mixer.Sound("Assets\\Sounds\\hover.wav")
hover_sfx.set_volume(2)

attack_sfx = pygame.mixer.Sound("Assets\\Sounds\\attack.wav")
attack_sfx.set_volume(0.2)

win_sfx = pygame.mixer.Sound("Assets\\Sounds\\win.wav")
win_sfx.set_volume(0.2)

lose_sfx = pygame.mixer.Sound("Assets\\Sounds\\lose.wav")
lose_sfx.set_volume(0.2)

def play_win():
    win_sfx.play()

def play_lose():
    lose_sfx.play()

def play_attack():
    attack_sfx.play()

def play_lofi():
    lofi.play(-1)

def play_click():
    click_sfx.play()

def stop_lofi():
    lofi.fadeout(1)
    
def play_battle():
    battle.play(-1)
        
def stop_battle():
    battle.fadeout(1)
    
def play_hover():
    hover_sfx.play()