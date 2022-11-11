from random import randint
from pygame import draw

from Axis import Axis
from GameObject import GameObject

COLOR_GREEN = (100, 255, 100)
COLOR_RED = (255, 50, 50)
COLOR_YELLOW = (250, 255, 97)


class CharObject(GameObject):
    def __init__(self, x, y, speed, sprite, tag, life=100, gun_damage=20):
        super().__init__(x, y, speed, sprite)

        self.last_bullet = 0
        self.bullet_delay = randint(800, 2000)
        self.life = life
        self.max_life = life
        self.tag = tag
        self.gun_damage = gun_damage

    def render_life_bar(self, screen, align="bottom", color=COLOR_GREEN):

        if self.tag != 0:
            color = COLOR_YELLOW

        size = self.get_sprite_size()
        life_bar_size = Axis(size.x, size.y / 10)

        if align == "bottom":
            pos_y = size.y + self.y + life_bar_size.y * 2

        elif align == "top":
            pos_y = self.y - life_bar_size.y * 2

        health_size = life_bar_size.x * (self.life / self.max_life)
        draw.rect(screen, COLOR_RED,
                  (self.x, pos_y, life_bar_size.x, life_bar_size.y))
        draw.rect(screen, color, (self.x, pos_y, health_size, life_bar_size.y))

    def render(self, screen):
        self.render_life_bar(screen)
        super().render(screen)
