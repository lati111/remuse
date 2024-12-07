import dearpygui.dearpygui as dpg
from ReMuse.UI import base

class PlaylistUI(base.BaseUI):
    tag = "playlist_window"

    def __init__(self, UIManager):
        base.BaseUI.__init__(self, UIManager)

        with dpg.window(tag=self.tag):
            dpg.add_text("Playlists")


