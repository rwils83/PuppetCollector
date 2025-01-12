from world import puppet_town, stranger_things, upside_down
from player import Player
from combat import Combat
from puppets import Puppet
from item import Weapon, Armor, HealthPotion, CaptureItems


class Game:
    def __init__(self):
        self.player = None

    def start_game(self):
        self.introduce_game()
        self.create_player()
        self.equip_player()
        self.explore_town(puppet_town)
        self.explore_town(stranger_things)
        self.explore_town(upside_down)

    def introduce_game(self):
        print("""
One day in Gnomious, a brave soul willing to collect all the 
puppets needed for a proper puppet show went on a mission. The first 
destination: Puppet Town. Can our hero rid the world of anomalies 
and collect puppets for the show? Only time will tell...
""")

    def create_player(self):
        player_name = input("Enter your name here: \r\n")
        self.player = Player(name=player_name)
        print(f"Welcome, {self.player.name}. Your mission begins!")

    def equip_player(self):
        self.player.current_weapon = Weapon(name='Pink Dildo', damage=5)
        self.player.current_armor = Armor(name='Leather Harness and Chaps',
                                          health_mod=2)
        print(f"Armed with {self.player.current_weapon.name} and "
              f"{self.player.current_armor.name}, you enter Puppet Town.\n")

    def start_combat(self, anomaly):
        print(
            f"You hear a strange sound and realize an anomaly is approaching: {anomaly.name}!")
        combat = Combat(self.player, anomaly)
        combat.combat_loop()
        print(f"You have defeated {anomaly.name}!")

    def capture_puppet(self, puppet, item_name="Collar and Leash"):
        print(
            f"As you explore, you find a {item_name} and spot {puppet.name}.")
        self.player.current_cap_tool = CaptureItems(name=item_name,
                                                    maxCapture=1)
        print(self.player.capture_puppet(puppet))

    def explore_town(self, town):
        # Intro Narrative
        print(f"{town.description}")
        print(
            "Puppet Mayor: Please help us, Puppet Master! Rid our town of "
            "anomalies and restore fun.\n")

        # Combat and Puppet Captures
        self.start_combat(town.anomalies[0])
        self.capture_puppet(town.puppets[0])

        self.start_combat(town.anomalies[1])
        self.capture_puppet(town.puppets[1])

        # Shop Interaction
        self.visit_shop(town)

        # Final Combat and Puppet Capture
        self.start_combat(town.anomalies[2])
        self.capture_puppet(town.puppets[2])

    def visit_shop(self, town):
        print("You encounter a shop. Would you like to enter?")
        enter_shop = self.get_input(["1. Yes", "2. No"], [1, 2])

        if enter_shop == 1:
            shop = town.shop
            shop.enter_shop()
            shop.get_items(player=self.player)
            print(f"You receive {shop.items[0].name}, {shop.items[1].name}.")
            add_health = self.get_input(
                "Would you like to use your health potion?", [1, 2])
            if add_health == 1:
                self.player.take_health_potion()
        else:
            print("You decide to continue your journey.")

    def get_input(self, prompt, valid_choices):
        """Helper method for input validation."""
        while True:
            print("\n".join(prompt if isinstance(prompt, list) else [prompt]))
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice in valid_choices:
                    return choice
            except ValueError:
                pass
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    game = Game()
    game.start_game()
