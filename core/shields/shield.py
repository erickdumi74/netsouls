# core/shield.py
import curses

class Shield:
    def __init__(self, name, glyphs, defense):
        self.name = name
        self.glyphs = glyphs
        self.active_directions = set()
        self.defense = defense

    def toggle(self, direction):
        if direction in self.active_directions:
            self.active_directions.remove(direction)
        else:
            self.active_directions.clear()
            self.active_directions.add(direction)

    def clear(self):
        self.active_directions.clear()

    def add(self, direction):
        self.active_directions.add(direction)

    def has(self, direction):
        return direction in self.active_directions

    def render(self, screen, y, x):
        for direction in self.active_directions:
            glyph = self.glyphs.get(direction, '?')
            if direction == 'up' and y > 0:
                screen.addstr(y - 1, x, glyph)
            elif direction == 'down' and y < curses.LINES - 1:
                screen.addstr(y + 1, x, glyph)
            elif direction == 'left' and x > 0:
                screen.addstr(y, x - 1, glyph)
            elif direction == 'right' and x < curses.COLS - 1:
                screen.addstr(y, x + 1, glyph)

    def apply_blocking_behavior(self, incoming_direction, weapon_behavior):
        """
        Override this in subclasses for different behaviors like passive block, multi-angle, etc.
        """
        return incoming_direction in self.active_directions
