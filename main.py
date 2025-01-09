from pywinauto import Application
from PIL import Image

import pystray

from core.hotkey_manager import HotkeyManager
from modules.terrain_edit_tool import TerrainEditModule
from modules.vegetation_edit_tool import VegetationEditModule


def on_clicked_toggle_autorun(tray, item):
    pass


def on_clicked_exit(tray, item):
    tray.stop()


def setup_tray_icon():
    icon = Image.open("icon.png")
    menu = pystray.Menu(
        pystray.MenuItem("Settings", on_clicked_exit),
        pystray.MenuItem("Auto-launch", on_clicked_toggle_autorun),
        pystray.MenuItem("Exit", on_clicked_exit)
    )

    tray = pystray.Icon("Dijkstra", icon, "REDkit hotkey extender", menu)
    tray.run_detached()


def main():
    m = HotkeyManager()
    a = Application().connect(title_re=".*REDkit.*")

    TerrainEditModule(a, m)
    VegetationEditModule(a, m)

    setup_tray_icon()

    m.start_listening()


if __name__ == "__main__":
    main()
