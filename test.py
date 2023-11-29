import pygame
from pygame.locals import *

pygame.init()

# Fenstergröße
window_size = 800
square_size = window_size // 8

# Erstellen des Fensters
screen = pygame.display.set_mode((window_size, window_size), SRCALPHA)
pygame.display.set_caption("Transparentes Schachbrett")

# Laden des Hintergrundbildes und Anpassen der Alpha-Komponente
bg = pygame.image.load("Images/brett.png").convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Zeichnen des transparenten Hintergrunds
    screen.blit(bg, (0, 0))

    # Zeichnen des transparenten Schachbretts
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(screen, (col * square_size, row * square_size, square_size, square_size))

    pygame.display.update()

pygame.quit()
