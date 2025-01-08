import threading
from collections import deque

from pynput import keyboard, mouse


class HotkeyManager:
    def __init__(self):
        self.pressed_keys = set()

        self.hotkey_handlers = []
        self.scroll_handlers = []

        self.keyboard_listener = None
        self.mouse_listener = None

        self.action_queue = deque(maxlen=1)
        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)

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
        self.worker_thread.start()

        self.keyboard_listener.join()
        self.mouse_listener.join()
        self.worker_thread.join()

    def _on_press(self, key):
        n = self._normalize_key(key)
        self.pressed_keys.add(n)
        for s, callback in self.hotkey_handlers:
            if s == self.pressed_keys:
                self.action_queue.append(callback)

    def _on_release(self, key):
        n = self._normalize_key(key)
        self.pressed_keys.discard(n)

    def _on_scroll(self, x, y, dx, dy):
        d = 'up' if dy > 0 else 'down'
        for s, sd, callback in self.scroll_handlers:
            if s == self.pressed_keys and sd == d:
                self.action_queue.append(callback)

    def _worker_loop(self):
        while True:
            if self.action_queue:
                action = self.action_queue.popleft()
                action()

    @staticmethod
    def _normalize_key(k):
        if isinstance(k, keyboard.Key):
            return k.name.lower()
        if isinstance(k, keyboard.KeyCode):
            if k.char is not None:
                if 1 <= ord(k.char) <= 26:
                    return chr(ord('a') + (ord(k.char) - 1))
                return k.char.lower()
            if k.vk is not None:
                if 65 <= k.vk <= 90:
                    return chr(k.vk + 32)
                if 97 <= k.vk <= 122:
                    return chr(k.vk)
                return str(k.vk)

        return str(k).lower()
