import dearpygui.dearpygui as dpg
import time
import tkinter

dpg.create_context()
# dpg.show_style_editor()
dpg.create_viewport(title='Eye Rest Reminder', width=425, height=345)

# Screen size
root = tkinter.Tk()
viewport_width = root.winfo_screenwidth()
viewport_height = root.winfo_screenheight()
pos_x = viewport_width - dpg.get_viewport_width()
pos_y = viewport_height - dpg.get_viewport_height()
dpg.set_viewport_pos([pos_x,pos_y])
dpg.set_viewport_always_top(False)

# Countdown
def on_click(item):
    countdown = dpg.get_value("input") * 60
    while dpg.get_value(item) and countdown > 0:
        time.sleep(1)
        countdown -= 1
        dpg.set_value(display, countdown)
    if countdown <= 0:
        dpg.set_value(display, "Rest")
    if dpg.get_value(item):
        dpg.set_viewport_always_top(True)
    else:
        dpg.set_viewport_always_top(False)
    dpg.set_value(item, False)
    

# Window, set as main to occupy whole viewport
with dpg.window(label="Example Window",tag="Primary Window"):

    # Checkbox to start countdown
    with dpg.theme(tag="__start"):
        with dpg.theme_component(dpg.mvCheckbox):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 15)
    dpg.add_checkbox(label="Enable Countdown", enabled=True, callback=on_click)
    dpg.bind_item_theme(dpg.last_item(), "__start")

    # Number input for countdown
    with dpg.theme(tag="__input"):
        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 15)
    input = dpg.add_input_int(label="Set Countdown (Minutes)", width=200, tag="input", default_value=20)
    dpg.bind_item_theme(dpg.last_item(), "__input")

    # Display for countdown
    display = dpg.add_text("Ready", color=(255,0,0), )
    with dpg.font_registry():
        display_font = dpg.add_font("ostrich-regular.ttf", 170)
        dpg.bind_item_font(display, display_font)

# Global theme
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, False, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 8, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)
dpg.set_viewport_small_icon("favicon.ico")
dpg.set_viewport_large_icon("favicon.ico")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()