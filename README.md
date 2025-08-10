# 🥔 Netsouls

**An ASCII roguelike with a Soulslike heartbeat… and a potato for a hero.**  
Timing, stamina, and stubbornness — no hunger clocks, no fluff.

---

## 📄 License
This project is licensed under the **Polyform Noncommercial License 1.0.0**.  
You may use, copy, and modify this software for personal or noncommercial purposes only.  
See the [LICENSE](LICENSE) file for full terms.

- **You may**: Play, share, modify, and distribute Netsouls for **noncommercial purposes**.
- **You may not**: Sell, license, or monetize Netsouls or derivatives without **written permission**.
- **Commercial licensing**: Contact me if you wish to use Netsouls commercially.

© 2025 Erick Dumitrescu – Terminal Minds. All rights reserved except as granted under the license.

---

## 📜 Lore Snapshot
In the Starchborn Age, **Echoes** are memory made real — currency, power, and life itself.  
You are **Sir Atarms**, the Potato Knight, roaming shifting realms where death is a lesson and every return leaves a scar.  
Some chase the **First Thread** to master the Netsouls. You just aim to endure.

---

## 🕹 How to Play

### Prerequisites
- **Python 3.10+**
- A terminal or command prompt

### Run the Game
```bash
# Clone the repo
git clone https://github.com/erickdumi74/netsouls.git
cd netsouls

# Run it
python -m pip install windows-curses #if on windows and its first time playing
python main.py
```
### Direction, Combat and Items

**Movement**
- `i` = Up
- `k` = Down
- `j` = Left
- `l` = Right  
_(You cannot move into occupied tiles.)_

**Combat**
- `e` = Attack Up
- `d` = Attack Down
- `s` = Attack Left
- `f` = Attack Right

**Shields**
- `Space` then one of `e/d/s/f` = Raise or lower shield in that direction  
  _(Press Space first to arm the shield, then a direction key. Shields interact with weapon timing and stamina.)_

**Gear Switching**
- `r` = Switch weapon
- `w` = Switch shield
- `g` = Switch armor  
_(You can switch gear mid‑fight.)_

**Death & Respawn**
- `Esc` = Respawn (only when dead)

**Tips**
- Stamina matters: attacks and defenses may delay regen.
- Positioning > face‑tank: avoid standing where the enemy’s next arc will land.
- Read the HUD: enemy bars and cues matter.

**Need a refresher in‑game?** Press `?` for the help panel.


