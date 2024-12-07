import dearpygui.dearpygui as dpg
from UI import manager

class Core:
    UI = None

    def __init__(self):
        self.UI = manager.UIManager()
        self.UI.openHomeWindow()

core = Core()