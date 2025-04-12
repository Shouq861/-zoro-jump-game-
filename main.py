import pygame
import sys

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

# إعداد القفز
is_jumping = False
player_velocity = 0
gravity = 0.8
ground_y = 300

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(background, (0, 0))
    screen.blit(player_image, player_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not is_jumping:
                is_jumping = True
                player_velocity = -15

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_jumping:
                is_jumping = True
                player_velocity = -15

    if is_jumping:
        player_rect.y += int(player_velocity)
        player_velocity += gravity
        if player_rect.y >= ground_y:
            player_rect.y = ground_y
            is_jumping = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()