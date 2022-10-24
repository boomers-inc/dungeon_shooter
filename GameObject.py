from pygame import Rect

class GameObject:
    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = sprite.convert_alpha()

    def get_rect(self):
        size = self.sprite.get_size()
        return Rect(self.x, self.y, size[0], size[1])

    def render(self, screen):
        screen.blit(self.sprite, [self.x, self.y])
