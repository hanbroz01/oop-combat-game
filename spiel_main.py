class Character:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def receive_damage(self, damage):
        self.health -= damage

        # Prevent health from going below 0
        if self.health < 0:
            self.health = 0

        if damage > 0:
            print(f"{self.name} received {damage} damage.")
        elif damage < 0:
            print(f"{self.name} gained {-damage} health!")
        else:
            print(f"{self.name} was not affected.")

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.power} damage!")
        target.receive_damage(self.power)


class Player(Character):

    def __init__(self, name):
        super().__init__(name, health=3, power=1)
        self.level = 1
        print(f"These are the starting stats for {self.name}:\n"
              f"Level = {self.level}\n"
              f"Health = {self.health}\n"
              f"Power = {self.power}\n"
              )

    def level_up(self): 
        self.level += 1
        self.health = min(self.health + 1, 10)
        self.power += 1
        print(f"{self.name} leveled up! Level: {self.level}, Health: {self.health}, Power: {self.power}")


class Monster(Character):
   
    def __init__(self, name):
        super().__init__(name, health=6, power=1)
        self.base_power = self.power   # save original power

    def rage(self, is_raging):
        if is_raging:
            self.power = self.base_power * 2
            print(f"{self.name} is raging! Power doubled to {self.power}.")
        else:
            self.power = self.base_power
            print(f"{self.name} calmed down. Power reset to {self.power}.")






print("Testing:")
player1 = Player("Han")
monster1 = Monster("Goblin")

player1.attack(monster1)  # Goblin health decreases
monster1.attack(player1)  # Player health decreases

monster1.receive_damage(100)  # Health cannot go below 0
player1.level_up()
monster1.rage(True)
monster1.attack(player1)
