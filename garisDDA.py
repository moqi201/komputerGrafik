import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algoritma Garis DDA")

white = (255, 255, 255)
red = ()

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    steps = max(abs(dx), abs(dy))
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    
    for _ in range(steps + 1):
        screen.set_at((round(x), round(y)), red)
        x += x_increment
        y += y_increment

running = True
while running:
    screen.fill(white)
    dda(100, 100, 500, 300)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit() 
    