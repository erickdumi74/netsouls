class CombatEngine:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies  # List of all enemies in the world
        self.already_hit = set()

    def reset_hits(self):
        self.already_hit.clear()

    def handle_combat(self):
        weapon = self.player.current_weapon
        if not weapon or not weapon.animating:
            self.reset_hits()
            return

        direction = self.player.attack_direction
        attack_pos = self.get_attack_position(self.player.y, self.player.x, direction)

        for enemy in self.enemies:
            if enemy.is_alive() and (enemy.y, enemy.x) == attack_pos:
                if enemy not in self.already_hit:
                    if self.player.stamina >= weapon.stamina_cost:
                        enemy.take_damage(weapon.damage)
                        enemy.drain_stamina(weapon.stamina_damage)
                        self.already_hit.add(enemy)

    def get_attack_position(self, y, x, direction):
        if direction == "up":
            return y - 1, x
        elif direction == "down":
            return y + 1, x
        elif direction == "left":
            return y, x - 1
        elif direction == "right":
            return y, x + 1
        return y, x
