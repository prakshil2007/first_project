import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (30, 30, 30) # Dark Grey

# 3. Setup Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Boilerplate")
clock = pygame.time.Clock()

# 4. Game Loop
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Drawing ---
    screen.fill(BACKGROUND_COLOR) # Clear screen
    pygame.display.flip()         # Update display

    # --- Limit FPS ---
    clock.tick(60)

pygame.quit()
sys.exit()