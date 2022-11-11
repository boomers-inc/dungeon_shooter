from GameObject import GameObject


class Bullet(GameObject):
    def __init__(self, x, y, speed, sprite, tag, damage=20, ):
        super().__init__(x, y, speed, sprite)

        self.tag = tag
        self.damage = damage
