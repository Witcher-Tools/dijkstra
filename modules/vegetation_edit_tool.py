class VegetationEditModule:
    def __init__(self, app, hotkey_manager):
        try:
            window = app.window(title="Vegetation Edit Tool")
            panel = window.child_window(title="panel", class_name="wxWindowNR", found_index=0)

            self.buttons = []

            for children in panel.children():
                if children.window_text() != '' and children.window_text() != 'm_brushDescPanel':
                    try:
                        button = window.child_window(title=children.window_text(), class_name="Static")
                        self.buttons.append(button)
                    except Exception:
                        pass

        except Exception as e:
            print(e)

        self.register_hotkeys(hotkey_manager)

    def register_hotkeys(self, hotkey_manager):
        for i in range(1, 9):
            hotkey_manager.register_hotkey([str(i)], lambda x=i: self.handle_preset(x))

    def handle_preset(self, idx):
        if 0 <= idx < len(self.buttons):
            self.buttons[idx].click()
