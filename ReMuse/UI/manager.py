import dearpygui.dearpygui as dpg
from UI import home

class UIManager:
    currentUI = None;

    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title='ReMuse', width=600, height=200)
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def openHome(self):
        self.currentUI = home.HomeUI()
        self.displayWindow()

    def displayWindow(self):
        dpg.set_primary_window(self.currentUI.tag, True)
        dpg.start_dearpygui()
        dpg.destroy_context()
