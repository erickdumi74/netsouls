from core.enemies.enemy import Enemy
import random

class MoldBlob(Enemy):
    def __init__(self, y, x):
        super().__init__(y, x, name="Mold Blob", hp=50, stamina=30, glyph='B', movement_speed=8, passable_through=False,
                         _stamina_regen_cooldown=7, _stamina_regen_delay=15, damage=5)

    def move(self, player, all_enemies):
        if self.move_cooldown > 0:
            self.move_cooldown -= 1
            return

        # Attack logic - for mold_blob
        if self.try_attack_player(player):
            self.move_cooldown = self.movement_speed
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        random.shuffle(directions)

        self.do_move(directions, all_enemies, player)

        self.move_cooldown = self.movement_speed

    def try_attack_player(self, player):
        """Check if player is adjacent and attack if possible."""
        if not player.is_alive():
            return False

        dy = abs(self.y - player.y)
        dx = abs(self.x - player.x)

        if (dy == 1 and dx == 0) or (dy == 0 and dx == 1):
            self.attack_player(player)
            return True

        return False