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
            if len(self.player.inventory['health']) > 0:
                use_potion = input("Would you like to use a health "
                                   "potion?\r\n1.Yes\r\n2.No\r\n")
                if use_potion == "1":
                    print(f"You have used a health potion, adding "
                          f"{self.player.inventory['health'][0].amount} "
                          f"health!")
                    self.player.health = self.player.health + \
                                         self.player.inventory['health'][0] \
                                             .amount
                    self.player.inventory['health'].remove(
                        self.player.inventory['health'][0]
                    )

                else:
                    print(f"The battle will continue. Good luck Puppet "
                          f"Master! ")
            self.player_damage_given()
            if self.enemy.health > 0:
                print(f"You hit {self.enemy.name} with your "
                      f"{self.player.current_weapon.name} "
                      f"for "
                      f"{self.player.damage_modifier()} "
                      f"damage. The enemy health is now: {self.enemy.health}")
            else:
                print(f"You delivered the final blow and "
                      f"{self.enemy.name} is dead.")
                return
            self.enemy_damage_given()
            if self.player.health > 0:
                print(
                    f"You were hit for {self.enemy.damage}. Your health is now: "
                    f"{self.player.health}")
            else:
                print("You have lost the battle and are now dead")
