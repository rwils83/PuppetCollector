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
        return f"You have added {puppet.name} to the puppet show. Enjoy " \
               f"your new puppet, Puppet Master!"

    def show_inventory(self):
        spells = '\r\n\t'.join(spell.name for spell in self.inventory['spells'])
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
""")