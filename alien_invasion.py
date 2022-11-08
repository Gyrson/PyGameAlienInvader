import pygame
import sys
from settings import Settings

class AlienInvasion:
    '''Overall Class for the game and it's ressources.'''
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # Display Settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Vinvasion")
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            #Listens to Keyboard and Mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Sets Display every time we iterate
            #-- Background Color
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()