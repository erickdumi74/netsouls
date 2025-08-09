# engine/engine.py
from core.player import PotatoKnight
from core.enemies.training_dummy import TrainingDummy
from core.enemies.mold_blob import MoldBlob
from systems.combat import CombatEngine
from core.input_map import handle_input
from ui.status_panel import render_status_panel
from ui.death_panel import handle_death_sequence


class GameEngine:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.enemies = []
        self.player = PotatoKnight(10, 20)
        for i in range (1, 4):
            self.enemies.append(MoldBlob(7, 20))
        #self.enemies = [MoldBlob(7, 20)]
        self.combat_engine = CombatEngine(self.player, self.enemies)

    def run(self):
        while True:
            self.stdscr.clear()
            
            # Player control
            # optional todo remove into renderer
            self.player.draw(self.stdscr)
            if self.player.is_alive():
                self.player.update()
            
            # Enemy control
            # optional todo remove into renderer
            for enemy in self.enemies:
                enemy.draw(self.stdscr)
                if enemy.is_alive():
                    enemy.update(self.player, self.enemies)
            
            if not self.player.is_alive():
                # Draw death panel
                handle_death_sequence(self.stdscr, y=0, x=80)
            else:
                #render_map(stdscr)
                # Draw HUD panel
                render_status_panel(self.stdscr, y=0, x=80, player=self.player, enemies=self.enemies)        
            
            # Combat mode (if any)
            self.combat_engine.handle_combat()
            
            # Draw the screen
            self.stdscr.refresh()

            # Handle quit
            key = self.stdscr.getch()
            if key == ord('y'):
                break

            # Handle key press
            handle_input(key, self.player, self.combat_engine)
