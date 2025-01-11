class VegetationEditModule:
    def __init__(self, app, hotkey_manager):
        try:
            window = app.window(title="Vegetation Edit Tool")

            self.buttons = []

            self.buttons = [
                window.child_window(class_name="Static", found_index=3),
                window.child_window(class_name="Static", found_index=4),
                window.child_window(class_name="Static", found_index=5),
                window.child_window(class_name="Static", found_index=6),
                window.child_window(class_name="Static", found_index=7),
                window.child_window(class_name="Static", found_index=8)
            ]
        except Exception:
            pass

        self.register_hotkeys(hotkey_manager)

    def register_hotkeys(self, hotkey_manager):
        for i in range(1, 9):
            hotkey_manager.register_hotkey([str(i)], lambda x=i: self.handle_preset(x))

    def handle_preset(self, idx):
        if 0 <= idx - 1 < len(self.buttons):
            self.buttons[idx-1].click()
