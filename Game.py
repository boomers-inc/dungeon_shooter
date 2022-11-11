from math import atan2, cos, sin
from random import uniform
import pygame

from Axis import Axis
from GameObject import GameObject


class Game:
    def __init__(self):
        super().__init__()
        pygame.display.init()

        monitor = pygame.display.Info()
        self.resolution = Axis(
            x=int(monitor.current_w * 0.9),
            y=int(monitor.current_h * 0.9)
        )
        self.screen = pygame.display.set_mode(size=self.resolution.to_list())

        self.clock = pygame.time.Clock()
        self.frame_time = 0

        self.bg = pygame.transform.smoothscale(pygame.image.load("assets/bg.png").convert_alpha(), (self.resolution.x, self.resolution.y))
        self.door = GameObject(x=self.resolution.x/2, y=0, sprite=pygame.image.load("assets/door.png").convert_alpha(), speed=())

        self.player = GameObject(x=self.resolution.x/2, y=self.resolution.y * 0.8, speed=Axis(8, 6), sprite=pygame.image.load("assets/player.png").convert_alpha())
        self.player_direction = "left"

        self.cursor = GameObject(x=0, y=0, speed=None, sprite=pygame.image.load("assets/cursor.png").convert_alpha())

        self.bullets = []
        self.enemies = []
    
        self.level = 1
        self.spawn_enemies_random()


    def start(self):
        while True:
            self.frame_time = self.clock.tick() / 10
            self.check_events()
            self.player_input()

            self.screen.blit(self.bg, (0, 0))

            for enemy in self.enemies:
                if enemy.x > self.resolution.x * 0.95:
                    enemy.speed.x = -enemy.speed.x

                elif enemy.x < 0:
                    enemy.speed.x = -enemy.speed.x

                if enemy.y > self.resolution.y * 0.85:
                    enemy.speed.y = -enemy.speed.y
                
                elif enemy.y < 0:
                    enemy.speed.y = -enemy.speed.y


                enemy.x += enemy.speed.x * self.frame_time
                enemy.y += enemy.speed.y * self.frame_time
                enemy.render(self.screen)

            for bullet in self.bullets:
                for enemy in self.enemies:
                    if enemy.get_rect().colliderect(bullet.get_rect()):
                        try:
                            self.bullets.remove(bullet)
                            self.enemies.remove(enemy)
                        except:
                            print("error removing item")

                bullet.x += bullet.speed.x * self.frame_time
                bullet.y += bullet.speed.y * self.frame_time
                bullet.render(self.screen)

            self.player.render(self.screen)
            self.cursor.render(self.screen)

            if len(self.enemies) == 0:
                self.door.render(self.screen)
                if self.player.get_rect().colliderect(self.door.get_rect()):
                    self.next_level()

            pygame.display.update()


    def next_level(self):
        self.player.x = self.resolution.x/2
        self.player.y = self.resolution.y * 0.8
        self.level += 1
        self.spawn_enemies_random()


    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.player.y > 0:
                self.player.y -= self.player.speed.y * self.frame_time

        if keys[pygame.K_s]:
            if self.player.y < self.resolution.y * 0.95:
                self.player.y += self.player.speed.y * self.frame_time

        if keys[pygame.K_a]:
            if self.player.x > 0:
                self.player.x -= self.player.speed.x * self.frame_time

        if keys[pygame.K_d]:
            if self.player.x < self.resolution.x * 0.95:
                self.player.x += self.player.speed.x * self.frame_time

        pos = pygame.mouse.get_pos()

        self.cursor.x = pos[0] - self.cursor.sprite.get_rect().centerx
        self.cursor.y = pos[1] - self.cursor.sprite.get_rect().centery
        
        self.update_player_sprite()
        

    def update_player_sprite(self):
        if self.cursor.x < self.player.x and self.player_direction == "right":
            self.player.sprite = pygame.transform.flip(self.player.sprite, True, False)
            self.player_direction = "left"
            
        elif self.cursor.x > self.player.x and self.player_direction == "left":
            self.player.sprite = pygame.transform.flip(self.player.sprite, True, False)
            self.player_direction = "right"


    def get_bullet_speed(self, source_obj, target_obj, speed):
        my = (target_obj.y - source_obj.y)
        mx = (target_obj.x - source_obj.x)
        rad = atan2(my, mx)

        return Axis(speed * cos(rad), speed * sin(rad))


    def spawn_enemies_random(self):
        for i in range(self.level+2):
            self.spawn_enemy()

    def spawn_enemy(self):
        self.enemies.append(
            GameObject(x=self.resolution.x*uniform(0.1, 0.9), y=self.resolution.y * uniform(0, 0.3), speed=Axis(uniform(-8, 8), uniform(-1, 1)), sprite=pygame.image.load("assets/enemy.png").convert_alpha())
        )


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.bullets.append(
                    GameObject(x=self.player.x+self.player.get_rect()[3]/2, y=self.player.y+self.player.get_rect()[3]/2, speed=self.get_bullet_speed(source_obj=self.player, target_obj=self.cursor, speed=30), sprite=pygame.image.load("assets/bullet.png").convert_alpha())
                )