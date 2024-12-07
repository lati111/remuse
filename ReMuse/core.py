import dearpygui.dearpygui as dpg
from ReMuse.UI import manager

class Core:
    UI = None

    def __init__(self):
        self.UI = manager.UIManager()
        self.UI.openHomeWindow()

