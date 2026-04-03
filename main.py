"""
Educational Game Suite - Main Launcher
A collection of educational games including Rock-Paper-Scissors, Math puzzles, and more
Built with Pygame
"""

import pygame
import sys
from pygame import mixer

# Import all game modules
from Assets import Game
from Assets import Combination
from Assets import Cramers
from Assets import Permutation
from Assets import Graph


def initialize_pygame():
    """Initialize Pygame and create the main display window"""
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()
    
    # Create display window
    WIDTH, HEIGHT = 1280, 720
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Educational Game Suite")
    
    return surface, WIDTH, HEIGHT


def run_game_menu(surface, width, height):
    """Main menu to select and run different games"""
    clock = pygame.time.Clock()
    FPS = 60
    running = True
    
    # Game options
    games = {
        "1": {"name": "Rock-Paper-Scissors Battle", "function": Game.runGame},
        "2": {"name": "Combination Puzzle", "function": Combination.runCombi},
        "3": {"name": "Cramer's Rule Solver", "function": Cramers.runCramers},
        "4": {"name": "Permutation Challenge", "function": Permutation.runPermu},
        "5": {"name": "Graph Visualization", "function": Graph.runGraph},
    }
    
    print("\n" + "="*50)
    print("  EDUCATIONAL GAME SUITE")
    print("="*50)
    print("\nAvailable Games:")
    for key, game in games.items():
        print(f"  {key}. {game['name']}")
    print("\n  Q. Quit")
    print("="*50)
    
    while running:
        user_input = input("\nSelect a game (1-5) or (Q to quit): ").strip().upper()
        
        if user_input == "Q":
            print("Goodbye!")
            return False
        
        if user_input in games:
            print(f"\nLaunching: {games[user_input]['name']}...")
            try:
                # Run the selected game
                title = pygame.display.set_caption(games[user_input]['name'])
                games[user_input]['function'](title, surface)
                
                # After game finishes, redisplay menu
                print("\n" + "="*50)
                print("  RETURNING TO MAIN MENU")
                print("="*50)
                print("\nAvailable Games:")
                for key, game in games.items():
                    print(f"  {key}. {game['name']}")
                print("\n  Q. Quit")
                print("="*50)
                
            except Exception as e:
                print(f"Error running game: {e}")
                print("Please try another game or check the assets folder.")
        else:
            print("Invalid choice. Please enter 1-5 or Q.")
    
    return True


def main():
    """Main entry point for the application"""
    try:
        # Initialize Pygame
        surface, width, height = initialize_pygame()
        
        # Run main menu loop
        run_game_menu(surface, width, height)
        
    except Exception as e:
        print(f"Fatal error: {e}")
        print("Make sure all game assets are in the 'Assets' folder.")
        print("Check the ASSETS.md file for required assets.")
        return 1
    finally:
        pygame.quit()
        sys.exit(0)


if __name__ == "__main__":
    main()
