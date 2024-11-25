import pygame
import cv2
import numpy as np

# Initialize Pygame
pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Screen Recording Example")
clock = pygame.time.Clock()

# Set up video writer
fps = 30
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for MP4
video_writer = cv2.VideoWriter("output.mp4", fourcc, fps, (screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Example Pygame drawing
    screen.fill((0, 0, 0))  # Clear screen with black
    pygame.draw.circle(screen, (255, 0, 0), (screen_width // 2, screen_height // 2), 50)
    pygame.display.flip()

    # Capture the Pygame screen as an array
    frame = pygame.surfarray.array3d(screen)  # Get RGB array
    frame = np.flip(frame, axis=0)  # Flip vertically
    frame = np.rot90(frame)  # Rotate to match the correct orientation
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

    # Write the frame to the video
    video_writer.write(frame)

    clock.tick(fps)

# Cleanup
video_writer.release()
pygame.quit()
