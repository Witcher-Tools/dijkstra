class VegetationEditModule:
    def __init__(self, app, hotkey_manager):
        try:
            window = app.window(title="Vegetation Edit Tool")



        except Exception as e:
            print(e)

        self.register_hotkeys(hotkey_manager)

    def register_hotkeys(self, hotkey_manager):

        pass
