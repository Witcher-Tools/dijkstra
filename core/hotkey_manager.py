from pynput import keyboard, mouse


class HotkeyManager:
    def __init__(self):
        self.keybindings = []
        self.active_keys = set()
        self.keyboard_listener = None
        self.mouse_listener = None

    def register_hotkey(self, keys, action):
        self.keybindings.append({"keys": set(keys), "action": action})

    def start_listeners(self):
        self.keyboard_listener = keyboard.Listener(
            on_press=self._on_key_press,
            on_release=self._on_key_release
        )
        self.mouse_listener = mouse.Listener(on_scroll=self._on_scroll)

        self.keyboard_listener.start()
        self.mouse_listener.start()

        self.keyboard_listener.join()
        self.mouse_listener.join()

    def _on_key_press(self, key):
        try:
            self.active_keys.add(key.char.lower() if hasattr(key, "char") else key)
        except AttributeError:
            self.active_keys.add(key)
        self._check_hotkeys()

    def _on_key_release(self, key):
        try:
            self.active_keys.discard(key.char.lower() if hasattr(key, "char") else key)
        except AttributeError:
            self.active_keys.discard(key)

    def _on_scroll(self, x, y, dx, dy):
        for binding in self.keybindings:
            keys = binding["keys"]
            action = binding["action"]
            if "scroll" in keys and all(k in self.active_keys for k in keys if k != "scroll"):
                action(dy)

    def _check_hotkeys(self):
        for binding in self.keybindings:
            keys, action = binding["keys"], binding["action"]
            if keys.issubset(self.active_keys):
                action()
