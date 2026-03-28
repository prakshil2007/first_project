import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mouse & Text Demo")

# Font setup
font = pygame.font.Font(None, 36) # None uses default system font

# Button Setup
button_rect = pygame.Rect(225, 175, 150, 50)
button_color = (0, 200, 0)
text_color = (255, 255, 255)
click_count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # collidepoint checks if a point is inside a rectangle
            if button_rect.collidepoint(mouse_pos):
                click_count += 1
                button_color = (0, 255, 0) # Flash bright green
        
        if event.type == pygame.MOUSEBUTTONUP:
            button_color = (0, 200, 0) # Return to normal green

    screen.fill((255, 255, 255))

    # Draw Button
    pygame.draw.rect(screen, button_color, button_rect)
    
    # Render Text
    btn_text = font.render("Click Me!", True, text_color)
    count_text = font.render(f"Clicks: {click_count}", True, (0, 0, 0))

    # Center text on button
    text_rect = btn_text.get_rect(center=button_rect.center)
    
    # Blit (draw) text onto screen
    screen.blit(btn_text, text_rect)
    screen.blit(count_text, (20, 20))

    pygame.display.flip()

pygame.quit()