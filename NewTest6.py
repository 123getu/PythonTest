from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption("catch")
random = randint(1,3)
if random == 1:  
    background = transform.scale(image.load("Background1Placeholder.png"), (700, 500))
elif random == 2:
    background = transform.scale(image.load("Background2Placeholder.png"), (700, 500))
else:
    background = transform.scale(image.load("Background3Placeholder.png"), (700, 500))


#parameters of the image sprite
x1 = 100
y1 = 300

x2 = 300
y2 = 300

x3 = 300
y3 = 100

x4 = 100
y4 = 100

sprite1 = transform.scale(image.load('Enemy1Placeholder.png'), (100, 100))
sprite2 = transform.scale(image.load('Enemy2Placeholder.png'), (100, 100))
sprite3 = transform.scale(image.load('Enemy3Placeholder.png'), (100, 100))
sprite4 = transform.scale(image.load('PlayerPlaceholder.png'), (100, 100))
speed = 10
#game loop
run = True
clock = time.Clock()
FPS = 60
step = 0
step2 = 0
tick = 0
direction1 = 1
direction2 = 1
#music
mixer.init()
mixer.music.load('PlaceholderMusic.mp3') #simple-hiphop-beat-20231218-182036 Music by <a href="https://pixabay.com/id/users/genxbeats-20046096/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=182036">Genx Beats</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=182036">Pixabay</a>
mixer.music.play()
while run:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    window.blit(sprite3, (x3, y3))
    window.blit(sprite4, (x4, y4))

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
        step += speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
        step += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
        step += speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
        step += speed

    if keys_pressed[K_a] and x4 > 5:
        x4 -= speed
        step2 += speed
    if keys_pressed[K_d] and x4 < 595:
        x4 += speed
        step2 += speed
    if keys_pressed[K_w] and y4 > 5:
        y4 -= speed
        step2 += speed
    if keys_pressed[K_s] and y4 < 395:
        y4 += speed
        step2 += speed
    
    if x2 == 0:
        direction1 = 1
        direction2 = 1
    if x2 == 500:
        direction1 = -1
        direction2 = 1
    if y2 == 0:
        direction1 = 1
        direction2 = 1
    if y2 == 400:
        direction1 = 1
        direction2 = -1
    x2 += speed*direction1/2
    y2 += speed*direction2/2

    if y3 > 5:
        x3 -= speed/2
        y3 += speed
    if y3 < 595:
        x3 += speed/2
        y3 -= speed
    if x3 > 5:
        x3 += speed/2
        y3 -= speed
    if x3 < 395:
        x3 -= speed/2
        y3 += speed

    if tick == 60:
        print('steps:',step,'\nSteps2:', step2)
        tick = 0
    else:
        tick += 1
    display.update()
    clock.tick(FPS)
    
