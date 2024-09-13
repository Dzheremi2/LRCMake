import flet as ft
from ..funcs.sync_interface import sync_interface

class syncModeFAB(ft.FloatingActionButton):
    def __init__(self, page, lines_cnt):
        super().__init__()

        self.icon = ft.icons.TEXT_SNIPPET
        self.text = "Sync Mode"
        self.enable_feedback = True
        self.on_click = lambda event: sync_interface(page, lines_cnt)
        self.tooltip = 'Enter "Sync Lyrics" mode'