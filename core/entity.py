# core/entity.py
import math

class Entity:
    def __init__(self, y, x, char='@'):
        self.y = y
        self.x = x
        self.char = char

    def draw(self, screen):
        screen.addstr(self.y, self.x, self.char)

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, amount):
         if self.is_alive():
            self.handle_damage(self.get_total_defense(), amount)
            self.blink_timer = 3
            if self.hp == 0:
                self.die()

    def get_total_defense(self):
        armor_def = self.current_armor.defense if self.current_armor else 0
        shield_def = self.current_shield.defense if self.current_shield.active_directions else 0
        natural_def = ((self.attributes["END"] * 0.5) +
                    (self.attributes["STR"] * 0.3) +
                    (self.attributes["VIT"] * 0.2)) / 2

        buff = self.current_armor.buff if self.current_armor else 1.0

        return math.floor((natural_def + armor_def + shield_def) * buff)

    def handle_damage(self, total_defense, damage): 
        if total_defense == 0:
            self.drain_health(damage)
            return
        
        if total_defense >= damage:
            # Need to figure out the stamina count for the defense
            self._calculate_stamina_count(total_defense)
            return
        
        if  total_defense < damage:
            health_loss = damage - total_defense
            self.drain_health(health_loss)
            # Need to figure out the stamina count for the defense
            self._calculate_stamina_count(total_defense)

    def _calculate_stamina_count(self, total_defense):
        if self.stamina >= total_defense: # I have enough stamina take it from there
            self.drain_stamina(total_defense)
        else:
            health_loss = total_defense - self.stamina
            self.drain_stamina(self.stamina)
            self.drain_health(health_loss)
        return




