from typing import Any
from pygame import *

class Gamesprite(sprite.Sprite):
    def __init__(self, img, x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))
        
W,H = 700,500
win = display.set_mode((W,H))
display.set_caption("Налаштування")
clock = time.Clock()
FPS = 60
background = transform.scale(image.load("background.jpg"), (700, 500))

mixer.init()
jng = mixer_music.load("jungles.ogg")
jng = mixer_music.play()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

lol = "a_d"

font.init()
text1 = font.Font(None, 70)
text2 = font.Font(None, 70)

bty_play = Gamesprite("Button.png", 400, 250, 80, 50, 0)

game = True
finich = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0, 0))
    
    bty_play.update()
    bty_play.reset()    
    
    text_win = text1.render("Making...",1,(255,0,0))
    win.blit(text_win, (180,50))
               
    display.update()
    clock.tick(FPS)  
