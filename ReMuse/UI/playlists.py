import dearpygui.dearpygui as dpg
from ReMuse.UI import base
from ReMuse.DB import database

class PlaylistUI(base.BaseUI):
    tag: str = "playlist_window"
    addPlaylistModalTag: str = "add_playlist_modal"

    db = database.Database()

    def __init__(self, UIManager):
        base.BaseUI.__init__(self, UIManager)
        self.db = database.Database()
        self.setup()
            
    def setup(self):
        with dpg.window(tag=self.tag):
            # Title
            with dpg.group(horizontal=True):
                dpg.add_text("Playlists")
                dpg.add_button(label="+", callback=self.openNewPlaylistModal)

            # Playlist table
            with dpg.table(header_row=True):
                dpg.add_table_column(label="Playlists")
                dpg.add_table_column(label="Songs")

                with dpg.table_row():
                    dpg.add_text("Good vibes")
                    dpg.add_text("128")
                    
                with dpg.table_row():
                    dpg.add_text("Battle music")
                    dpg.add_text("9")            

    def openNewPlaylistModal(self, sender, app_data):
        dpg.delete_item(self.addPlaylistModalTag)

        with dpg.window(tag=self.addPlaylistModalTag, width=200, height=100, pos=[dpg.get_viewport_width() / 2 - 100, dpg.get_viewport_height() / 2 - 75], modal=True):
            dpg.add_input_text(tag="playlist_title_input", label="Title")
            dpg.add_button(label="Add", callback=self.saveNewPlaylist)
        
    def saveNewPlaylist(self):
        title: str = dpg.get_value('playlist_title_input')
        if (title == ''):
            self.toast('The title field cannot be empty')
            return

        if (self.db.playlist.titleIsUnique(title) == False):
            self.toast('A playlist with this title already exists')
            return

        self.db.playlist.insert(title)
        dpg.delete_item(self.addPlaylistModalTag)

