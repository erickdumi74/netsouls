import curses

class Weapon:
    def __init__(self, name, arc, stamina_cost, stamina_delay, damage
                 , glyphs, shield_behavior, stamina_damage
                 , mapping=None, animation_duration=1):
        self.name = name
        self.arc = arc
        self.mapping = mapping
        self.stamina_cost = stamina_cost
        self.stamina_delay = stamina_delay
        self.damage = damage
        self.stamina_damage = stamina_damage
        self.glyphs = glyphs
        self.shield_behavior = shield_behavior
        self.owner = None

        # Animation state
        self.animation_timer = 0
        self.animation_duration = animation_duration
        self.animating = False
        self.animation_frame = 0  # current frame index
    
    def attack(self):
        self._handle_stamina()
        self._handle_animation()
        #return None
    
    def _handle_animation(self):
        self.animating = True
        self.animation_frame = 0
        self.animation_timer = self.animation_duration  # ← CORE LINE
        self.owner._stamina_regen_delay = self.stamina_delay
    
    def _handle_stamina(self):
        if self.owner and self.owner.stamina >= self.stamina_cost:
            self.owner.drain_stamina(self.stamina_cost)
        else:
            self.animating = False
            return "Not enough stamina!"

    def handle_animation_time(self):
        if self.animating:
            self.animation_timer -= 1
            self.animation_frame += 1
            if self.animation_timer <= 0:
                self.animating = False
                self.animation_frame = 0

    def render_attack_frame(self, screen, y, x, direction):
        if direction == "up" and y > 0:
            screen.addstr(y - 1, x, self.glyphs["up"])
        elif direction == "down" and y < curses.LINES - 1:
            screen.addstr(y + 1, x, self.glyphs["down"])
        elif direction == "left" and x > 0:
            screen.addstr(y, x - 1, self.glyphs["left"])
        elif direction == "right" and x < curses.COLS - 1:
            screen.addstr(y, x + 1, self.glyphs["right"])
    
    def get_attack_tiles(self, y, x, direction):
        if direction == "up":
            return [(y - 1, x)]
        elif direction == "down":
            return [(y + 1, x)]
        elif direction == "left":
            return [(y, x - 1)]
        elif direction == "right":
            return [(y, x + 1)]
        return []