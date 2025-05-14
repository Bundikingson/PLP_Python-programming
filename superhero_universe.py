"""
superhero_universe.py
A Python OOP demonstration featuring:
1. Superhero class with encapsulation and inheritance
2. Animal polymorphism example
"""

# --- Assignment 1: Superhero Class with Inheritance ---
class Superhero:
    """Base class representing a superhero"""
    def __init__(self, name, secret_identity, power_level):
        self._name = name  # Protected attribute
        self.__secret_identity = secret_identity  # Private attribute
        self.power_level = power_level
        self._villains_defeated = 0

    def introduce(self):
        """Public method to introduce the hero"""
        print(f"I am {self._name}! Power level: {self.power_level}")

    def reveal_secret(self, password):
        """Encapsulation example: controlled access to private data"""
        if password == "JLADarkKnight":
            print(f"My real identity is {self.__secret_identity}")
        else:
            print("Access denied!")

    def attack(self):
        """Base attack method to be overridden by subclasses"""
        print(f"{self._name} uses a basic attack!")

    def __str__(self):
        return f"Superhero: {self._name} (Power: {self.power_level})"


class TechHero(Superhero):
    """Subclass representing tech-based heroes"""
    def __init__(self, name, secret_identity, power_level, gadget):
        super().__init__(name, secret_identity, power_level)
        self.gadget = gadget

    def attack(self):
        """Polymorphism: Override attack method"""
        print(f"{self._name} deploys {self.gadget}!")

    def hack(self):
        """Unique method for tech heroes"""
        print(f"{self._name} is hacking the mainframe...")


class MagicHero(Superhero):
    """Subclass representing magic-based heroes"""
    def __init__(self, name, secret_identity, power_level, spell):
        super().__init__(name, secret_identity, power_level)
        self.spell = spell

    def attack(self):
        """Polymorphism: Override attack method"""
        print(f"{self._name} casts {self.spell}!")

    def teleport(self):
        """Unique method for magic heroes"""
        print(f"{self._name} vanishes in a puff of smoke!")


# --- Assignment 2: Animal Polymorphism Example ---
class Animal:
    """Base class for animals demonstrating polymorphism"""
    def __init__(self, name):
        self.name = name

    def move(self):
        """To be overridden by subclasses"""
        print(f"{self.name} is moving in a generic way")

    def speak(self):
        """To be overridden by subclasses"""
        pass


class Dog(Animal):
    def move(self):
        print(f"{self.name} runs happily on four legs! 🐕")

    def speak(self):
        print("Woof! Woof!")


class Fish(Animal):
    def move(self):
        print(f"{self.name} swims gracefully through the water! 🐟")

    def speak(self):
        print("Blub blub...")


class Bird(Animal):
    def move(self):
        print(f"{self.name} soars through the sky! 🦅")

    def speak(self):
        print("Chirp! Chirp!")


# --- Demonstration Code ---
if __name__ == "__main__":
    print("=== Superhero Demonstration ===")
    iron_man = TechHero("Iron Man", "Tony Stark", 95, "Repulsor Beams")
    dr_strange = MagicHero("Doctor Strange", "Stephen Strange", 99, "Crimson Bands of Cyttorak")

    iron_man.introduce()
    iron_man.attack()
    iron_man.hack()
    iron_man.reveal_secret("JLADarkKnight")

    dr_strange.introduce()
    dr_strange.attack()
    dr_strange.teleport()

    print("\n=== Animal Polymorphism Demonstration ===")
    animals = [
        Dog("Rex"),
        Fish("Nemo"),
        Bird("Eagle")
    ]

    for animal in animals:
        animal.move()
        animal.speak()
