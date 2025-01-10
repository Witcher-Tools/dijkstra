import threading
import queue

from pynput import keyboard, mouse


class HotkeyManager:
    def __init__(self):
        self.pressed_keys = set()

        self.hotkey_handlers = []
        self.scroll_handlers = []

        self.keyboard_listener = None
        self.mouse_listener = None

        self.action_queue = queue.Queue(maxsize=2)

        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self.worker_thread.start()

    def register_hotkey(self, keys, callback):
        combo = frozenset(self._normalize_key(k) for k in keys)
        self.hotkey_handlers.append((combo, callback))

    def register_scroll_hotkey(self, keys, direction, callback):
        combo = frozenset(self._normalize_key(k) for k in keys)
        d = direction.lower()
        self.scroll_handlers.append((combo, d, callback))

    def start_listening(self):
        self.keyboard_listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        self.mouse_listener = mouse.Listener(on_scroll=self._on_scroll)

        self.keyboard_listener.start()
        self.mouse_listener.start()

        self.keyboard_listener.join()
        self.mouse_listener.join()

        self.action_queue.put(None)

        self.worker_thread.join()

    def stop_listening(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    def _on_press(self, key):
        norm = self._normalize_key(key)
        self.pressed_keys.add(norm)
        for combo, callback in self.hotkey_handlers:
            if combo == self.pressed_keys:
                if not self.action_queue.full():
                    self.action_queue.put(callback)

    def _on_release(self, key):
        norm = self._normalize_key(key)
        self.pressed_keys.discard(norm)

    def _on_scroll(self, x, y, dx, dy):
        direction = 'up' if dy > 0 else 'down'
        for combo, scroll_dir, callback in self.scroll_handlers:
            if combo == self.pressed_keys and scroll_dir == direction:
                if not self.action_queue.full():
                    self.action_queue.put(callback)

    def _worker_loop(self):
        while True:
            try:
                task = self.action_queue.get()
            except queue.Empty:
                continue
            if task is None:
                break
            task()
            self.action_queue.task_done()

    @staticmethod
    def _normalize_key(k):
        if isinstance(k, keyboard.Key):
            return (k.name or '').lower()
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
