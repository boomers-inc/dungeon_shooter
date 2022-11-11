from GameObject import GameObject

class Bullet(GameObject):
    def __init__(self, x, y, speed, sprite):
        super().__init__(x, y, speed, sprite)
        
        self.tag = 0