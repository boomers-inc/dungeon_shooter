from GameObject import GameObject


def heal(player):
    value = 10
    if player.life + value > player.max_life:
        player.life = player.max_life
    else:
        player.life += value


def add_damage(player):
    player.gun_damage += 1


class Item(GameObject):
    def __init__(self, x, y, sprite, effect, speed=None):
        super().__init__(x, y, speed, sprite)

        self.effect = effect
