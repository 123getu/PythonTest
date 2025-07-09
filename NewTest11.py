import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tebak Gambar")
font = pygame.font.Font(None, 48)
clock = pygame.time.Clock()
signature = font.render('123getu', True, (100,0,100))
# Data gambar dan jawaban
questions = [
    {"image": "apple.jpg", "answer": "apple"},
    {"image": "cat.jpg", "answer": "cat"},
    {"image": "bunny.jpg", "answer": "bunny"},
    {"image": "grape.jpg", "answer": "grape"},
    {"image": "screwdriver.jpg", "answer": "screwdriver"},
    {"image": "ladder.jpg", "answer": "ladder"},
    {"image": "microwave.jpg", "answer": "microwave"},
    {"image": "elephant.jpg", "answer": "elephant"},
    {"image": "komodo dragon.jpg", "answer": "komodo dragon"},
    {"image": "jade.jpg", "answer": "jade"},
]

current_question = 0
user_input = ""
score = 0
feedback = ""
pygame.mixer.init()
pygame.mixer.music.load('PlaceholderMusic.mp3')
pygame.mixer.music.play()
def render_text(text, y, color=(255, 255, 255)):
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (50, y))

def load_image(path):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (300, 300))

running = True
while running:
    screen.fill((0, 0, 50))
    screen.blit(signature, (650,550))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN: #makes us can write something on the screen
            if event.key == pygame.K_RETURN:
                correct_answer = questions[current_question]["answer"]
                if user_input.lower() == correct_answer:
                    feedback = "Benar!"
                    score += 1
                else:
                    feedback = f"Salah! Jawaban: {correct_answer}"
                user_input = ""
                current_question += 1
                if current_question >= len(questions):
                    running = False
            elif event.key == pygame.K_BACKSPACE: #deleting word that we have written
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    if current_question < len(questions):
        img_path = questions[current_question]["image"]
        img = load_image(img_path)
        screen.blit(img, (250, 50))
        
        render_text("Jawabanmu: " + user_input, 400)
        render_text(feedback, 460)
        render_text(f"Skor: {score}"+'/5', 520)

    pygame.display.flip()
    clock.tick(30)

# Setelah selesai
screen.fill((0, 0, 0))
pygame.mixer.music.stop()
if score >= 7:
    render_text(f"You Win! Your Final Score: {score}"+'/10', 250, (0, 255, 0))
    pygame.display.flip()
    pygame.time.wait(3000)
else:
    render_text(f"You Lost. Your Final Score: {score}"+'/10', 250, (255, 0, 0))
    pygame.display.flip()
    pygame.time.wait(3000)


pygame.quit()
sys.exit()
