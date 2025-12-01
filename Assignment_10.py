import pygame, math, sys, random

pygame.init()

screenW, screenH = 900, 700
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Catacomb Escape: Stealth Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (220, 0, 0)
GREEN = (0, 200, 0)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 0)
GRAY = (40, 40, 40)
BLACK = (0, 0, 0)
ORANGE = (255, 150, 0)

player = pygame.Rect(80, 600, 40, 40)
player_speed = 4

goal = pygame.Rect(820, 100, 40, 40)


class Guard:
    def __init__(self, x, y, path, speed=2):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.path = path
        self.path_index = 0
        self.base_speed = speed
        self.speed = speed
        self.target_speed = speed
        self.direction = pygame.Vector2(1, 0)
        self.pause_timer = 0
        self.scan_angle = 0
        self.chasing = False
        self.chase_cooldown = 0
        self.color = RED

    def move(self, player_rect):

        if self.speed < self.target_speed:
            self.speed += 0.05
        elif self.speed > self.target_speed:
            self.speed -= 0.05


        if self.chasing:
            self.direction = pygame.Vector2(player_rect.center) - pygame.Vector2(self.rect.center)
            if self.direction.length() != 0:
                self.direction = self.direction.normalize()
            self.rect.center += self.direction * self.speed


            self.chase_cooldown -= 1
            if self.chase_cooldown <= 0:
                self.chasing = False
                self.target_speed = self.base_speed
                self.color = RED
            return


        if self.pause_timer > 0:
            self.pause_timer -= 1

            self.scan_angle += 0.03
            self.direction = pygame.Vector2(math.cos(self.scan_angle), math.sin(self.scan_angle))
            return

        target = pygame.Vector2(self.path[self.path_index])
        pos = pygame.Vector2(self.rect.center)
        to_target = target - pos
        if to_target.length() < 4:

            self.path_index = (self.path_index + 1) % len(self.path)
            self.pause_timer = random.randint(60, 120)
        else:
            self.direction = to_target.normalize()
            self.rect.center += self.direction * self.speed

    def draw_vision(self):
        cone_length = 200
        angle = math.atan2(self.direction.y, self.direction.x)
        points = [self.rect.center]
        for offset in [-0.5, 0.5]:
            dx = math.cos(angle + offset) * cone_length
            dy = math.sin(angle + offset) * cone_length
            points.append((self.rect.centerx + dx, self.rect.centery + dy))
        pygame.draw.polygon(screen, (255, 255, 100, 40), points)
        pygame.draw.rect(screen, self.color, self.rect)

    def sees_player(self, player_rect):
        cone_length = 200
        vec_to_player = pygame.Vector2(player_rect.center) - pygame.Vector2(self.rect.center)
        distance = vec_to_player.length()
        if distance < cone_length:
            vec_to_player.normalize_ip()
            dot = self.direction.dot(vec_to_player)
            if dot > math.cos(math.radians(45)):
                return True
        return False

    def alert(self):
        self.chasing = True
        self.chase_cooldown = 180  
        self.target_speed = self.base_speed * 1.6  
        self.color = ORANGE

guards = [
    Guard(300, 250, [(300, 250), (600, 250), (600, 400), (300, 400)], 2),
    Guard(200, 550, [(200, 550), (600, 550), (600, 650), (200, 650)], 2),
    Guard(700, 300, [(700, 300), (800, 300), (800, 500), (700, 500)], 1.8),
]

font = pygame.font.SysFont(None, 40)
win = False
lose = False
running = True

while running:
    dt = clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not win and not lose:
        dx = dy = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -player_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = player_speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = player_speed

        player.x += dx
        player.y += dy
        player.x = max(0, min(player.x, screenW - player.width))
        player.y = max(0, min(player.y, screenH - player.height))

        for guard in guards:
            if not guard.chasing and guard.sees_player(player):
                guard.alert()

            guard.move(player)

            if player.colliderect(guard.rect):
                lose = True

        if player.colliderect(goal):
            win = True

    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, goal)
    pygame.draw.rect(screen, BLUE, player)

    for guard in guards:
        guard.draw_vision()

    if win:
        text = font.render("You reached the exit!", True, WHITE)
        screen.blit(text, (240, 300))
    elif lose:
        text = font.render("Caught by the Roman patrols!", True, RED)
        screen.blit(text, (230, 300))

    pygame.display.flip()
