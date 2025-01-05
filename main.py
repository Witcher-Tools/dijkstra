from pynput import keyboard, mouse

from core.hotkey_manager import HotkeyManager
from modules.terrain_edit_tool import TerrainEditModule


def main():
    hotkey_manager = HotkeyManager()

    terrain_module = TerrainEditModule()
    terrain_module.register_hotkeys(hotkey_manager)

    hotkey_manager.start_listeners()


if __name__ == "__main__":
    main()

# app = Application().connect(title_re=".*REDkit.*")
# tools = app.window(title="Vegetation Edit Tool")
#
# panel = tools.child_window(title="panel", class_name="wxWindowNR", found_index=0)
# # panel.print_control_identifiers(filename='ex4')
#
# buttons = []
#
# for children in panel.children():
#     if children.window_text() != '' and children.window_text() != 'm_brushDescPanel':
#         try:
#             button = tools.child_window(title=children.window_text(), class_name="Static")
#             buttons.append(button)
#         except Exception:
#             pass
#
# current_button = 0
# print("But", buttons)
#
# #
# # slopeButton = tools.child_window(class_name="msctls_updown32", found_index=1)
# # scaleButton = tools.child_window(class_name="msctls_updown32", found_index=0)
# #
# # brushPreset1 = tools.child_window(title="1", class_name="Button")
# # brushPreset2 = tools.child_window(title="2", class_name="Button")
# # brushPreset3 = tools.child_window(title="3", class_name="Button")
# # brushPreset4 = tools.child_window(title="4", class_name="Button")
# # brushPreset5 = tools.child_window(title="5", class_name="Button")
# # brushPreset6 = tools.child_window(title="6", class_name="Button")
# #
# # paint = tools.child_window(title="Paint", class_name="Button")
# #
# # rect = slopeButton.rectangle()
# #
# # bottom_center_x = (rect.left + rect.right) // 2
# # bottom_center_y = rect.bottom - 1
# #
#
# def on_key_press(key):
#     # global shift_pressed, alt_pressed, ctrl_pressed
#     global buttons, current_button
#
#     if key == keyboard.Key.f1:
#
#         current_button = 0
#
#         buttons[current_button].click()
#
#
#     # if key == keyboard.Key.shift:
#     #     shift_pressed = True
#     # if key == keyboard.Key.alt_l:
#     #     alt_pressed = True
#     # if key == keyboard.Key.ctrl_l:
#     #     ctrl_pressed = True
#     #
#     # if key == keyboard.Key.f1:
#     #     brushPreset1.click_input()
#     # if key == keyboard.Key.f2:
#     #     brushPreset2.click_input()
#     # if key == keyboard.Key.f3:
#     #     brushPreset3.click_input()
#     # if key == keyboard.Key.f4:
#     #     brushPreset4.click_input()
#     # if key == keyboard.Key.f5:
#     #     brushPreset5.type_keys('{VK_SPACE}')
#     # if key == keyboard.Key.f6:
#     #     brushPreset6.type_keys('{VK_SPACE}')
#
# def on_key_release(key):
#     global shift_pressed, alt_pressed, ctrl_pressed
#     # if key == keyboard.Key.shift:
#     #     shift_pressed = False
#     # if key == keyboard.Key.alt_l:
#     #     alt_pressed = False
#     # if key == keyboard.Key.ctrl_l:
#     #     ctrl_pressed = False
# #
# # def on_scroll(x, y, dx, dy):
# #     global shift_pressed, alt_pressed, slopeButton, bottom_center_x, bottom_center_y
# #
# #     if shift_pressed:
# #         if dy > 0:
# #             try:
# #                 slopeButton.click()
# #             except Exception:
# #                 pass
# #         else:
# #             try:
# #                 slopeButton.click(coords=(bottom_center_x, bottom_center_y))
# #             except Exception:
# #                 pass
# #     if alt_pressed:
# #         if dy > 0:
# #             try:
# #                 scaleButton.click()
# #             except Exception:
# #                 pass
# #         else:
# #             try:
# #                 scaleButton.click(coords=(bottom_center_x, bottom_center_y))
# #             except Exception:
# #                 pass
# #
# keyboard_listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
# # mouse_listener = mouse.Listener(on_scroll=on_scroll)
#
# keyboard_listener.start()
# # mouse_listener.start()
#
# keyboard_listener.join()
# # mouse_listener.join()
