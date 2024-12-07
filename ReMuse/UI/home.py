import dearpygui.dearpygui as dpg
from ReMuse.UI import base

class HomeUI(base.BaseUI):
    tag = "home_window"

    def __init__(self, UIManager):
        base.BaseUI.__init__(self, UIManager)

        with dpg.window(tag=self.tag):
            dpg.add_button(tag="playlists_btn", label="Playlists", callback=UIManager.openPlaylistWindow)