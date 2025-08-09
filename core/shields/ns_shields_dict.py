from core.shields.light_buckler import LightBuckler
from core.shields.round_shield import RoundShield

shields_lib = {
    "light_buckler": LightBuckler,
    "round_shield": RoundShield,
}
def get_shield(shield_name):
    shield = shields_lib.get(shield_name)
    if not shield:
        raise ValueError(f"Shield '{shield_name}' not found.")
    return shield()