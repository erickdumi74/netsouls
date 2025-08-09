# engine/engine_bootstrap.py
import curses
from engine.engine import GameEngine

def run_game():
    curses.wrapper(start)

def start(stdscr):
    stdscr.nodelay(True)
    stdscr.timeout(100)
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, 81, curses.COLOR_BLACK)
    
    engine = GameEngine(stdscr)
    engine.run()
