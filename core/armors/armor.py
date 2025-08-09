class Armor:
    def __init__(self, name, defense, weight, requirements=None, buff=1.0):
        self.name = name
        self.defense = defense
        self.weight = weight
        self.requirements = requirements or {}  # e.g., {"STR": 2}
        self.buff = buff  # Optional: modifies final defense (1.0 = neutral)
