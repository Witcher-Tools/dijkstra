import json
from pynput import keyboard, mouse


class HotkeyManager:
    def __init__(self):
        self.keybindings = []  # List of dictionaries with "keys" and "action"
        self.active_keys = set()  # Track currently pressed keys
        self.keyboard_listener = None
        self.mouse_listener = None

    def register_hotkey(self, keys, action):
        """Register a hotkey combination with an associated action."""
        self.keybindings.append({"keys": keys, "action": action})

    def load_config(self, config_path):
        """Load hotkeys configuration from a JSON file."""
        with open(config_path, 'r') as file:
            config = json.load(file)
            for entry in config["hotkeys"]:
                self.register_hotkey(entry["keys"], entry["action"])

    def start_listeners(self):
        """Start keyboard and mouse listeners."""
        self.keyboard_listener = keyboard.Listener(
            on_press=self._on_key_press,
            on_release=self._on_key_release
        )
        self.mouse_listener = mouse.Listener(on_scroll=self._on_scroll)

        self.keyboard_listener.start()
        self.mouse_listener.start()

        self.mouse_listener.join()
        self.keyboard_listener.join()

    def _on_key_press(self, key):
        try:
            self.active_keys.add(key.char.lower() if hasattr(key, "char") else key)
        except AttributeError:
            self.active_keys.add(key)

        for binding in self.keybindings:
            keys, action = binding["keys"], binding["action"]

            if all(k in self.active_keys for k in keys):
                action()

    def _on_key_release(self, key):
        """Handle key release events."""
        try:
            # Remove key from active keys set
            self.active_keys.discard(key.char.lower() if hasattr(key, "char") else key)
        except AttributeError:
            self.active_keys.discard(key)

    def _on_scroll(self, x, y, dx, dy):
        """Handle mouse scroll events."""
        for binding in self.keybindings:
            keys, action = binding["keys"], binding["action"]

            # Check if "scroll" and all keys are active
            if "scroll" in keys and all(k in self.active_keys for k in keys if k != "scroll"):
                action(dy)  # Pass scroll direction to the action
