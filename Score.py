from GameObject import GameObject
from pygame import font

FONT_RETRO_GAMING = 'assets/Retro-Gaming.ttf'


class Score(GameObject):
    def __init__(self, x=0, y=0, speed=..., sprite=..., font_size=20, color=None, value=0):
        super().__init__(x, y, speed, sprite)

        if color is None:
            color = [255, 255, 255]

        font.init()
        self.font = font.Font(FONT_RETRO_GAMING, font_size)
        self.font_size = font_size
        self.color = color
        self.value = value

    def render(self, screen):
        text = self.font.render(f'Score: {str(self.value)}', True, self.color)
        screen.blit(text, [self.x, self.y])
