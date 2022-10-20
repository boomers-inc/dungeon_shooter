class GameObject:
    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = sprite.convert_alpha()

    def render(self, screen):
        screen.blit(self.sprite, [self.x, self.y])
