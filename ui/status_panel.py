# status_panel.py
from ui.render_bar import render_bar
import curses

def render_status_panel(stdscr, y, x, player, enemies, max_distance=8):
    """Draws the HUD directly on stdscr at (y, x), using curses color pairs."""

    # ┌ Top border
    stdscr.addstr(y, x, "┌" + "─" * 27 + "┐")

    y = y + 1
    stdscr.addstr(y, x, "│")
    stdscr.addstr("      » PLAYER STATUS      ", curses.color_pair(4))
    stdscr.addstr("│")

    # HP
    y = y + 1
    draw_stat_bar(stdscr, y, x, "HP ", player.hp, player.max_hp)

    # STA
    y = y + 1
    draw_stat_bar(stdscr, y, x, "STA", player.stamina, player.max_stamina)

    # Echoes

    y = y + 1
    if player.current_echo:
        draw_echo_bar(stdscr, y, x, player.current_echo.amount, False)
    else:
        draw_echo_bar(stdscr, y, x, player.dropped_echo.amount, True)

    y = y + 1
    stdscr.addstr(y, x, "│                           │")

    # Equipment
    y = y + 1
    stdscr.addstr(y, x, "│")
    stdscr.addstr(" »  ITEMS                  ", curses.color_pair(4))
    stdscr.addstr("│")

    y = y + 1
    draw_equipment_line(stdscr, y, x, "WPN", player.current_weapon.name)
    y = y + 1
    shield_name = f"[{player.current_shield.name}]" if not player.current_shield.active_directions else player.current_shield.name
    draw_equipment_line(stdscr, y, x, "SHD", shield_name)
    y = y + 1
    armor_name = f"{player.current_armor.name} (+{player.current_armor.defense})" if player.current_armor else "None"
    draw_equipment_line(stdscr, y, x, "ARM", armor_name)
    y = y + 1
    stdscr.addstr(y , x, "│                           │")

    offset = draw_enemies(stdscr, y, x, enemies, player, max_distance)

    stdscr.addstr(offset, x, "└" + "─" * 27 + "┘")

def draw_equipment_line(stdscr, y, x, label, value, width=21):
    stdscr.addstr(y, x, f"│ {label}: {value:<{width}}│")

def draw_stat_bar(stdscr, y, x, label, value, max_value, bar_width=10):
    """Draws a single stat bar (HP/STA) with color and padded value display."""
    bar, color = render_bar(value, max_value, bar_width)
    stdscr.addstr(y, x, f"│ {label}: ", curses.A_BOLD)
    stdscr.addstr(bar, curses.color_pair(color))
    stdscr.addstr(f" {value:>3}/{max_value:<4}  │")

def draw_echo_bar(stdscr, y, x, amount, lost_echoes):
    echo_str = f"[{amount:,}]" if lost_echoes else f"{amount:,}"
    content = f" ECH: {echo_str}"
    padded = content.ljust(27)  # 27 characters inside the borders
    stdscr.addstr(y, x, f"│{padded}│")

def draw_enemies(stdscr, y, x, enemies, player, max_distance):
    # Enemies

    draw_header = True
    offset = y = y + 1
    for enemy in enemies:
        dist = abs(enemy.y - player.y) + abs(enemy.x - player.x)
        if dist <= max_distance:
            if draw_header:
                stdscr.addstr(y, x, "│")
                stdscr.addstr(" »  ENEMIES NEARBY         ", curses.color_pair(4))
                stdscr.addstr("│")
                draw_header = False
                offset += 1

            hp, hp_color = render_bar(enemy.hp, enemy.max_hp, 6)
            st, st_color = render_bar(enemy.stamina, enemy.max_stamina, 6)
            stdscr.addstr(offset,   x, f"│ {enemy.name[:8]:<8} HP: ", curses.A_BOLD)
            stdscr.addstr(hp, curses.color_pair(hp_color))
            stdscr.addstr(f" {enemy.hp:>2}/{enemy.max_hp:<2} │")
            offset += 1
            stdscr.addstr(offset, x, f"│          ST: ", curses.A_BOLD)
            stdscr.addstr(st, curses.color_pair(st_color))
            stdscr.addstr(f" {enemy.stamina:>2}/{enemy.max_stamina:<2} │")
            offset += 1
    return offset

