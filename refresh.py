import pygame

# Initialize Pygame
pygame.init()

# Create a clock object
clock = pygame.time.Clock()

# Get the dimensions of the display
display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h

# Create a fullscreen window
window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Pixel Refresh")
pygame.mouse.set_visible(False)

color_state = 0
colors = [
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (0, 255, 255),   # Cyan
    (255, 0, 255),   # Magenta
    (255, 255, 255), # White
    (0, 0, 0)        # Black
]

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Check for ESC key
                running = False

    color = colors[color_state]

    # Set color based on state
    color_state = (color_state + 1) % len(colors)
    color = colors[color_state]

    window.fill(color)
    # Limit the refresh rate to 1 FPS
    clock.tick(1)
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
