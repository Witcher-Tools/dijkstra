class TerrainEditModule:
    def __init__(self, app, hotkey_manager):
        try:
            window = app.window(title="Terrain Edit Tools")

            self.scale_button = window.child_window(class_name="msctls_updown32", found_index=0)
            self.slope_button = window.child_window(class_name="msctls_updown32", found_index=1)

            self.preset_buttons = [
                window.child_window(title="1", class_name="Button"),
                window.child_window(title="2", class_name="Button"),
                window.child_window(title="3", class_name="Button"),
                window.child_window(title="4", class_name="Button"),
                window.child_window(title="5", class_name="Button"),
                window.child_window(title="6", class_name="Button")
            ]

            self.probability_bar = window.child_window(class_name="msctls_trackbar32", found_index=8)

            self.horizontal_texture_mask = window.child_window(title="Horizontal Texture Mask:", class_name="Button")
            self.vertical_texture_mask = window.child_window(title="Vertical Texture Mask:", class_name="Button")
        except Exception:
            pass

        self.register_hotkeys(hotkey_manager)

    def register_hotkeys(self, hotkey_manager):
        hotkey_manager.register_hotkey(['f1'], lambda: self.handle_brush_preset(1))
        hotkey_manager.register_hotkey(['f2'], lambda: self.handle_brush_preset(2))
        hotkey_manager.register_hotkey(['f5'], lambda: self.handle_brush_preset(3))
        hotkey_manager.register_hotkey(['f6'], lambda: self.handle_brush_preset(4))
        hotkey_manager.register_hotkey(['f7'], lambda: self.handle_brush_preset(5))

        hotkey_manager.register_scroll_hotkey(['alt_l'], 'up', self.handle_scale_up)
        hotkey_manager.register_scroll_hotkey(['alt_l'], 'down', self.handle_scale_down)

        hotkey_manager.register_scroll_hotkey(['shift'], 'up', self.handle_slope_up)
        hotkey_manager.register_scroll_hotkey(['shift'], 'down', self.handle_slope_down)

        hotkey_manager.register_hotkey(['ctrl_l', 'q'], self.handle_probability_preset_decrease)
        hotkey_manager.register_hotkey(['ctrl_l', 'e'], self.handle_probability_preset_increase)

        hotkey_manager.register_hotkey(['ctrl_l', 'shift', 'q'], lambda: self.handle_probability_preset_decrease(5))
        hotkey_manager.register_hotkey(['ctrl_l', 'shift', 'e'], lambda: self.handle_probability_preset_increase(5))

        hotkey_manager.register_hotkey(['ctrl_l', 'alt_l', 'q'], lambda: self.handle_probability_preset_decrease(30))
        hotkey_manager.register_hotkey(['ctrl_l', 'alt_l', 'e'], lambda: self.handle_probability_preset_increase(30))

        hotkey_manager.register_hotkey(['ctrl_l', 'v'], self.handle_vertical_texture_mask)
        hotkey_manager.register_hotkey(['ctrl_l', 'h'], self.handle_horizontal_texture_mask)

    def handle_brush_preset(self, idx):
        self.preset_buttons[idx - 1].type_keys("{SPACE}")

    def handle_slope_up(self):
        self.slope_button.click()

    def handle_slope_down(self):
        rect = self.slope_button.rectangle()
        bottom_center_x = (rect.left + rect.right) // 2
        bottom_center_y = rect.bottom - 1

        self.slope_button.click(coords=(bottom_center_x, bottom_center_y))

    def handle_scale_up(self):
        self.scale_button.click()

    def handle_scale_down(self):
        rect = self.scale_button.rectangle()
        bottom_center_x = (rect.left + rect.right) // 2
        bottom_center_y = rect.bottom - 1

        self.scale_button.click(coords=(bottom_center_x, bottom_center_y))

    def handle_probability_preset_decrease(self, impact=15):
        self.probability_bar.type_keys(f"{{LEFT {impact}}}")

    def handle_probability_preset_increase(self, impact=15):
        self.probability_bar.type_keys(f"{{RIGHT {impact}}}")

    def handle_horizontal_texture_mask(self):
        self.horizontal_texture_mask.type_keys("{SPACE}", pause=None)

    def handle_vertical_texture_mask(self):
        self.vertical_texture_mask.type_keys("{SPACE}", pause=None)
