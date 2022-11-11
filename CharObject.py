from GameObject import GameObject

class CharObject(GameObject):
    def __init__(self, x, y, speed, sprite, tag):
        super().__init__(x, y, speed, sprite)

        self.last_bullet = 0
        self.bullet_delay = 2000
        self.life = 100

        self.tag = tag
