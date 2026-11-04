import sys
import pygame

# Initialize Pygame
pygame.init()

# Window Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame!")
clock = pygame.time.Clock()

running = True
while running:
    # 1. EVENT HANDLING (Input from user)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(60)

# Clean exit
pygame.quit()
sys.exit()