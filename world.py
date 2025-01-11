from enemy import Anomaly
from puppets import Puppet
from item import Weapon, Armor, CaptureItems, HealthPotion, Spells


class Location:
    def __init__(self, name, description, anomalies=None, puppets=None,
                 shop=None):
        self.name = name
        self.description = description
        self.anomalies = anomalies or []
        self.puppets = puppets or []
        self.shop = shop


class Shop:
    def __init__(self, name, items, free=False):
        self.name = name
        self.items = items
        self.free = free

    def enter_shop(self):
        items_list = '\n'.join(item.name for item in self.items)
        if self.free:
            print(f"You enter {self.name}")
            print(f"{self.name} has the following items for sale: \r\n"
                  f"{items_list}")

    def get_items(self, player):
        item_buy = input("Would you like to get the items?\r\n1. Yes\r\n2. "
                         "No\r\n")
        if item_buy == "1":
            player.pick_up_item(self.items[0])
            player.pick_up_item(self.items[1])


puppet_town_shop = Shop(
    name="Blame It on the Tonic",
    items=[
        HealthPotion(name="Puppet Town Health Potion", amount="100"),
        Spells(name="Medicinal Spell", damgeMod="20")
    ],
    free=True
)

puppet_town = Location(
    name="Puppet Town",
    description=(
        "A lively town filled with puppets. Recently, anomalies have "
        "caused chaos, and only the Puppet Master can save the day."
    ),
    anomalies=[
        Anomaly(name='Grumpy Puppet', damage=3, stats={
            "Skills": [
                "Punches inanimate objects",
                "Accuses video games of being rigged",
                "Entrapment"
            ],
            "Weaknesses": [
                "Medicinal Spells",
                "Illogical Epiphanies",
                "Chair damage increased by 2"
            ]
        }),
        Anomaly(name="The Next Anomaly", damage=4, stats={
            "Skills": [
                "Skill 1",
                "Skill 2",
                "Skill 3",
            ],
            "Weaknesses": [
                "Weakness 1",
                "Weakness 2",
                "Weakness 3"
            ]
        }),
        Anomaly(name="Final Anomaly", damage=5, stats={
            "Skills": [
                "Skill 1",
                "Skill 2",
                "Skill 3"
            ],
            "Weaknesses": [
                "Weakness 1",
                "Weakness 2",
                "Weakness 3"
            ]
        })
    ],
    puppets=[
        Puppet(name="Squashed", abilities={
            "Endurance": "Low",
            "Knowledge": "Low",
            "Special Skill": ""
        }
               ),
        Puppet(name="Shiny", abilities={
            "Endurance": "Medium",
            "Knowledge": "Medium",
            "Special Skill": "TBD"
        })
    ],
    shop=puppet_town_shop
)
