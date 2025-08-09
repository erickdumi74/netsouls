import curses

class Echo:
    def __init__(self, y, x, amount):
        self.y = y
        self.x = x
        self.amount = amount
        self.reclaimed = False

    def position(self):
        return self.y, self.x

    def is_at(self, y, x):
        return self.y == y and self.x == x
    
    def draw(self, screen):
        screen.addstr(self.y, self.x, "º", curses.color_pair(3))
