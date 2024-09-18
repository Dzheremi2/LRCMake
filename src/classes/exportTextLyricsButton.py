import flet as ft
from ..funcs.export_text_lyrics import to_clipboard

class exportTextLyrcis(ft.IconButton):
    def __init__(self, page):
        super().__init__()

        self.icon = ft.icons.LYRICS_OUTLINED
        self.enable_feedback = True
        self.tooltip = "Export synced lyrics to clipboard"
        self.on_click = lambda _: to_clipboard(page)