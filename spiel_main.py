# ----------------------------
# 🛡️ OOP Combat Game
# ----------------------------
# This script demonstrates Python OOP concepts:
# Classes, inheritance, methods, and basic combat mechanics.
# The output is deterministic, intended for testing and learning.

class Character:
    """
    Base class for all characters (Player and Monster).
    Handles shared attributes and behaviors:
    - health
    - power
    - receiving damage
    - attacking another character
    """

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def receive_damage(self, damage):
        """
        Applies damage (or healing if negative) to the character.
        Health cannot drop below 0.
        Provides console feedback.
        """
        self.health -= damage

        # Prevent health from going below 0
        if self.health < 0:
            self.health = 0

        # Feedback depending on effect
        if damage > 0:
            print(f"{self.name} received {damage} damage.\n")
        elif damage < 0:
            print(f"{self.name} gained {-damage} health!")
        else:
            print(f"{self.name} was not affected.")

    def attack(self, target):
        """
        Inflicts damage equal to self.power on the target character.
        """
        print(f"{self.name} attacks {target.name} for {self.power} damage!\n")
        target.receive_damage(self.power)


class Player(Character):
    """
    Player-controlled character.
    Inherits from Character and adds:
    - Level
    - Level-up mechanics (health + power growth)
    """

    def __init__(self, name):
        super().__init__(name, health=3, power=1)
        self.level = 1

        # Initial stats display
        print(f"These are the starting stats for {self.name}:\n"
              f"Level = {self.level}\n"
              f"Health = {self.health}\n"
              f"Power = {self.power}\n")

    def level_up(self):
        """
        Increases level and improves stats.
        Health is capped at 10.
        """
        self.level += 1
        self.health = min(self.health + 1, 10)
        self.power += 1
        print(f"{self.name} leveled up! "
              f"Level: {self.level}, Health: {self.health}, Power: {self.power}")


class Monster(Character):
    """
    Enemy character.
    Inherits from Character and adds:
    - Rage mechanic (temporary power boost)
    """

    def __init__(self, name):
        super().__init__(name, health=6, power=1)
        self.base_power = self.power  # Save original power to reset after rage

    def rage(self, is_raging):
        """
        Toggles rage mode.
        When raging, power is doubled.
        """
        if is_raging:
            self.power = self.base_power * 2
            print(f"{self.name} is raging! Power doubled to {self.power}.")
        else:
            self.power = self.base_power
            print(f"{self.name} calmed down. Power reset to {self.power}.")


# ----------------------------
# Example Test / Demo
# ----------------------------

print("Testing:")

# Create characters
player1 = Player("Han")
monster1 = Monster("Goblin")

# ----------------------------
# Turn 1
# ----------------------------
player1.attack(monster1)  # Player attacks monster
monster1.attack(player1)  # Monster attacks player

# Add a visual break between turns
print("\n" + "-"*40 + "\n")

# ----------------------------
# Turn 2
# ----------------------------
# Apply massive damage to demonstrate health floor
monster1.receive_damage(100)  # Health cannot go below 0
player1.level_up()             # Player levels up

# Add a visual break
print("\n" + "-"*40 + "\n")

# ----------------------------
# Turn 3
# ----------------------------
# Monster rage and attack
monster1.rage(True)
monster1.attack(player1)

# End of demo
print("\nDemo complete!")
