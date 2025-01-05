import json
from pynput import keyboard, mouse


class HotkeyManager:
    def __init__(self):
        self.keybindings = {}
        self.keyboard_listener = None
        self.mouse_listener = None

    def register_hotkey(self, key_combination, action):
        """Register a new hotkey."""
        self.keybindings[key_combination] = action

    def load_config(self, config_path):
        """Load hotkeys from a configuration file."""
        with open(config_path, 'r') as file:
            config = json.load(file)
            for entry in config["hotkeys"]:
                self.register_hotkey(tuple(entry["keys"]), entry["action"])

    def start_listeners(self):
        """Start listening for keyboard and mouse events."""
        self.keyboard_listener = keyboard.Listener(on_press=self._on_key_press)
        self.mouse_listener = mouse.Listener(on_scroll=self._on_scroll)
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def _on_key_press(self, key):
        """Handle key press events."""
        for keys, action in self.keybindings.items():
            if all(k in keys for k in [key]):
                action()

    def _on_scroll(self, x, y, dx, dy):
        """Handle mouse scroll events."""
        if (keyboard.Key.shift,) in self.keybindings:
            action = self.keybindings.get((keyboard.Key.shift,))
            action(dy)
