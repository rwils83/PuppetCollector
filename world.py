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
        HealthPotion(name="Puppet Town Health Potion", amount=100),
        Spells(name="Medicinal Spell", damgeMod=20)
    ],
    free=True
)
stranger_things_shop = Shop(
    name="Scoops Slinging Delight",
    items=[
        HealthPotion(name="Banana Split you open", amount=100),
        Spells(name="Crushed Nuts", damgeMod=20)

    ],
    free=True
)
upside_down_shop = Shop(
    name="",
    items=[

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
        Anomaly(
            name='Squashed',
            damage=3,
            stats={
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
            }
        ),
        Anomaly(
            name="Suckubus",
            damage=4,
            stats={
                "Skills": [
                    "Flirts with everyone, even in battle",
                    "Pretends to tamper with enemy plans but gets lazy",
                    "Says mean things that upset everyone, including her "
                    "allies",
            ],
                "Weaknesses":[
                    "Thinks everyone loves her, gets hit harder when they "
                    "don’t",
                    "Falls for any compliment, easily tricked",
                    "Her mean spirit makes allies slow to help her"
                ]
            }
        ),
        Anomaly(
            name="Darkfeather",
            damage=5,
            stats={
                "Skills": [
                    "Touts vague qualifications and overstates alliances",
                    "Keeps a close watch on her top 5, gets upset if ranks "
                    "change",
                    "Perceives shadows following her, grows paranoid"
                ],
                "Weaknesses": [
                    "Demands exclusivity, alienating herself",
                    "Gossip backfires, causing chaos in her ranks",
                    "Feels the sting of imagined frost"
                ]
            }
        )
    ],
    puppets=[
        Puppet(
            name="Shiny",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        ),
        Puppet(
            name="Jester",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        ),
        Puppet(
            name="Highmark",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        )
    ],
    shop=puppet_town_shop
)

stranger_things = Location(
    name="Stranger Things",
    description="",
    anomalies=[
        Anomaly(
            name="",
            damage=5,
            stats={
                "Skills":[],
                "Weaknesses":[]
            }
        ),
        Anomaly(
            name="",
            damage=7, stats={
                "Skills":[],
                "Weaknesses":[]
            }
        ),
        Anomaly(
            name="",
            damage=8, stats={
                "Skills":[],
                "Weaknesses":[]
            }
        )
    ],
    puppets=[
        Puppet(
            name="Temu Steve",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        ),
        Puppet(
            name="Zesty",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        ),
        Puppet(
            name="place_holder",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        )
    ],
    shop=stranger_things_shop
)

upside_down = Location(
    name="The Upside Down",
    description="",
    anomalies=[
        Anomaly(
            name="",
            damage=5, stats={
                "Skills": [],
                "Weaknesses":[]
            }
        ),
        Anomaly(
            name="",
            damage=7, stats={
                "Skills": [],
                "Weaknesses":[]
            }
        ),
        Anomaly(
            name="",
            damage=8, stats={
                "Skills": [],
                "Weaknesses":[]
            }
        )
    ],
    puppets=[
        Puppet(
            name="",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        ),
        Puppet(
            name="",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        ),
        Puppet(
            name="",
            abilities={
                "Endurance": "",
                "Knowledge": "",
                "Special Skill": ""
            }
        )
    ],
    shop=upside_down_shop
)