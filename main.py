import os
import sys
from time import sleep
from threading import Thread

import win32api
import win32event
import winerror

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')
sys.path.append(vendor_dir)

mutex_name = "Global\\DijkstraUniqueMutexName"
mutex = win32event.CreateMutex(None, False, mutex_name)

if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    sys.exit(0)

tray = None
tray_visible = False

editor_connected = False

running = True


def create_tray():
    global tray
    from PIL import Image
    from pystray import MenuItem, Icon, Menu

    icon = Image.open(resource_path(r"resources/icons/dijkstra.ico"))

    menu = Menu(
        MenuItem("Exit", exit_app)
    )
    tray = Icon("Dijkstra", icon, "REDkit Hotkey Extender", menu)
    tray.run_detached()


def show_tray():
    global tray_visible, editor_connected
    if not tray_visible:
        create_tray()
        tray_visible = True
    editor_connected = True


def stop_tray():
    global tray, tray_visible, editor_connected
    if tray is not None:
        tray.stop()
        tray = None
    tray_visible = False
    editor_connected = False


def run_app(app):
    global editor_connected
    from modules.terrain_edit_tool import TerrainEditModule
    from modules.vegetation_edit_tool import VegetationEditModule
    from core.hotkey_manager import HotkeyManager

    m = HotkeyManager()

    TerrainEditModule(app, m)
    VegetationEditModule(app, m)

    Thread(target=m.start_listening, daemon=True).start()

    show_tray()


def stop_app():
    stop_tray()


def exit_app():
    global running

    stop_app()
    running = False


def app_loop():
    global editor_connected

    def redkit_running():
        from psutil import process_iter

        for p in process_iter(['name']):
            if p.info['name'] and 'editor.exe' == p.info['name']:
                return True

    while running:
        is_running = redkit_running()

        if is_running and not editor_connected:
            from pywinauto import Application
            try:
                run_app(Application().connect(title_re=".*The Witcher 3 REDkit.*"))
            except Exception as e:
                pass
        elif not is_running and editor_connected:
            stop_app()

        sleep(10)


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    Thread(target=app_loop, daemon=True).start()

    while running:
        sleep(5)


if __name__ == "__main__":
    main()
