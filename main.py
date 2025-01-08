from pywinauto import Application

from core.hotkey_manager import HotkeyManager
from modules.terrain_edit_tool import TerrainEditModule

if __name__ == "__main__":
    m = HotkeyManager()

    a = Application().connect(title_re=".*REDkit.*")

    terrain_edit_tool = TerrainEditModule(a, m)
    vegetation_edit_tool = TerrainEditModule(a, m)

    m.start_listening()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        m.stop_listening()
