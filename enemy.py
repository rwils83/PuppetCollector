class Enemy:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.damage = 10


# We need to come up with some enemy types and attributes

class Anomaly(Enemy):
    def __init__(self, name, damage, stats):
        super().__init__()
        self.name = name
        self.damage = damage
        self.ability = ""
        self.stats = stats
