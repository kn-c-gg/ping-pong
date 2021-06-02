
'''1. Библиотеки'''
from pygame import *
from random import randint

'''2. Классы'''
#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса - инициализация свойств
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        # подключение конструктора родительского класса
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()

        # координаты и скорость перемещения
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    
    #метод для отрисовки спрайта
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if (keys[K_LEFT] or keys[K_a]) and self.rect.x > 5:
            self.rect.x -= self.speed
        if (keys[K_RIGHT] or keys[K_d]) and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, -15, 15, 20)
        bullets.add(bullet)
        fire_sound.play()

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            lost += 1
            lost_sound.play()
            self.rect.y = 0
            self.rect.x = randint(0, win_width-80)

'''3. Объекты и переменные'''
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("ping pong")

font.init()
font1 = font.SysFont("Arial", 36)

lost = 0
score = 0

win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

#Персонажи игры:

#Игровые переменные:
game = True
finish = False
clock = time.Clock()
FPS = 30

'''4. Игровой цикл'''
while game:
    # Обработка событий
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:

        # Составление кадра от фона до спрайтоы
        window.fill((50, 100, 200))

    display.update()
    clock.tick(FPS)
