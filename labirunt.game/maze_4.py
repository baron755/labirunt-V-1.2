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
        
class Player(Gamesprite):
    def update(self, ) -> None:
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H-80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < W-80:
            self.rect.x += self.speed
            
class Enemy(Gamesprite):
    direction = "left"
    
    def update(self):
        if self.rect.x <= W-1400:
            self.direction = "right"
        if self.rect.x >= W-200:
            self.direction = "left"
            
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
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
            

W,H = 1000,500
win = display.set_mode((W,H))
display.set_caption("Рівень 4")
clock = time.Clock()
FPS = 60
background = transform.scale(image.load("background.jpg"), (1400, 500))

mixer.init()
mixer_music.load("jungles.ogg")
mixer_music.play()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

font.init()
text1 = font.Font(None, 70)
text_win = text1.render("YOU WIN!",1,(0,200,0))
text_lose = text1.render("YOU LOSE!",1,(200,0,0))

game = True
finich = False

player = Player("hero.png", W-900, H-100, 50, 50, 4)

enemy_1 = Enemy("cyborg.png", W-200, H-200, 150, 150, 6)
enemy_2 = Enemy("cyborg.png", W-1400, H-450, 150, 150, 6)

treasure = Gamesprite("treasure.png", W-100, H-100, 65, 65, 0)

wall_1 = Wall((154,205,50), W-1200, H-250, 20, 500)
wall_2 = Wall((154,205,50), W-1000, H-250, 20, 500)
wall_3 = Wall((154,205,50), W-800, H-250, 20, 500)
wall_4 = Wall((154,205,50), W-600, H-250, 20, 500)
wall_5 = Wall((154,205,50), W-400, H-250, 20, 500)
wall_6 = Wall((154,205,50), W-200, H-250, 20, 500)

wall_7 = Wall((154,205,50), W-1100, H-500, 20, 250)
wall_8 = Wall((154,205,50), W-900, H-500, 20, 250)
wall_10 = Wall((154,205,50), W-500, H-500, 20, 250)
wall_11 = Wall((154,205,50), W-300, H-500, 20, 250)

b_wall_1 = Wall((154,205,50), W-1400, H-20, 1400, 20)
b_wall_2 = Wall((154,205,50), W-1400, H-500, 1400, 20)
b_wall_3 = Wall((154,205,50), W-20, H-500, 20, 700)
b_wall_4 = Wall((154,205,50), W-1400, H-500, 20, 700)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0, 0))

    if not finich:
        player.update()
        player.reset()
    
        enemy_1.update()
        enemy_1.reset()
        
        enemy_2.update()
        enemy_2.reset()
        
        b_wall_1.draw()
        b_wall_2.draw()
        b_wall_3.draw()
        b_wall_4.draw()
        
        wall_1.draw()
        wall_2.draw()
        wall_3.draw()
        wall_4.draw()
        wall_5.draw()
        wall_6.draw()
        
        wall_7.draw()
        wall_8.draw()
        wall_10.draw()
        wall_11.draw()
        
        treasure.update()
        treasure.reset()
        
        if (sprite.collide_rect(player, enemy_1) or  
            sprite.collide_rect(player, enemy_2) or
            sprite.collide_rect(player, b_wall_1) or
            sprite.collide_rect(player, b_wall_2) or
            sprite.collide_rect(player, b_wall_3) or
            sprite.collide_rect(player, b_wall_4) or
            sprite.collide_rect(player, wall_1) or  
            sprite.collide_rect(player, wall_2) or
            sprite.collide_rect(player, wall_3) or
            sprite.collide_rect(player, wall_4) or
            sprite.collide_rect(player, wall_5) or
            sprite.collide_rect(player, wall_6) or
            sprite.collide_rect(player, wall_7) or
            sprite.collide_rect(player, wall_8) or
            sprite.collide_rect(player, wall_10) or
            sprite.collide_rect(player, wall_11)):
            
            finich = True
            win.blit(text_lose, (200,200))
            kick.play()
            
        if sprite.collide_rect(player, treasure):
            finich = True
            win.blit(text_win, (600,200))
            money.play()
            
            from maze_5 import *
         
    else:
        time.delay(3000)
        player.rect.x = W-900
        player.rect.y = H-100
        
        enemy_1.rect.x = W-200
        enemy_1.rect.y = H-200
        
        enemy_2.rect.x = W-1400
        enemy_2.rect.y = H-450
        
        finich = False
        
    display.update()
    clock.tick(FPS)  