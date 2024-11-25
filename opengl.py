import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
print("OpenGL Vendor  :", glGetString(GL_VENDOR).decode())
print("OpenGL Renderer:", glGetString(GL_RENDERER).decode())
print("OpenGL Version :", glGetString(GL_VERSION).decode())
# Set up the perspective
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, display[0] / display[1], 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -5)  # Move into the screen

# Triangle vertices
vertices = np.array([
    [0.0, 1.0, 0.0],
    [-1.0, -1.0, 0.0],
    [1.0, -1.0, 0.0]
], dtype=np.float32)

def draw_triangle():
    """Renders a triangle."""
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3fv(vertices[0])
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3fv(vertices[1])
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3fv(vertices[2])
    glEnd()

# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Rotate the triangle
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)
    glRotatef(angle, 0, 1, 0)
    angle += 1

    draw_triangle()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
