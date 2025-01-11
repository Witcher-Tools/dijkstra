# Dijkstra
REDkit hotkeys extender.

After installation, the Dijkstra Hotkey Extender can optionally set itself to run at startup. It quietly sits in the background until the REDkit editor launches. Once REDkit is running, a tray icon pops up to show that the hotkey extender is active. You can right-click this tray icon to close the app, and it will stay closed until you restart your PC or launch it again manually.

---

## Hotkeys

### Terrain Edit Tool
- `Alt + Scroll Up` — Increase scale
- `Alt + Scroll Down` — Decrease scale
- `Shift + Scroll Up` — Increase slope
- `Shift + Scroll Down` — Decrease slope
- `Ctrl + Q` — Decrease probability
- `Ctrl + E` — Increase probability
- `Ctrl + Shift + Q` — Decrease probability by 5
- `Ctrl + Shift + E` — Increase probability by 5
- `Ctrl + Alt + Q` — Decrease probability by 30
- `Ctrl + Alt + E` — Increase probability by 30
- `Ctrl + V` — Check/uncheck vertical texture mask
- `Ctrl + H` — Check/uncheck horizontal texture mask
- `F1` — Select brush preset 1
- `F2` — Select brush preset 2
- `F5` — Select brush preset 3
- `F6` — Select brush preset 4
- `F7` — Select brush preset 5

### Vegetation Edit Tool
- `1` — Select 1 brush
- `2` — Select 2 brush
- `3` — Select 3 brush
- `4` — Select 4 brush
- `5` — Select 5 brush
- `6` — Select 6 brush

---

## Build
You can change hotkeys or add new by changing ```register_hotkeys``` functions in modules folder.

Then you can build it with pyinstaller.
```
pip install -r requirements.txt
pyinstaller dijkstra.spec
```
Resulting executable will be in `dist` folder.