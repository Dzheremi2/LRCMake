import flet as ft
from ..funcs.edit_interface import edit_interface

class editModeFAB(ft.FloatingActionButton):
    def __init__(self, page, lines_cnt, audioplayer):
        super().__init__()

        self.icon = ft.icons.ARROW_BACK_ROUNDED
        # self.text = "Edit Mode"
        self.mini = True
        self.enable_feedback = True
        self.on_click = lambda _: edit_interface(page, lines_cnt, audioplayer)