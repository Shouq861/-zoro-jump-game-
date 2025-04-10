import pygame
import sys

# تهيئة Pygame
pygame.init()

# إعداد الشاشة
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zorro Jump Game")

# تحميل صورة الخلفية
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# الألوان
BROWN = (139, 69, 19)

# المتغيرات
clock = pygame.time.Clock()
ground_y = 350
running = True

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # رسم الأرض
    pygame.draw.rect(screen, BROWN, (0, ground_y, WIDTH, HEIGHT - ground_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()