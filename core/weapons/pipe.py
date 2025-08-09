from core.weapons.weapon import  Weapon

class Pipe(Weapon):
    def __init__(self):
        super().__init__(
            name="Pipe",
            arc=["forward"],
            stamina_cost=1,
            stamina_delay=4,
            damage=1,
            stamina_damage=1,
            glyphs={"up": "|", "down": "|", "left": "-", "right": "-"},
            shield_behavior="drop_active_direction",
            animation_duration=2
        )