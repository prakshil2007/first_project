import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255)) # Fill screen with white
    pygame.display.flip()

pygame.quit()