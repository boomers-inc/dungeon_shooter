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

        self.player = GameObject(x=self.resolution.x/2, y=self.resolution.y * 0.8, speed=Axis(8, 6), sprite=pygame.image.load("assets/player.png"))
        self.player_direction = "left"

        self.cursor = GameObject(x=0, y=0, speed=None, sprite=pygame.image.load("assets/cursor.png"))

        self.bullets = []
        self.enemies = []

        self.spawn_enemy()

    def start(self):
        while True:
            self.frame_time = self.clock.tick() / 10
            self.exec_events()
            self.player_input()

            self.screen.fill((30, 30, 30))
            self.player.render(self.screen)
            self.cursor.render(self.screen)

            for enemy in self.enemies:
                enemy.render(self.screen)

            for bullet in self.bullets:
                for enemy in self.enemies:
                    if enemy.get_rect().colliderect(bullet.get_rect()):
                        self.bullets.remove(bullet)
                        self.enemies.remove(enemy)

                bullet.x += bullet.speed.x * self.frame_time
                bullet.y += bullet.speed.y * self.frame_time
                bullet.render(self.screen)

            pygame.display.update()

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player.y -= self.player.speed.y * self.frame_time

        if keys[pygame.K_s]:
            self.player.y += self.player.speed.y * self.frame_time

        if keys[pygame.K_a]:
            self.player.x -= self.player.speed.x * self.frame_time

        if keys[pygame.K_d]:
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

            
    def get_bullet_speed(self):
        x = (self.cursor.x - self.player.x)/25
        y = (self.cursor.y - self.player.y)/25

        return Axis(x, y)

    def spawn_enemy(self):
        self.enemies.append(
            GameObject(x=self.resolution.x*uniform(0.1, 0.9), y=self.resolution.y * uniform(0, 0.3), speed=Axis(8, 6), sprite=pygame.image.load("assets/enemy.png"))
        )


    def exec_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.bullets.append(
                    GameObject(x=self.player.x, y=self.player.y, speed=self.get_bullet_speed(), sprite=pygame.image.load("assets/bullet.png"))
                )
    