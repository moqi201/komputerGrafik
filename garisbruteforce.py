import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Pengaturan layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritma Garis Brute Force")

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def draw_line_brute_force(x1, y1, x2, y2):
    # Menghitung gradien (m)
    # Persamaan: y = mx + c
    if x2 - x1 != 0:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        
        # Iterasi dari x awal ke x akhir
        # Kita asumsikan x1 < x2 untuk contoh ini
        start_x = int(min(x1, x2))
        end_x = int(max(x1, x2))
        
        for x in range(start_x, end_x + 1):
            y = m * x + c
            # Gambar pixel di koordinat (x, round(y))
            screen.set_at((x, round(y)), RED)
    else:
        # Penanganan khusus untuk garis vertikal (m tak terhingga)
        start_y = int(min(y1, y2))
        end_y = int(max(y1, y2))
        for y in range(start_y, end_y + 1):
            screen.set_at((int(x1), y), RED)

# Main Loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Contoh menggambar garis dari (100, 100) ke (500, 400)
    draw_line_brute_force(100, 100, 500, 400)
    
    pygame.display.flip()

pygame.quit()
sys.exit()