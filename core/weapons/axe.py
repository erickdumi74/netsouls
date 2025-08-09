from core.weapons.weapon import Weapon

class Axe(Weapon):
    def __init__(self):
        super().__init__(
            name="Axe",
            arc=["right", "forward", "left"],
            stamina_cost=3,
            stamina_delay=13,
            damage=5,
            stamina_damage=3,
            glyphs={"up": "┬", "down": "┴", "left": "├", "right": "┤"},
            shield_behavior="drop_all_temporarily",
            animation_duration=5
        )
