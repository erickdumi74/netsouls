from core.shields.shield import Shield

class RoundShield(Shield):
    def __init__(self):
        super().__init__(
            name="Round Shield",
            glyphs = {
                "up":    "0",  # use only in 1 direction (too wide for all)
                "down":  "0",
                "left":  "0",
                "right": "0"
            },
            defense=2
        )

