import flet as ft
from ..funcs.sync_funcs import get_timing_string, make_line

class makeSyncFAB(ft.FloatingActionButton):
    def __init__(self, audioplayer, page):
        super().__init__()

        self.icon = ft.icons.LYRICS_ROUNDED
        self.text = "Sync Line"
        self.enable_feedback = True
        self.on_click = lambda _: make_line(get_timing_string(audioplayer), page)