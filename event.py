import pyWinhook as pyHook


if __name__ == "__main__":
    def on_mouse_event(event):
        if event.MessageName == "mouse wheel":
            print("Mouse wheel intercepted")
            if event.Wheel > 0:
                print("Custom CTRL + Mouse Wheel Up")
                return False  # Prevent the event from propagating to the editor
        return True  # Allow other events


    hm = pyHook.HookManager()
    hm.MouseWheel = on_mouse_event
    hm.HookMouse()
