import pygame
import random
import time

# Inisialisasi
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Target!")

# Warna
WHITE = (100, 0, 0)
RED = (255, 0, 0)
FAKE = (225, 0, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 36)

# Lingkaran Target
target_radius = 30
target_x = random.randint(target_radius, WIDTH - target_radius)
target_y = random.randint(target_radius, HEIGHT - target_radius)
decoy_radius = 30
decoy_x =random.randint(decoy_radius, WIDTH - decoy_radius)
decoy_y =random.randint(decoy_radius, HEIGHT - decoy_radius)

# Skor & Timer
frame = 0
score = 0
start_time = time.time()
game_duration = 10  # detik
# Game loop
running = True
pygame.mixer.init()
pygame.mixer.music.load('PlaceholderMusic.mp3')
pygame.mixer.music.play()
while running:
    screen.fill(WHITE)

    elapsed_time = time.time() - start_time
    remaining_time = max(0, int(game_duration - elapsed_time))
    frame += 1
    # Gambar target
    pygame.draw.circle(screen, RED, (target_x, target_y), target_radius)
    pygame.draw.circle(screen, FAKE, (decoy_x, decoy_y), decoy_radius)
    # Gambar skor dan waktu
    score_text = font.render(f"Skor: {score}", True, BLACK)
    time_text = font.render(f"Waktu: {remaining_time}", True, BLACK)
    signature = font.render(f"123getu", True, (255,0,255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))
    screen.blit(signature, (450, 300))
    pygame.display.flip()
    if frame == 5000:
        target_x = random.randint(target_radius, WIDTH - target_radius)
        target_y = random.randint(target_radius, HEIGHT - target_radius)
        decoy_x =random.randint(decoy_radius, WIDTH - decoy_radius)
        decoy_y =random.randint(decoy_radius, HEIGHT - decoy_radius)
        frame = 0
    if remaining_time <= 0:
        running = False
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            dist = ((mx - target_x)**2 + (my - target_y)**2)**0.5
            dist2 = ((mx - decoy_x)**2 + (my - decoy_y)**2)**0.5
            if dist <= target_radius:
                score += 1
                pygame.mixer.Sound('Win.wav').play()
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)
                decoy_x =random.randint(decoy_radius, WIDTH - decoy_radius)
                decoy_y =random.randint(decoy_radius, HEIGHT - decoy_radius)
            elif dist2 <= decoy_radius:
                if score > 0:
                    score -= 1
                pygame.mixer.Sound('Hit.wav').play()
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)
                decoy_x =random.randint(decoy_radius, WIDTH - decoy_radius)
                decoy_y =random.randint(decoy_radius, HEIGHT - decoy_radius)
# Game selesai
screen.fill(WHITE)
end_text = font.render(f"Game Over! Skor Akhir: {score}", True, BLACK)
test = font.render(f"frame: {frame}", True, BLACK)
screen.blit(end_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
pygame.mixer.music.stop()
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
