class TerrainEditModule:
    def __init__(self, app, hotkey_manager):
        try:
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

        self.register_hotkeys(hotkey_manager)

    def register_hotkeys(self, hotkey_manager):
        hotkey_manager.register_hotkey(['f1'], self.handle_brush_preset)

        hotkey_manager.register_scroll_hotkey(['alt_l'], 'up', self.handle_scale_up)
        hotkey_manager.register_scroll_hotkey(['alt_l'], 'down', self.handle_scale_down)

        hotkey_manager.register_scroll_hotkey(['ctrl_l'], 'up', self.handle_slope_up)
        hotkey_manager.register_scroll_hotkey(['ctrl_l'], 'down', self.handle_slope_down)

        pass

    def handle_brush_preset(self):
        self.brushPreset1.click()
        print("Brush preset")

    def handle_slope_up(self):
        self.slope_button.click()
        print("Slope up")

    def handle_slope_down(self):
        self.slope_button.click(coords=(5, 5))
        print("Slope down")

    def handle_scale_up(self):
        self.scale_button.click()
        print("Scale up")

    def handle_scale_down(self):
        self.scale_button.click(coords=(5, 5))
        print("Scale down")
