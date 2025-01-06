from pywinauto import Application
from pynput import keyboard


class TerrainEditModule:
    def __init__(self):
        try:
            app = Application().connect(title_re=".*REDkit.*")
            window = app.window(title="Terrain Edit Tools")

            self.scale_button = window.child_window(class_name="msctls_updown32", index=0)
            self.slope_button = window.child_window(class_name="msctls_updown32", index=1)

            self.brushPreset1 = window.child_window(title="1", class_name="Button")
            self.brushPreset2 = window.child_window(title="2", class_name="Button")
            self.brushPreset3 = window.child_window(title="3", class_name="Button")
            self.brushPreset4 = window.child_window(title="4", class_name="Button")
            self.brushPreset5 = window.child_window(title="5", class_name="Button")
            self.brushPreset6 = window.child_window(title="6", class_name="Button")
        except Exception as e:
            print(e)

    def register_hotkeys(self, hotkey_manager):
        hotkey_manager.register_hotkey([keyboard.Key.shift_l, "scroll"], self.handle_slope_scroll)
        hotkey_manager.register_hotkey([keyboard.Key.alt_l, "scroll"], self.handle_scale_scroll)
        hotkey_manager.register_hotkey([keyboard.Key.f1], self.handle_brush_preset)
        hotkey_manager.register_hotkey([keyboard.Key.f2], self.handle_brush_preset2)

    def handle_brush_preset(self):
        # self.brushPreset1.click()
        print("Brush preset")

    def handle_brush_preset2(self):
        # self.brushPreset2.set_keyboard_focus()
        # self.brushPreset2.type_keys("{SPACE}", set_foreground=False)
        print("Brush preset 2")

    def handle_scale_scroll(self, dy):
        print("Scrolling scale", dy)

    def handle_slope_scroll(self, dy):
        print("Scrolling slope", dy)
