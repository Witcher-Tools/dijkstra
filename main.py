from pywinauto import Application

from core.hotkey_manager import HotkeyManager
from modules.terrain_edit_tool import TerrainEditModule
from modules.vegetation_edit_tool import VegetationEditModule


def main():
    m = HotkeyManager()

    a = Application().connect(title_re=".*REDkit.*")

    TerrainEditModule(a, m)
    VegetationEditModule(a, m)

    m.start_listening()


if __name__ == "__main__":
    main()
