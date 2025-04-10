import pygame
import sys

# تهيئة مكتبة Pygame
pygame.init()

# إعداد حجم الشاشة
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zoro Jump")

# تحديد الألوان
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)

# إعداد اللاعب (مؤقتًا مربع أخضر)
player = pygame.Rect(100, 300, 50, 50)
velocity = 0
is_jumping = False
gravity = 0.8
ground_y = 350

# التحكم في سرعة التحديث
clock = pygame.time.Clock()

# حلقة اللعبة
running = True
while running:
    screen.fill(WHITE)  # الخلفية

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # القفز بزر المسافة أو الضغط بالماوس
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not is_jumping:
                velocity = -15
                is_jumping = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_jumping:
                velocity = -15
                is_jumping = True

    # تطبيق القفز
    if is_jumping:
        player.y += int(velocity)
        velocity += gravity
        if player.y >= ground_y - player.height:
            player.y = ground_y - player.height
            is_jumping = False

    # رسم الأرض واللاعب
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, (139, 69, 19), (0, ground_y, WIDTH, HEIGHT - ground_y))  # الأرض

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()