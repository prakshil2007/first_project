import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Player settings
x, y = 300, 200  # Starting position
player_size = 50
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Input Handling ---
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # --- Drawing ---
    screen.fill((0, 0, 0)) # Black background
    
    # Draw the player (Surface, Color, Rect(x, y, width, height))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, player_size, player_size))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
