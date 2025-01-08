class TerrainEditModule:
    def __init__(self, app, hotkey_manager):
        try:
            window = app.window(title="Terrain Edit Tools")

            self.scale_button = window.child_window(class_name="msctls_updown32", found_index=0)
            self.slope_button = window.child_window(class_name="msctls_updown32", found_index=1)

            self.brush_preset1 = window.child_window(title="1", class_name="Button")
            self.brush_preset2 = window.child_window(title="2", class_name="Button")
            self.brush_preset3 = window.child_window(title="3", class_name="Button")
            self.brush_preset4 = window.child_window(title="4", class_name="Button")
            self.brush_preset5 = window.child_window(title="5", class_name="Button")
            self.brush_preset6 = window.child_window(title="6", class_name="Button")

            self.probability_bar = window.child_window(class_name="msctls_trackbar32", found_index=8)
        except Exception as e:
            print(e)

        self.register_hotkeys(hotkey_manager)

    def register_hotkeys(self, hotkey_manager):
        hotkey_manager.register_hotkey(['f1'], self.handle_brush_preset)

        hotkey_manager.register_scroll_hotkey(['alt_l'], 'up', self.handle_scale_up)
        hotkey_manager.register_scroll_hotkey(['alt_l'], 'down', self.handle_scale_down)

        hotkey_manager.register_scroll_hotkey(['shift_l'], 'up', self.handle_slope_up)
        hotkey_manager.register_scroll_hotkey(['shift_l'], 'down', self.handle_slope_down)

        hotkey_manager.register_hotkey(['ctrl_l', 'q'], self.handle_probability_preset_decrease)
        hotkey_manager.register_hotkey(['ctrl_l', 'e'], self.handle_probability_preset_increase)

    def handle_brush_preset(self):
        print("Brush preset")
        self.brush_preset1.click()

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

    def handle_probability_preset_decrease(self):
        rect = self.probability_bar.rectangle()
        width = rect.right - rect.left
        height = rect.bottom - rect.top

        x_offset = int(width * 0.1)
        y_offset = int(height / 2)

        self.probability_bar.click(coords=(x_offset, y_offset))
        # self.probability_bar.type_keys("{LEFT 15}", set_foreground=False)

    def handle_probability_preset_increase(self):
        rect = self.probability_bar.rectangle()
        width = rect.right - rect.left
        height = rect.bottom - rect.top

        x_offset = int(width * 0.9)
        y_offset = int(height / 2)

        self.probability_bar.click(coords=(x_offset, y_offset))
        # self.probability_bar.type_keys("{RIGHT 15}", coords=(start_coords, end_coords))
