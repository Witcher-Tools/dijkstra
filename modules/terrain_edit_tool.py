class TerrainEditModule:
    def __init__(self, ui_helper):
        self.ui_helper = ui_helper
        self.slope_button = None
        self.scale_button = None

    def initialize(self):
        """Initialize buttons dynamically."""
        tools_window = self.ui_helper.find_window("Terrain Edit Tools")
        self.slope_button = self.ui_helper.find_button(tools_window, class_name="msctls_updown32", index=1)
        self.scale_button = self.ui_helper.find_button(tools_window, class_name="msctls_updown32", index=0)

    def register_hotkeys(self, hotkey_manager):
        """Register hotkeys for this module."""
        hotkey_manager.register_hotkey((keyboard.Key.shift, mouse.Button.middle), self.handle_slope_scroll)
        hotkey_manager.register_hotkey((keyboard.Key.alt, mouse.Button.middle), self.handle_scale_scroll)

    def handle_slope_scroll(self, dy):
        """Handle slope button scroll."""
        if dy > 0:
            self.ui_helper.click_button(self.slope_button)
        else:
            self.ui_helper.click_button(self.slope_button, bottom=True)

    def handle_scale_scroll(self, dy):
        """Handle scale button scroll."""
        if dy > 0:
            self.ui_helper.click_button(self.scale_button)
        else:
            self.ui_helper.click_button(self.scale_button, bottom=True)
