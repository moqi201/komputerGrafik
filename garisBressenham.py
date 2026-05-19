import pygame
import sys

pygame.init()

wodh, height = 600, 400
screen = pygame.display.set_mode((wodh, height))
pygame.display.set_caption("Algoritma Garis Bresenham")

white = (255, 255, 255)
red = (255, 0, 0)

def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x = x1
    y = y1
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    if dx > dy :
        p = 2 * dy - dx  
        while x != x2:
            screen.set_at((x, y), white)
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy  
        while y != y2:
            screen.set_at((x, y), white)
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)
running = True
while running:
    screen.fill(red)
    bresenham(100, 100, 500, 300)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()