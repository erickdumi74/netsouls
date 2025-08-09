from core.armors.armor import Armor 

armor_lib = {
    "leather_vest": Armor("Leather Vest", defense=2, weight=1, requirements={"STR": 2}),
    "iron_plate": Armor("Iron Plate", defense=4, weight=3, requirements={"STR": 5, "END": 3})
}

def get_armor(armor_name):
    armor = armor_lib.get(armor_name)
    if not armor:
        raise ValueError(f"Armor '{armor_name}' not found.")
    return armor
