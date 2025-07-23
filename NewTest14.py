import pygame
from pygame.locals import *

pygame.init()

# Setup window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Mario Clone")

# Colors
WHITE = (255, 255, 255)
PLAYER = (200, 0, 255)
BROWN = (139, 69, 19)

# Clock
clock = pygame.time.Clock()
FPS = 60
max_Velocit_Y = 12
max_Velocit_X = 5
# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill(PLAYER)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HEIGHT - 100
        self.vel_y = 0
        self.jumping = False
        self.vel_x1 = 0.5
        self.vel_x2 = 0.5

    def update(self):
        keys = pygame.key.get_pressed()

        # Gerak kiri/kanan
        if keys[K_a]:
            self.vel_x1 += 0.2
            self.rect.x -= self.vel_x1
            if self.vel_x1 >= 6.9:
                self.vel_x1 = 6.9
        else:
            self.vel_x1 -= 0.15
            self.rect.x -= self.vel_x1
            if self.vel_x1 <= 0:
                self.vel_x1 = 0
        if keys[K_d]:
            if self.vel_x2 >= 7:
                self.vel_x2 = 7
            self.rect.x += self.vel_x2
            self.vel_x2 += 0.2
        else:
            self.vel_x2 -= 0.15
            self.rect.x += self.vel_x2
            if self.vel_x2 <= 0:
                self.vel_x2 = 0

        # Lompat
        if keys[K_SPACE] and not self.jumping:
            self.vel_y = -max_Velocit_Y
            self.jumping = True

        # Gravitasi
        self.vel_y += 0.6
        self.rect.y += self.vel_y

        # Cek tabrakan dengan platform
        hits = pygame.sprite.spritecollide(self, platform_group, False)
        if hits:
            if self.vel_y >= 0:
                self.rect.bottom = hits[0].rect.top
                self.vel_y = 0
                self.jumping = False

        # Game over kalau jatuh ke bawah layar
        if self.rect.top > HEIGHT:
            game_over()
        hits = pygame.sprite.spritecollide(self, coin_group, True)
        global score
        if hits:
            pygame.mixer.Sound('Hit.wav').play()
            score += 1
            if score == 10:
                win_game()

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 215, 0))  # warna emas
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Platform
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Group
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

platform_group = pygame.sprite.Group()
ground = Platform(0, HEIGHT - 20, WIDTH, 20)
platform1 = Platform(0, 475, 250, 15)
platform2 = Platform(300, 400, 100, 15)
platform3 = Platform(500, 325, 100, 15)
platform4 = Platform(700, 250, 100, 15)
platform5 = Platform(300, 175, 150, 15)
platform6 = Platform(100, 75, 100, 15)

for plat in [ground, platform1, platform2, platform3, platform4, platform5, platform6]:
    platform_group.add(plat)

# Font
font = pygame.font.SysFont("Arial", 30)

# Group untuk coin
coin_group = pygame.sprite.Group()

# Tambahkan beberapa coin
coin_positions = [(100, 450), (350, 350), (550, 275), (600, 150), (125, 25), (750, 450), (100, 250), (350, 0), (700, 50), (0, 0)]  # Di atas platform
for pos in coin_positions:
    coin = Coin(*pos)
    coin_group.add(coin)

# Skor
score = 0
font = pygame.font.SysFont("Arial", 30)
signature = font.render('123getu', True, (255,0,255))
def game_over():
    pygame.mixer.music.stop()
    win.fill(WHITE)
    text = font.render("Game Over! Press any key to exit", True, (255, 0, 0))
    win.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                waiting = False
    pygame.quit()
    quit()
def win_game():
    pygame.mixer.music.stop()
    pygame.mixer.Sound('Win.wav').play()
    win.fill(WHITE)
    text = font.render("You Win! Press any key to exit", True, (255, 255, 0))
    win.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                waiting = False
    pygame.quit()
    quit()
pygame.mixer.init()
pygame.mixer.music.load('PlaceholderMusic.mp3')
pygame.mixer.music.play()
# Main loop
running = True
while running:
    clock.tick(FPS)
    win.fill(WHITE)
    win.blit(signature,(700,340))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player_group.update()
    player_group.draw(win)
    platform_group.draw(win)

    coin_group.draw(win)

    # Tampilkan skor
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
