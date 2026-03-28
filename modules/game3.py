import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Ball settings
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 20
ball_velocity = [4, 4]  # X speed, Y speed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update Position ---
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # --- Check Boundaries (Bounce) ---
    # Left or Right Wall
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
        ball_velocity[0] = -ball_velocity[0] # Reverse X direction
    
    # Top or Bottom Wall
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
        ball_velocity[1] = -ball_velocity[1] # Reverse Y direction

    # --- Drawing ---
    screen.fill((20, 20, 40)) # Dark Blue
    pygame.draw.circle(screen, (0, 255, 255), (ball_pos[0], ball_pos[1]), ball_radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()