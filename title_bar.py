import pygame

# Initialize Pygame
pygame.init()

# Create a display window
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("My Custom Title")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

import pygame

# Initialize Pygame
pygame.init()

# Create a display window
screen = pygame.display.set_mode((800, 600))

# Load an icon (must be a Surface)
icon = pygame.image.load("icon.png")  # Path to your image file
pygame.display.set_icon(icon)

# Set a custom title
pygame.display.set_caption("Custom Icon Example")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()