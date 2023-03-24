'''
Author: Radish
Date: 2023-03-01 11:40
LastEditors: Radish
LastEditTime: 2023-03-01 15:33
Description: Dear PyGui 
See: https://www.osgeo.cn/dearpygui/index.html
'''
import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    font = dpg.add_font(file="fonts/SourceHanSansCN-Bold.otf", size=18)
dpg.bind_font(font)

def callback(sender, app_data):
    print("sender:", sender)
    print("app_data:", app_data)

dpg.add_file_dialog(directory_selector=True, show=False, callback=callback, tag="select_dir")
    
with dpg.window(label="图片压缩",tag="Primary Window"):
    dpg.add_text("图片压缩")
    dpg.add_button(label="Directory Selector", callback=lambda: dpg.show_item("select_dir"))

# dpg.show_font_manager()
dpg.create_viewport(title='Custom Title', width=600, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()