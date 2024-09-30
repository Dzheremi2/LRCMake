import flet as ft
from ..funcs.sync_interface import sync_interface
from ..funcs.make_lined_text import split_text_on_lines_cnt

class syncModeFAB(ft.FloatingActionButton):
    def __init__(self, page, lines_cnt, audioplayer):
        super().__init__()

        self.icon = ft.icons.TEXT_SNIPPET
        self.text = "Sync Mode"
        self.enable_feedback = True
        self.on_click = lambda _: sync_interface(page, split_text_on_lines_cnt(page)+1, audioplayer)
        self.tooltip = 'Enter "Sync Lyrics" mode'