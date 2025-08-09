# render_bar.py

def get_bar_color_pair(ratio):
    """Return curses color pair index based on ratio"""
    if ratio <= 0.33:
        return 1  # Red
    elif ratio <= 0.66:
        return 2  # Yellow
    else:
        return 3  # Green

def render_bar(value, max_value, bar_width):
    """Return (bar_string, color_pair_index)"""
    if max_value == 0:
        return "." * bar_width, 2  # Yellow as default fallback

    ratio = value / max_value
    filled_len = int(round(bar_width * ratio))
    empty_len = bar_width - filled_len

    bar = "#" * filled_len + "." * empty_len
    return bar, get_bar_color_pair(ratio)
