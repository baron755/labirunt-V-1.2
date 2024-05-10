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
display.set_caption("Лабіринт")
clock = time.Clock()
FPS = 60
background = transform.scale(image.load("background.jpg"), (700, 500))

mixer.init()
jng = mixer_music.load("jungles.ogg")
jng = mixer_music.play()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

font.init()
text1 = font.Font(None, 70)
text2 = font.Font(None, 70)

bty_play = Gamesprite("Button.png", 400, 250, 80, 50, 0)
bty_settings = Gamesprite("Button.png", 460, 320, 80, 50, 0)
bty_exit = Gamesprite("Button.png", 400, 400, 80, 50, 0)

game = True
finich = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0, 0))
    
    bty_play.update()
    bty_play.reset()  
    
    bty_settings.update()
    bty_settings.reset()
    
    bty_exit.update()
    bty_exit.reset()  
    
    text_win = text1.render("Labirunt game",1,(255,0,0))
    win.blit(text_win, (180,50))
    text_play = text2.render("Play",1,(255,0,0))
    win.blit(text_play, (300,250))
    text_settings = text2.render("Settings",1,(255,0,0))
    win.blit(text_settings, (250,320))
    text_exit = text2.render("Exit",1,(255,0,0))
    win.blit(text_exit, (300,400))
    
    if e.type == MOUSEBUTTONDOWN:
        x, y = e.pos
        if bty_play.rect.collidepoint(x, y):
            from maze import *
            
    if e.type == MOUSEBUTTONDOWN:
        x, y = e.pos
        if bty_settings.rect.collidepoint(x, y):
            from settings import *
            
    if e.type == MOUSEBUTTONDOWN:
        x, y = e.pos
        if bty_exit.rect.collidepoint(x, y):
            game = False       
           
    display.update()
    clock.tick(FPS)  
