# core/player.py
from core.entity import Entity
from core.weapons.ns_weapons_dict import get_weapon
from core.shields.ns_shields_dict import get_shield
from core.armors.ns_armor_dict import get_armor
from core.items.echo import Echo
import curses

class PotatoKnight(Entity):

    def __init__(self, y, x):
        super().__init__(y, x, char='@')

        self.initial_x = x
        self.initial_y = y

        self.current_shield = get_shield("light_buckler")
        self.shield_intenvtory = ["light_buckler", "round_shield"]
        self.pending_shield = False

        self.equip_weapon(get_weapon("pipe"))

        self.weapon_inventory = ["pipe","sword", "axe"]
        self.current_weapon_index = 0
        self.last_attack_direction = None
        self.attack_direction = 'right'  # still fine to keep
        self.attacking = False

        self.armor_inventory = ["leather_vest","iron_plate"]
        self.current_armor = None
        self.current_armor_index = None

        self.hp = 50
        self.max_hp = 50
        self.stamina = 20
        self.max_stamina = 20
        self.attributes = {
            "STR": 3,
            "VIT": 2,
            "END": 4
        }

        self._stamina_regen_timer = 0
        self._stamina_regen_cooldown = 10  # Adjust this to slow it down (higher = slower regen)
        self._stamina_regen_delay = 70
        self._regeneration_delay_timer = 0 

        self.blink_timer = 0

        self.current_echo = Echo(self.y, self.x, 1200)
        self.dropped_echo = None

        self.item_keys = {
            ord('e'): 'up',
            ord('d'): 'down',
            ord('s'): 'left',
            ord('f'): 'right'
        }

    def equip_weapon(self, weapon):
        weapon.owner = self
        self.current_weapon = weapon

    def draw(self, screen):

        if not self.is_alive():
            screen.addstr(self.y, self.x, 'X', curses.color_pair(1))
            return

        if self.blink_timer > 0:
            screen.addstr(self.y, self.x, '@', curses.A_REVERSE)
            self.blink_timer -= 1
        else:
            screen.addstr(self.y, self.x, self.char)

        # Attack animation
        if self.current_weapon.animating:
            self.current_weapon.render_attack_frame(screen, self.y, self.x, self.attack_direction)

        # Shield rendering
        self.current_shield.render(screen, self.y, self.x)   

        # Lost echo rendering
        if self.dropped_echo:
            self.dropped_echo.draw(screen)         
    
    def toggle_shield(self, direction):
        self.current_shield.toggle(direction)

    def switch_weapon(self):
        self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapon_inventory)
        new_weapon_name = self.weapon_inventory[self.current_weapon_index]
        
        self.equip_weapon(get_weapon(new_weapon_name))
        
        print(f"Sir Atarms has equipped: {self.current_weapon.name}")

    def switch_armor(self):
        if not self.armor_inventory:
            print("You have no armor to switch to.")
            return

        if self.current_armor_index is None:
            self.current_armor_index = 0
        else:
            self.current_armor_index = (self.current_armor_index + 1) % len(self.armor_inventory)
        
        new_armor_name = self.armor_inventory[self.current_armor_index]
        
        #self.equip_weapon(get_weapon(new_armor_name))
        self.current_armor = get_armor(new_armor_name)

        print(f"Sir Atarms has equipped: {self.current_armor.name}")

    def switch_shield(self):
        current_index = self.shield_intenvtory.index(self.current_shield.name.lower().replace(" ", "_"))
        next_index = (current_index + 1) % len(self.shield_intenvtory)
        next_shield_name = self.shield_intenvtory[next_index]
        self.current_shield = get_shield(next_shield_name)
        print(f"Sir Atarms has equipped: {self.current_shield.name}")

    def regenerate_stamina(self):
        if self.stamina < self.max_stamina:
            if self._regeneration_delay_timer < self._stamina_regen_delay:
                self._regeneration_delay_timer += 1
                return  # Wait for delay to pass
            if self._stamina_regen_timer >= self._stamina_regen_cooldown:
                self.stamina += 1
                self._stamina_regen_timer = 0
            else:
                self._stamina_regen_timer += 1

    def recover_echo(self):
        if self.is_alive():
            if self.dropped_echo and self.y == self.dropped_echo.y and self.x == self.dropped_echo.x:
                self.current_echo = self.dropped_echo
                self.dropped_echo = None

    def update(self):
        self.regenerate_stamina()
        self.current_weapon.handle_animation_time()
        self.recover_echo()
            

    def respawn(self):
        self.hp = self.max_hp
        self.stamina = self.max_stamina

        # Reset position to spawn point (must be set elsewhere)
        self.y = self.initial_y
        self.x = self.initial_x

        # Reset any flags
        self.dead_handled = False
        self.pending_shield = False
        self.shield_direction = set()

        # Optionally reset other state
        self.current_weapon.animating = False
        self._regeneration_delay_timer = 0

        # Optional: restore flask, clear status effects, etc.
        # self.flask_uses = self.max_flask_uses

    def die(self):
        if self.current_echo: # drop echoes
            self.current_echo.x = self.x
            self.current_echo.y = self.y
            self.dropped_echo = self.current_echo
            self.current_echo = None
        else: # loose all echoes on second death
            self.dropped_echo = None
            self.current_echo = Echo(self.y, self.x, 0)
            
    def drain_stamina(self, amount):
        self.stamina = max(0, self.stamina - amount)
        self._regeneration_delay_timer = 0

    def drain_health(self, amount):
        self.hp = max(0, self.hp - amount)
        
