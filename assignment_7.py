import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the square")

FPS = 60
clock = pygame.time.Clock()

# player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
speed = 300  # pixels per second

running = True
while running:
    dt = clock.tick(FPS) / 1000.0  # seconds elapsed since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= speed * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += speed * dt
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= speed * dt
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += speed * dt

    # keep inside window
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (200, 80, 80), (int(player_x), int(player_y), player_size, player_size))
    pygame.display.flip()

pygame.quit()
sys.exit()