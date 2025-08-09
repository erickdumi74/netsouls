import curses

def handle_death_sequence(stdscr, y=19, x=0):
    """Draws a HUD-style death message at a fixed position (like the HUD)."""

    death_msg = "YOU ARE DEAD!"
    prompt_msg = "Press ESC to respawn"

    stdscr.addstr(y, x, "┌" + "─" * 27 + "┐")

    # Draw 'YOU DIED' in bold red
    stdscr.addstr(y + 1, x, "│ ")
    stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr(f"{death_msg:<26}")  # HUD-width formatted
    stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr("│")

    # Draw the respawn prompt below
    stdscr.addstr(y + 2, x, f"│ {prompt_msg:<26}│")

    # Bottom border if needed
    stdscr.addstr(y + 3, x, "└" + "─" * 27 + "┘")