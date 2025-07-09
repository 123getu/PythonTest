from pygame import *

#parent class for sprites 
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("RockBackround.png"), (win_width, win_height))
#Game characters:
packman = GameSprite('PlayerPlaceholder.png', 5, win_height - 80, 4)
monster = GameSprite('Enemy1Placeholder.png', win_width - 80, 280, 2)
final = GameSprite('Placeholder.png', win_width - 120, win_height - 80, 0)
speed = 10
game = True
clock = time.Clock()
FPS = 60

#music
mixer.init()
mixer.music.load('PlaceholderMusic.mp3') #simple-hiphop-beat-20231218-182036 Music by <a href="https://pixabay.com/id/users/genxbeats-20046096/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=182036">Genx Beats</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=182036">Pixabay</a>
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    packman.reset()
    monster.reset()

    display.update()
    clock.tick(FPS)
