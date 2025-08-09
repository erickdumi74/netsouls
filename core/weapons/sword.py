from core.weapons.weapon import  Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__(
            name="Sword",
            arc=["forward"],
            stamina_cost=2,
            stamina_delay=10,
            damage=4,
            stamina_damage=2,
            glyphs={"up": "↑", "down": "↓", "left": "←", "right": "→"},
            shield_behavior="drop_active_direction",
            animation_duration=3
        )
