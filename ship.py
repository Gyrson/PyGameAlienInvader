import pygame

class Ship:
    '''A Class to manage the Ship'''

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Lädt das Bild des schiffes und ruft dessen umebendes Rechteck an
        self.image = pygame.image.load("Images/ship.bmp")
        self.rect = self.image.get_rect()

        # Platzieren des Schiffes
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)