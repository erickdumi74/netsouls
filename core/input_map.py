import curses

# core/input_map.py
def handle_input(key, player, combat_engine):

    if not player.is_alive():
        if key == 27:  # ESC to respawn
            player.respawn()
        return

    if key == ord(' '):
        player.pending_shield = True
        return

    if key == ord('r'):
        player.switch_weapon()
        
    elif key == ord('w'):
        player.switch_shield()

    elif key == ord('g'):
        player.switch_armor()
    
    elif key == ord('i'):  # Up
        new_y = max(0, player.y - 1)
        new_x = player.x
        if not is_tile_occupied(new_y, new_x, combat_engine.enemies):
            player.y = new_y

    elif key == ord('k'):  # Down
        new_y = min(curses.LINES - 1, player.y + 1)
        new_x = player.x
        if not is_tile_occupied(new_y, new_x, combat_engine.enemies):
            player.y = new_y

    elif key == ord('j'):  # Left
        new_x = max(0, player.x - 1)
        new_y = player.y
        if not is_tile_occupied(new_y, new_x, combat_engine.enemies):
            player.x = new_x

    elif key == ord('l'):  # Right
        new_x = min(curses.COLS - 1, player.x + 1)
        new_y = player.y
        if not is_tile_occupied(new_y, new_x, combat_engine.enemies):
            player.x = new_x

    elif key in player.item_keys:
        direction = player.item_keys[key]
        if player.pending_shield:
            # Raise or lower shield in that direction
            player.toggle_shield(direction)
            player.pending_shield = False
        else:
            # Regular attack
            player.attack_direction = direction
            player.current_weapon.attack()

def is_tile_occupied(y, x, enemies, include_dead=False):
    for enemy in enemies:
        if (not include_dead and not enemy.is_alive()) or enemy.passable_through:
            continue
        if (enemy.y, enemy.x) == (y, x):
            return True
    return False

def is_player_tile(y, x, player):
    return (player.y, player.x) == (y, x)