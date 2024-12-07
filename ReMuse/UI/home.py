import dearpygui.dearpygui as dpg

class HomeUI:
    tag = "home_window"

    def __init__(self):
        with dpg.window(tag=self.tag):
            dpg.add_button(tag="playlists_btn", label="Playlists")
            # dpg.add_button(tag="playlists_btn", label="Playlists", callback=openPlaylists)


