import flet as ft
from ..funcs.edit_interface import edit_interface

class editModeFAB(ft.FloatingActionButton):
    def __init__(self, page, lines_cnt):
        super().__init__()

        self.icon = ft.icons.ARROW_BACK_ROUNDED
        self.text = "Edit Mode"
        self.enable_feedback = True
        self.on_click = lambda event: edit_interface(page, lines_cnt)