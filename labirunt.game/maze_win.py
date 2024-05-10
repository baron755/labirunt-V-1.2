from typing import Any
from pygame import *   


lol = "a_d"

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
        
class Player(Gamesprite):
    def update(self, ) -> None:
        keys = key.get_pressed()
        if lol == "a_d":
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < H-80:
                self.rect.y += self.speed
            if keys[K_a] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_d] and self.rect.x < W-80:
                self.rect.x += self.speed
        elif lol == "up_down":
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < H-80:
                self.rect.y += self.speed
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < W-80:
                self.rect.x += self.speed
            
class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_w, wall_h):
        self.color = color
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
            

W,H = 700,500
win = display.set_mode((W,H))
display.set_caption("Ти виграв!")
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
text_win = text1.render("YOU WIN!",1,(0,200,0))
text_lose = text1.render("YOU LOSE!",1,(200,0,0))

game = True
finich = False

player = Player("hero.png", W-375, H-400, 50, 50, 4)
treasure_1 = Gamesprite("treasure.png", W-200, H-400, 100, 100, 0)
treasure_2 = Gamesprite("treasure.png", W-600, H-400, 100, 100, 0)
treasure_3 = Gamesprite("treasure.png", W-200, H-200, 100, 100, 0)
treasure_4 = Gamesprite("treasure.png", W-600, H-200, 100, 100, 0)
treasure_final = Gamesprite("treasure.png", W-435, H-200, 200, 200, 0)

screen = 'menu'
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0, 0))

    if not finich:
        player.update()
        player.reset()
    
        treasure_1.update()
        treasure_1.reset()
        
        treasure_2.update()
        treasure_2.reset()
        
        treasure_3.update()
        treasure_3.reset()
        
        treasure_4.update()
        treasure_4.reset()
        
        treasure_final.update()
        treasure_final.reset()
            
        if sprite.collide_rect(player, treasure_final):
            finich = True
            win.blit(text_win, (200,200))
            money.play()
            time.delay(3000)
            from menu import *
            
    else:
        time.delay(3000)
        player.rect.x = W-625
        player.rect.y = H-450
        finich = False
        
    display.update()
    clock.tick(FPS)  