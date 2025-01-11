class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_damage_given(self):
        self.enemy.health = self.enemy.health - self.player.damage_modifier()

    def enemy_damage_given(self):
        # will need to figure out logic for modifier
        self.player.health = self.player.health - self.enemy.damage

    def combat_loop(self):
        vulnerabilities = ", ".join(self.enemy.stats['Weaknesses'])
        print(f"You have discovered an anomaly, {self.enemy.name}. You must "
              f"rid Puppet Town of this disgrace!!")
        print(f"Your investigation shows that {self.enemy.name} is "
              f"vulnerable to {vulnerabilities}")

        while self.player.armor_modifier() > 0 and self.enemy.health > 0:
            round_summary = []  # Collect messages for a summary at the end
            # of the round

            # Option to use a health potion
            if len(self.player.inventory['health']) > 0:
                use_potion = input(
                    "Would you like to use a health "
                    "potion?\r\n1.Yes\r\n2.No\r\n")
                if use_potion == "1":
                    potion = self.player.inventory['health'][0]
                    self.player.health += potion.amount
                    round_summary.append(
                        f"You used a health potion and restored {potion.amount} health!")
                    self.player.inventory['health'].remove(potion)
                else:
                    round_summary.append(
                        "You chose not to use a health potion.")

            # Player attacks
            self.player_damage_given()
            if self.enemy.health > 0:
                round_summary.append(
                    f"You hit {self.enemy.name} with your {self.player.current_weapon.name} "
                    f"for {self.player.damage_modifier()} damage. The enemy's health is now {self.enemy.health}."
                )
            else:
                print(
                    f"You delivered the final blow and {self.enemy.name} is dead.")
                return

            # Enemy attacks
            self.enemy_damage_given()
            if self.player.health > 0:
                round_summary.append(
                    f"The enemy hit you for {self.enemy.damage} damage. Your "
                    f"health is now {self.player.health}."
                )
            else:
                print("You have lost the battle and are now dead.")
                return

            # Print the summary for this combat round
            print("\n".join(round_summary))
            input("\nPress Enter to continue to the next round...\n")

