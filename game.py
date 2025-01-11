from world import puppet_town
from player import Player
from combat import Combat
from puppets import Puppet
from item import Weapon, Armor, HealthPotion, CaptureItems


def start_game():
    print("""
One day in Gnomious, a brave soul willing to collect all the 
puppets needed for a proper puppet show went on a mission. The first 
destination: Puppet Town. Can our hero rid the world of anomalies 
and collect puppets for the show? Only time will tell...
""")

    # Create Player
    player_name = input("Enter your name here: \r\n")
    player = Player(name=player_name)
    print(f"Welcome, {player.name}. Your mission begins!")

    # Equip Player
    player.current_weapon = Weapon(name='Pink Dildo', damage=5)
    player.current_armor = Armor(name='Leather Harness and Chaps',
                                 health_mod=2)

    print("You first arrive at Puppet Town. You have researched this town....")
    # Display Puppet Town Intro
    print(f"{puppet_town.description}")
    print(
        "\nPuppet Mayor: Please help us, Puppet Master! Rid our town of "
        "anomalies and restore fun.")

    print(
        f"Armed with {player.current_weapon.name} and "
        f"{player.current_armor.name}, you enter Puppet Town.\n")

    # Initialize First Combat
    print("As you walk through the town, you hear a sound that can only be "
          "described as a bulldozer plowing through the town. "
          "You quickly realize what has happened....")
    first_anomaly = puppet_town.anomalies[0]
    combat_1 = Combat(player, first_anomaly)
    combat_1.combat_loop()

    # Capture Mechanic
    print(
        f"As {first_anomaly.name} falls, you find a Collar and Leash for "
        f"capturing puppets.")
    player.current_cap_tool = CaptureItems(name="Collar and Leash",
                                           maxCapture=1)

    # Capture First Puppet
    squashed = puppet_town.puppets[0]
    print(player.capture_puppet(squashed))
    print(player.equipped_items())

    print("You continue the journey through the town. You hear <some shit to"
          "to represent anomaly 2. I don't know how to write this shit")
    second_anomaly = puppet_town.anomalies[1]
    combat_2 = Combat(player, second_anomaly)
    combat_2.combat_loop()
    print(f"You have slain {second_anomaly.name}. You receive another leash "
          f"and collar. You realize soon you will have another puppet, "
          f"but with that, you will need a place to make sure they are "
          f"safely kept to prevent them from joining the anomaly horde....")
    print("Just then, you see a new puppet. This one immediately catches "
          "your eye. 'I must have this puppet you think to yourself'....")
    shiny = puppet_town.puppets[1]
    print("""
You continue your journey through the town. You stop, and see a shop. Would 
you like to stop in? 
1. Yes
2. No""")
    enter_shop = input("")
    shop = puppet_town.shop
    if enter_shop == "1":
        shop.enter_shop()
        shop.get_items(player=player)
    else:
        print("You continue you journey")
    player.

start_game()
