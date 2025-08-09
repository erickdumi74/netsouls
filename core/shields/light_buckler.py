# core/shields/light_buckler.py
from core.shields.shield import Shield

class LightBuckler(Shield):
    def __init__(self):
        super().__init__(
            name = "Light Buckler", 
            glyphs = {
            'up':    '^',
            'down':  'v',
            'left':  '<',
            'right': '>'
            },
            defense=1)