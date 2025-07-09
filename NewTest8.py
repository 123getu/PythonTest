from pygame import *

#parent class for sprites 
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed, move_set, radius1, radius2):
        super().__init__()
 
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.move_set = move_set
        self.radius1 = radius1
        self.radius2 = radius2
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#heir class for the player sprite (controlled by arrows)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
#heir class for the enemy sprite (moves by itself)
class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.move_set == 'horizontal':
            if self.rect.x <= self.radius1:
                self.side = "right"
            if self.rect.x >= win_width - self.radius2:
                self.side = "left"
            if self.side == "left":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
        elif self.move_set == 'vertical':
            if self.rect.y <= self.radius1:
                self.side = "right"
            if self.rect.y >= win_height - self.radius2:
                self.side = "left"
            if self.side == "left":
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
#class for obstacle sprites
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        #wall image – a rectangle of the required size and color
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
 
        #every sprite must store the rect – rectangular property
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

#Game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background1Placeholder.png"), (win_width, win_height))

#Game characters:
packman = Player('PlayerPlaceholder.png', 5, win_height - 80, 4, 'n/a', 0, 0)
monster1 = Enemy('Enemy1Placeholder.png', win_width - 80, 280, 20, 'horizontal', 0, 85)
monster2 = Enemy('Enemy2Placeholder.png', win_height - 0, 100, 25, 'vertical', 0, 85)
final = GameSprite('Placeholder.png', win_width - 120, win_height - 80, 0, 'n/a', 0, 0)
w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

#music
mixer.init()
mixer.music.load('PlaceholderMusic.mp3')
mixer.music.play(loops=99999)
money = mixer.Sound('Win.wav')
kick = mixer.Sound('Hit.wav')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        packman.update()
        monster1.update()
        monster2.update()
        
        packman.reset()
        monster1.reset()
        monster2.reset()
        final.reset() 

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        #Lost game
        if sprite.collide_rect(packman, monster1) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) or sprite.collide_rect(packman, monster2):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
            mixer_music.stop()

        #Won game
        if sprite.collide_rect(packman, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
            mixer_music.stop()

    display.update()
    clock.tick(FPS)
