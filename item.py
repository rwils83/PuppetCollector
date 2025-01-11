class Item:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.durability = 100
        self.usable = True

    def degradation(self):
        if self.durability > 0:
            self.durability = self.durability - 10
        else:
            self.usable = False


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__()
        self.type = "weapon"
        self.name = name
        self.damage = damage


class Armor(Item):
    def __init__(self, name, health_mod):
        super().__init__()
        self.type = "armor"
        self.name = name
        self.health_mod = health_mod


class HealthPotion(Item):
    def __init__(self, name, amount):
        super().__init__()
        self.type = "health"
        self.name = name
        self.amount = amount


class CaptureItems(Item):
    def __init__(self, name, maxCapture):
        super().__init__()
        self.type = "captureTool"
        self.name = name
        self.maxCapture = maxCapture


class Spells(Item):
    def __init__(self, name, damgeMod):
        super().__init__()
        self.type = "spell"
        self.name = name
        self.damageMod = damgeMod
