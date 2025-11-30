class Character:
    def __init__(self, name, description, health=100, attack=10, defense=5):
        """
        Initializes a new character.

        Args:
            name (str): The character's name.
            description (str): A brief description of the character.
            health (int, optional): The character's initial health points. Defaults to 100.
            attack (int, optional): The character's attack strength. Defaults to 10.
            defense (int, optional): The character's defense strength. Defaults to 5.
        """
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        """Reduces the character's health by a given amount."""
        self.health -= damage

    def attack_target(self, target):
        """Simulates an attack on a target character."""
        damage = self.attack - target.defense  # Simple damage calculation
        if damage > 0:
            target.take_damage(damage)
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack against {target.name} is blocked!")

    def __str__(self):
        """Returns a string representation of the character."""
        return f"{self.name} ({self.description}). Health: {self.health}"


# Example Usage
hero = Character("Aella", "A brave knight with a shining sword.", health=120, attack=15, defense=8)
goblin = Character("Grob", "A small, green goblin with a rusty dagger.", health=50, attack=8, defense=2)


