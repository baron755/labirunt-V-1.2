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
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
            
class Enemy(Gamesprite):
    direction = "left"
    
    def update(self):
        if self.rect.y <= H-500:
            self.direction = "right"
        if self.rect.y >= H-100:
            self.direction = "left"
            
        if self.direction == "left":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
            
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
display.set_caption("Рівень 3")
clock = time.Clock()
FPS = 60
background = transform.scale(image.load("background.jpg"), (700, 500))

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

player = Player("hero.png", W-675, H-350, 50, 50, 3)
enemy_1 = Enemy("cyborg.png", W-435, H-150, 50, 50, 5)
enemy_2 = Enemy("cyborg.png", W-235, H-150, 50, 50, 5)
treasure = Gamesprite("treasure.png", W-675, H-475, 65, 65, 0)

b_wall_1 = Wall((154,205,50), W-700, H-20, 700, 20)
b_wall_2 = Wall((154,205,50), W-700, H-500, 700, 20)
b_wall_3 = Wall((154,205,50), W-20, H-500, 20, 700)
b_wall_4 = Wall((154,205,50), W-700, H-500, 20, 700)

wall_1 = Wall((154,205,50), W-600, H-400, 20, 300)
wall_2 = Wall((154,205,50), W-700, H-400, 100, 20)
wall_3 = Wall((154,205,50), W-600, H-120, 500, 20)
wall_4 = Wall((154,205,50), W-500, H-205, 500, 20)
wall_5 = Wall((154,205,50), W-600, H-300, 500, 20)
wall_6 = Wall((154,205,50), W-120, H-400, 20, 100)
wall_7 = Wall((154,205,50), W-220, H-500, 20, 100)
wall_8 = Wall((154,205,50), W-320, H-400, 20, 100)
wall_9 = Wall((154,205,50), W-420, H-500, 20, 100)

black_wall_1 = Wall((0,0,0), W-700, H-300, 100, 200)
black_wall_2 = Wall((0,0,0), W-500, H-185, 400, 65)
black_wall_3 = Wall((0,0,0), W-500, H-280, 400, 75)

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
    
        treasure.update()
        treasure.reset()
        
        wall_1.draw()
        wall_2.draw()
        wall_3.draw()
        wall_4.draw() 
        wall_5.draw() 
        wall_6.draw() 
        wall_7.draw()
        wall_8.draw() 
        wall_9.draw()  
        
        black_wall_1.draw()
        black_wall_2.draw()
        black_wall_3.draw()
        
        b_wall_1.draw()
        b_wall_2.draw()
        b_wall_3.draw()
        b_wall_4.draw()
        
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
            sprite.collide_rect(player, wall_9)):
            finich = True
            win.blit(text_lose, (200,200))
            kick.play()
            
        if sprite.collide_rect(player, treasure):
            finich = True
            win.blit(text_win, (200,200))
            money.play()
            from maze_4 import *
            
            
             
    else:
        time.delay(3000)
        player.rect.x = W-675
        player.rect.y = H-375
        finich = False
        
    display.update()
    clock.tick(FPS)  