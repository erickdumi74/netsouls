from core.weapons.sword import Sword
from core.weapons.axe import Axe
from core.weapons.pipe import Pipe

weapons_lib = {
    "sword": Sword,
    "axe": Axe,
    "pipe": Pipe,
}

def get_weapon(weapon_name):
    weapon = weapons_lib.get(weapon_name)
    if not weapon:
        raise ValueError(f"Weapon '{weapon_name}' not found.")
    return weapon()
