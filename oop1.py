class Superhero:
    def __init__(self, name, secret_identity, power_level=50):
        # Encapsulated attributes (protected with single underscore)
        self._name = name
        self._secret_identity = secret_identity
        self._power_level = max(0, min(100, power_level))

    # Property getters for encapsulated attributes
    @property
    def name(self):
        return self._name

    @property
    def secret_identity(self):
        return self._secret_identity

    @property
    def power_level(self):
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        self._power_level = max(0, min(100, value))

    def introduce(self):
        return f"I am {self._name}, but my secret identity is {self._secret_identity}!"
    def use_power(self):
        return f"{self._name} uses a generic hero power at level {self._power_level}!"
    def __str__(self):
        return f"{self._name} (Power: {self._power_level})"
class TechHero(Superhero):
    def __init__(self, name, secret_identity, power_level, gadget):
        super().__init__(name, secret_identity, power_level)
        self.gadget = gadget
    def use_power(self):
        return f"{self._name} deploys {self.gadget} at power level {self._power_level}!"
    def upgrade_gadget(self):
        self._power_level += 10
        return f"{self.gadget} upgraded! New power: {self._power_level}"
class MagicHero(Superhero):
    def __init__(self, name, secret_identity, power_level, spell):
        super().__init__(name, secret_identity, power_level)
        self.__spell = spell  # Private attribute
    def use_power(self):
        return f"{self._name} casts {self.__spell}! ✨ (Power: {self._power_level})"
    def reveal_spell(self):
        return f"My secret spell is {self.__spell}"
if __name__ == "__main__":
    # Create instances
    generic_hero = Superhero("Captain", "zemc geb", 75)
    iron_tech = TechHero("Iron Coder", "Hens ze", 60, "Python Gauntlet")
    merlin = MagicHero("Merlin 2.0", "mlul we", 90, "Infinite Loop Curse")
    # Polymorphism demo
    heroes = [generic_hero, iron_tech, merlin]
    for hero in heroes:
        print(hero.use_power())
    # Properly accessing encapsulated attributes
    print("\n" + merlin.reveal_spell())
    print(f"\nHero name: {iron_tech.name}")  # Now works via getter
    print(f"Secret identity: {iron_tech.secret_identity}")
    print(f"Current power: {iron_tech.power_level}")
    # Attempting to modify power
    iron_tech.power_level = 200  # Auto-clamped to 100
    print(f"Power after overflow attempt: {iron_tech.power_level}")