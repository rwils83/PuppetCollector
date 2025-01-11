class Player:
    """Represents the player character, much more to come"""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.current_weapon = None
        self.current_armor = None
        self.inventory = {
            "weapons": [],
            "health": [],
            "armor": [],
            "spells": []
        }
        self.damage_base = 5
        self.equipped = ""
        self.current_cap_tool = ""
        self.puppets = []

    def damage_modifier(self):
        return self.current_weapon.damage + self.damage_base

    def armor_modifier(self):
        return self.current_armor.health_mod + self.health

    def pick_up_item(self, item):
        if item.type == "weapon":  # This will get changed back once we
            self.inventory['weapons'].append(item)
        elif item.type == "health":
            self.inventory['health'].append(item)
        elif item.type == "armor":
            self.inventory['armor'].append(item)
        elif item.type == "spell":
            self.inventory['spells'].append(item)
        else:
            print("Wtf are you doing Ryan")

    def equip_item(self, item):
        if item.type == "weapon":
            if item in self.inventory['weapons']:
                self.inventory['weapons'].append(self.current_weapon)
                self.inventory['weapons'].remove(item)
                self.current_weapon = item
        elif item.type == "armor":
            if item in self.inventory['armor']:
                self.inventory['armor'].append(self.current_armor)
                self.inventory['armor'].remove(item)
                self.current_armor = item
        else:
            print("Wtf are you doing Ryan")

    def equipped_items(self):
        if len(self.puppets) == 0:
            self.equipped = f"""
Your current Equipped items: 
    Weapon: {self.current_weapon.name}
    Armor: {self.current_armor.name}
    Capture Device: {self.current_cap_tool.name}
    
You current stats: 
    Health: {self.health}
    Armor modifier: {self.armor_modifier()}
    Damage dealt: {self.damage_modifier()}
"""
        else:
            self.equipped = f"""
Your current Equipped items: 
    Weapon: {self.current_weapon.name}
    Armor: {self.current_armor.name}
    Capture Device: {self.current_cap_tool.name}
    
You current stats: 
    Health: {self.health}
    Armor modifier: {self.armor_modifier()}
    Damage dealt: {self.damage_modifier()}
    Puppets: {', '.join(puppet.name for puppet in self.puppets)}"""
        return self.equipped

    def capture_puppet(self, puppet):
        self.puppets.append(puppet)
        input(
            f"You have added {puppet.name} to the puppet show. Enjoy your new puppet, Puppet Master!")

        # Allow the player to play with puppets after capturing one
        while True:
            choice = input(
                "Would you like to play with a puppet? (yes/no): ").strip().lower()
            if choice == "yes":
                self.puppet_play()
            elif choice == "no":
                print("Continuing your journey...")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def show_inventory(self):
        spells = '\r\n\t'.join(
            spell.name for spell in self.inventory['spells'])
        healthpotions = '\r\n\t'.join(potion.name for potion in self.inventory[
            'health'])
        weapons = '\r\n\t'.join(weapon.name for weapon in self.inventory[
            'weapons'])
        armor = '\r\n\t'.join(armor.name for armor in self.inventory['armor'])
        print(f"""
Spells:
    {spells}
Armor: 
    {armor}
Weapons: 
    {weapons}
Health: 
    {healthpotions}
""")

    def take_health_potion(self):
        potion = self.inventory['health'][0]
        self.health = potion.amount
        self.inventory['health'].pop()
        print(f"You have taken {potion.name} and restored you health to "
              f"{self.health}")

    def puppet_play(self):
        import json
        import random

        # Load scenarios from the JSON file with UTF-8 encoding
        with open("play_scenarios.json", "r", encoding="utf-8") as f:
            scenarios = json.load(f)

        # Pick a random scenario
        current_scenario = random.choice(list(scenarios.keys()))
        scenario_text = scenarios[current_scenario]

        # Display puppets and let the player choose one for flavor
        puppets = self.puppets
        if not puppets:
            print("No puppets available to play with.")
            return

        print("Available puppets:")
        for index, puppet in enumerate(puppets, start=1):
            print(f"{index}. {puppet.name}")

        # Ask the player to choose a puppet (purely for fun)
        selected_puppet_index = input(
            "Which puppet would you like to play with? Enter the number: ")

        try:
            selected_puppet_index = int(selected_puppet_index) - 1
            selected_puppet = puppets[selected_puppet_index]
        except (ValueError, IndexError):
            print("Invalid choice. Defaulting to the first puppet.")
            selected_puppet = puppets[0]

        # Replace pronouns in the scenario text (excluding "his")
        puppet_name = selected_puppet.name
        scenario_text = scenario_text.replace(" he ",
                                              f" {puppet_name} ").replace(
            " He ", f" {puppet_name.capitalize()} ")
        scenario_text = scenario_text.replace(" him ",
                                              f" {puppet_name} ").replace(
            " Him ", f" {puppet_name.capitalize()} ")
        scenario_text = scenario_text.replace(" he.",
                                              f" {puppet_name}.").replace(
            " He.", f" {puppet_name.capitalize()}.")

        # Split the scenario text into paragraphs
        paragraphs = scenario_text.split(
            "\n\n")  # Assumes paragraphs are separated by double newlines

        # Display the scenario one paragraph at a time
        print(f"\nYou chose to play with: {puppet_name}\n")
        for paragraph in paragraphs:
            print(paragraph.strip())
            input("\nPress Enter to continue...\n")

