import dearpygui.dearpygui as dpg
from ReMuse.UI import home, playlists

class UIManager:
    currentUI = None;

    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title='ReMuse', width=600, height=200)
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def openHomeWindow(self):
        self.switchWindows(home.HomeUI(self))

    def openPlaylistWindow(self):
        self.switchWindows(playlists.PlaylistUI(self))

    def switchWindows(self, newUI):
        if (self.currentUI != None):
            dpg.delete_item(self.currentUI.tag)

        self.currentUI = newUI
        dpg.set_primary_window(newUI.tag, True)
        dpg.start_dearpygui()
        dpg.destroy_context()
        
