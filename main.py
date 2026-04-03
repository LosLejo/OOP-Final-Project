"""
Educational Game Suite - Main Launcher
A collection of educational games including Rock-Paper-Scissors, Math puzzles, and more
Built with Pygame with GUI menu
"""

import pygame
import sys
import math
import time
from pygame import mixer

# Import all game modules
from Assets import Game
from Assets import Combination
from Assets import Cramers
from Assets import Permutation
from Assets import Graph
from Assets import Sound
from Assets import buttonGame


def main():
    """Main entry point - GUI-based menu"""
    try:
        # Initialize pygame, mixer, and sound
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        
        # Updates per second
        clock = pygame.time.Clock()
        FPS = 60
        
        # Screen dimensions
        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720
        
        # Create game window
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        maintitle = pygame.display.set_caption("Educational Game Suite")
        Sound.play_lofi()
        
        # Load images
        permu = pygame.image.load("Assets\\buttons\\permutation button.png").convert_alpha()
        combi = pygame.image.load("Assets\\buttons\\combination button.png").convert_alpha()
        cramers = pygame.image.load("Assets\\buttons\\cramer's rule.png").convert_alpha()
        game_img = pygame.image.load("Assets\\buttons\\game button.png").convert_alpha()
        graph = pygame.image.load("Assets\\buttons\\graph button.png").convert_alpha()
        exit_img = pygame.image.load("Assets\\buttons\\exit button.png").convert_alpha()
        bg = pygame.image.load("Assets\\backgrounds\\main bg.png").convert_alpha()
        bg_width = bg.get_width()
        
        # Hover button images
        perhover = pygame.image.load("Assets\\buttons\\permu hover.png").convert_alpha()
        comhover = pygame.image.load("Assets\\buttons\\combi hover.png").convert_alpha()
        cramhover = pygame.image.load("Assets\\buttons\\cramer hover.png").convert_alpha()
        playhover = pygame.image.load("Assets\\buttons\\playgame hover.png").convert_alpha()
        graphhover = pygame.image.load("Assets\\buttons\\graph hover.png").convert_alpha()
        exithover = pygame.image.load("Assets\\buttons\\exit hover.png").convert_alpha()
        
        # Create button instances
        permu_btn = buttonGame.Buttons(350, 400, permu, perhover, 6)
        combi_btn = buttonGame.Buttons(350, 510, combi, comhover, 6)
        cramers_btn = buttonGame.Buttons(680, 400, cramers, cramhover, 6)
        game_btn = buttonGame.Buttons(680, 510, game_img, playhover, 6)
        graph_btn = buttonGame.Buttons(520, 620, graph, graphhover, 6)
        exit_btn = buttonGame.Buttons(1190, 12, exit_img, exithover, 6)
        
        # Load title
        title = pygame.image.load("Assets\\title.png").convert_alpha()
        resized_title = pygame.transform.scale(title, (700, 338))
        title_rect = title.get_rect(topleft=[290, -500])
        
        # Game variables
        scroll = 0
        tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
        
        # Button flags
        runExit = False
        runGame = False
        runPermu = False
        runCombi = False
        runCramers = False
        runGraph = False
        
        # Game loop
        run = True
        while run:
            clock.tick(FPS)
            
            # Draw scrolling background
            for i in range(0, tiles):
                screen.blit(bg, (i * bg_width + scroll, 0))
            # Scroll background
            scroll -= 1
            
            # Reset scroll
            if abs(scroll) > bg_width:
                scroll = 0
            
            # Display title
            screen.blit(resized_title, title_rect)
            
            # Animate title
            if title_rect.bottom <= 450:
                title_rect.bottom += 4
            
            if title_rect.bottom == 454:
                # Display buttons
                if permu_btn.draw(screen):
                    Sound.play_click()
                    runPermu = True
                    
                if combi_btn.draw(screen):
                    Sound.play_click()
                    runCombi = True
                
                if cramers_btn.draw(screen):
                    Sound.play_click()
                    runCramers = True
                
                if game_btn.draw(screen):
                    Sound.play_click()
                    runGame = True
                   
                if graph_btn.draw(screen):
                    Sound.play_click()
                    runGraph = True
                
                if exit_btn.draw(screen):
                    Sound.play_click()
                    runExit = True
            
            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            # Handle game launches (outside event loop so they run every frame)
            if runCombi:
                Combination.runCombi(maintitle, screen)
                runCombi = False
                maintitle = pygame.display.set_caption("Educational Game Suite")
            
            if runPermu:
                Permutation.runPermu(maintitle, screen)
                runPermu = False
                maintitle = pygame.display.set_caption("Educational Game Suite")
            
            if runCramers:
                Cramers.runCramers(maintitle, screen)
                runCramers = False
                maintitle = pygame.display.set_caption("Educational Game Suite")
            
            if runGame:
                Sound.stop_lofi()
                Game.runGame(maintitle, screen)
                Sound.play_lofi()
                runGame = False
                maintitle = pygame.display.set_caption("Educational Game Suite")
                
            if runGraph:
                try:
                    Graph.runGraph(maintitle, screen)
                    runGraph = False
                    maintitle = pygame.display.set_caption("Educational Game Suite")
                except Exception as e:
                    print(f"Graph game error: {e}")
                    runGraph = False
            
            if runExit:
                time.sleep(0.5)
                run = False
            
            # Update window 
            pygame.display.update()
        
        # Cleanup
        Sound.stop_lofi()
        pygame.quit()
        return 0
        
    except Exception as e:
        print(f"Fatal error: {e}")
        print("Make sure all game assets are in the 'Assets' folder.")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
