import dearpygui.dearpygui as dpg
from UI import manager

class Core:
    UI = None

    def __init__(self):
        print("core init")
        self.UI = manager.UIManager()
        self.UI.openHome()

core = Core()