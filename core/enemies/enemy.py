# core/enemy.py
import curses

class Enemy:
    def __init__(self, y, x, name="Enemy", hp=10, stamina=5, glyph='E', movement_speed=0, passable_through=False, 
                 _stamina_regen_cooldown=5, _stamina_regen_delay=10, damage=5, attack_cost=5):
        self.y = y
        self.x = x
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.stamina = stamina
        self.max_stamina = stamina
        self.glyph = glyph
        self.blink_timer = 0
        self._initial_blink_timer_value = 3
        self.move_cooldown = 0
        self.movement_speed = movement_speed # The higher the number, the slower the monster
        self.passable_through = passable_through
        self._regeneration_delay_timer = 0
        self._stamina_regen_cooldown = _stamina_regen_cooldown  # Adjust this to slow it down (higher = slower regen)
        self._stamina_regen_delay = _stamina_regen_delay  # frames before regen begins
        self._stamina_regen_timer = 0
        self.damage = damage
        self.attack_cost = attack_cost
        
    def move(self, player, all_enemies):
        if self.movement_speed == 0:
            return

    def draw(self, screen):
        if not self.is_alive():
            screen.addstr(self.y, self.x, 'x')
            return 

        if self.blink_timer > 0:
            screen.addstr(self.y, self.x, self.glyph, curses.A_REVERSE)
            self.blink_timer -= 1
        else:
            screen.addstr(self.y, self.x, self.glyph)

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if self.is_alive():
            self.blink_timer = self._initial_blink_timer_value
            self.hp -= amount
            self.hp = max(0, self.hp)
            self._regeneration_delay_timer = 0

    def drain_stamina(self, amount):
        self.stamina = max(0, self.stamina - amount)
        self._regeneration_delay_timer = 0

    def update(self, player, enemies):
        self.regenerate_stamina()
        self.move(player, enemies)

    def do_move(self, directions, all_enemies, player):
        for dy, dx in directions:
            new_y = self.y + dy
            new_x = self.x + dx

            # Skip if out of bounds
            if not (0 <= new_y < curses.LINES and 0 <= new_x < curses.COLS):
                continue

            # Check if move is blocked by player or another enemy
            if (new_y, new_x) == (player.y, player.x) and not self.passable_through:
                continue

            for other in all_enemies:
                if (
                    other is not self 
                    and other.is_alive() 
                    and (other.y, other.x) == (new_y, new_x)
                    and not other.passable_through
                ):
                    break  # spot is blocked — abort this direction
            else:
                # This else-block runs ONLY if the loop did **not** break
                self.y = new_y
                self.x = new_x
                break  # found valid move — stop checking other directions

    def regenerate_stamina(self):
        #with open("debug.log", "a") as f:
        #    f.write(f"[{self.__class__.__name__}] Regen tick at {self.stamina}\n")
        if self.stamina < self.max_stamina:
            if self._regeneration_delay_timer < self._stamina_regen_delay:
                self._regeneration_delay_timer += 1
                return  # Wait for delay to pass
            if self._stamina_regen_timer >= self._stamina_regen_cooldown:
                self.stamina += 1
                self._stamina_regen_timer = 0
            else:
                self._stamina_regen_timer += 1

    def attack_player(self, player):
        if self.stamina >= self.attack_cost:  # Example stamina cost
            damage = self.damage  # You could make this variable per enemy
            player.take_damage(damage)
            self.drain_stamina(self.attack_cost)
            # self.blink_timer = self.initial_blink_timer_value  # Enemy can flash too if you like

    def try_attack_player(self, player):
        raise NotImplementedError("The try_attack_player method needs to be implemented by sub-class: {self}")
