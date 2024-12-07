import dearpygui.dearpygui as dpg

class BaseUI:
    UIManager = None
    toastcounter: int = 0

    def __init__(self, UIManager):
        self.UIManager = UIManager

    def toast(self, text: str):
        toastID: str = "toast-"+str(self.toastcounter)


        with dpg.window(tag=toastID, height=50, min_size=[400, 50], no_title_bar=True, no_scrollbar=True, popup=True, no_open_over_existing_popup=False):
            dpg.add_text(text)

        print(dpg.get_item_width(toastID))
        dpg.set_item_pos(toastID, [
            dpg.get_viewport_width() / 2 - 200, 
            dpg.get_viewport_height() / 2 - 35,
        ])

        self.toastcounter += 1