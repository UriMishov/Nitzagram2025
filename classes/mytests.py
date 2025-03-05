import pygame
pygame.display.set_mode((489, 270))

image = pygame.image.load("Images/background.png")
pygame.screen.blit(image)

while True:
    pygame.display.fill(45, 78, 12)
