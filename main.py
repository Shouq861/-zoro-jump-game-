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

# إعداد النقاط
score = 0
font = pygame.font.SysFont(None, 36)

# إعداد الساعة
clock = pygame.time.Clock()
running = True
game_over = False
scored = False

def reset_game():
    """إعادة تعيين المتغيرات إلى قيمها الافتراضية"""
    global player_rect, obstacle_rect, is_jumping, player_velocity, score, game_over
    player_rect.topleft = (100, 300)
    obstacle_rect.x = WIDTH
    is_jumping = False
    player_velocity = 0
    score = 0
    game_over = False

while running:
    if game_over:
        # عرض خلفية اللعبة الأصلية
        screen.blit(background, (0, 0))  # الخلفية الأصلية

        # عرض النص "Game Over"
        text = font.render("Game Over", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2 - 90))  # في أعلى الزر

        # عرض زر إعادة اللعبة باللون الأبيض
        restart_button = pygame.Rect(WIDTH // 2 - 80, HEIGHT // 2 - 40, 160, 40)  # زر أصغر
        pygame.draw.rect(screen, (255, 255, 255), restart_button)
        restart_text = font.render("Restart", True, (0, 0, 0))
        screen.blit(restart_text, (WIDTH // 2 - 40, HEIGHT // 2 - 35))

        # عرض عدد النقاط
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (WIDTH // 2 - 45, HEIGHT // 2 + 20))

        pygame.display.flip()

        # التعامل مع الضغط على زر إعادة اللعبة
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    reset_game()  # إعادة تعيين اللعبة
                    break
    else:
        # إذا كانت اللعبة مستمرة
        screen.blit(background, (0, 0))

        # التعامل مع الأحداث
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not is_jumping and not game_over:  # لا يمكن القفز إذا كانت اللعبة انتهت
                    is_jumping = True
                    player_velocity = -15

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not is_jumping and not game_over:  # لا يمكن القفز إذا كانت اللعبة انتهت
                    is_jumping = True
                    player_velocity = -15

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

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()