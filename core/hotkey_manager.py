from pynput import keyboard, mouse


class HotkeyManager:
    def __init__(self):
        self.pressed_keys = set()
        self.hotkey_handlers = []
        self.scroll_handlers = []
        self.keyboard_listener = None
        self.mouse_listener = None

    def register_hotkey(self, keys, callback):
        s = frozenset(self._normalize_key(k) for k in keys)
        self.hotkey_handlers.append((s, callback))

    def register_scroll_hotkey(self, keys, direction, callback):
        s = frozenset(self._normalize_key(k) for k in keys)
        d = direction.lower()
        self.scroll_handlers.append((s, d, callback))

    def start_listening(self):
        self.keyboard_listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        self.mouse_listener = mouse.Listener(on_scroll=self._on_scroll)
        self.keyboard_listener.start()
        self.mouse_listener.start()

        self.mouse_listener.join()
        self.keyboard_listener.join()

    def stop_listening(self):
        if self.keyboard_listener: self.keyboard_listener.stop()
        if self.mouse_listener: self.mouse_listener.stop()

    def _on_press(self, key):
        n = self._normalize_key(key)
        self.pressed_keys.add(n)
        for s, c in self.hotkey_handlers:
            if s.issubset(self.pressed_keys):
                c()

    def _on_release(self, key):
        n = self._normalize_key(key)
        if n in self.pressed_keys:
            self.pressed_keys.remove(n)

    def _on_scroll(self, x, y, dx, dy):
        d = 'up' if dy > 0 else 'down'
        for s, sd, c in self.scroll_handlers:
            if s.issubset(self.pressed_keys) and sd == d:
                c()

    @staticmethod
    def _normalize_key(k):
        if isinstance(k, keyboard.Key):
            return k.name
        if isinstance(k, keyboard.KeyCode):
            c = k.char
            if c is None:
                return 'None'
            if 1 <= ord(c) <= 26:
                return chr(ord('a') + (ord(c) - 1))
            return c.lower()
        return str(k)
