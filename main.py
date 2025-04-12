import pygame
import sys
import random

pygame.init()

# إعداد الشاشة
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zorro Jump Game")

# تحميل صورة الخلفية
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# تحميل صورة اللاعب
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (50, 50))
player_rect = player_image.get_rect()
player_rect.topleft = (100, 300)

# تحميل العقبات
obstacle_images = [
    pygame.transform.scale(pygame.image.load("crate.png"), (50, 50)),
    pygame.transform.scale(pygame.image.load("chest.png"), (50, 50)),
]
obstacle_image = random.choice(obstacle_images)
obstacle_rect = pygame.Rect(800, 300, 50, 50)

# إعداد القفز
is_jumping = False
player_velocity = 0
gravity = 0.8
ground_y = 300

# نقاط
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()
running = True
game_over = False
scored = False

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not is_jumping:
                    is_jumping = True
                    player_velocity = -15

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not is_jumping:
                    is_jumping = True
                    player_velocity = -15

    if not game_over:
        # القفز
        if is_jumping:
            player_rect.y += int(player_velocity)
            player_velocity += gravity
            if player_rect.y >= ground_y:
                player_rect.y = ground_y
                is_jumping = False

        # تحريك العقبة
        obstacle_rect.x -= 6
        if obstacle_rect.right < 0:
            obstacle_rect.left = WIDTH
            obstacle_image = random.choice(obstacle_images)
            scored = False

        # التحقق من تجاوز العقبة
        if not scored and obstacle_rect.right < player_rect.left:
            score += 1
            scored = True

        # تصادم
        if player_rect.colliderect(obstacle_rect):
            game_over = True

    # عرض الأرض
    pygame.draw.rect(screen, (139, 69, 19), (0, 350, WIDTH, 50))

    # عرض اللاعب والعقبة
    screen.blit(player_image, player_rect)
    screen.blit(obstacle_image, obstacle_rect)

    # عرض النقاط
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # عرض رسالة النهاية
    if game_over:
        text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()