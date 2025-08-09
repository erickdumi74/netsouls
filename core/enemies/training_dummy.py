from core.enemies.enemy import Enemy

class TrainingDummy(Enemy):
    def __init__(self, y, x):
        super().__init__(y, x, name="Dummy", hp=50, stamina=20, glyph='D',
                         _stamina_regen_cooldown=2, _stamina_regen_delay=5)

    def take_damage(self, amount):
        hp = self.hp
        super().take_damage(amount)
        self.hp = hp

    def drain_stamina(self, amount):
        #stamina = self.stamina
        super().drain_stamina(amount)
        #self.stamina = stamina