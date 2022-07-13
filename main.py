import dearpygui.dearpygui as dpg
import time

dpg.create_context()
# dpg.show_style_editor()
dpg.create_viewport(title='Eye Rest Reminder', width=600, height=300)

def on_click(item):
    # print(dpg.get_value(item))
    countdown = dpg.get_value("input") * 60
    # print(countdown)
    while dpg.get_value(item) and countdown > 0:
        countdown -= 1
        time.sleep(1)
        dpg.set_value(display, countdown)
    dpg.set_value(item, False)

with dpg.window(label="Example Window",tag="Primary Window"):
    
    dpg.add_checkbox(label="Enable Countdown", enabled=True, callback=on_click)

    with dpg.theme(tag="__input"):
        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 15)
    tick = dpg.add_input_int(label="Set Countdown (Minutes)", width=200, tag="input")
    dpg.bind_item_theme(dpg.last_item(), "__input")

    display = dpg.add_text("Hello", color=(255,0,0))

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, False, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()