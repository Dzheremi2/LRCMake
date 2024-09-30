import flet as ft
from ..funcs.music import play_music
from ..funcs.sync_funcs import reset_lyrics
from ..variables import Variables

class appbar(ft.AppBar):
    def __init__(self, audioplayer, page, drawer):
        super().__init__()

        self.title = ft.Text("LRCMake")
        self.bgcolor = ft.colors.ON_PRIMARY
        self.title_text_style = ft.TextStyle(font_family="Google Sans", size=20, weight=ft.FontWeight.W_400)
        self.actions = [
            ft.IconButton(icon=ft.icons.PLAY_CIRCLE_OUTLINED, tooltip="Force play audio", on_click=lambda _: play_music(audioplayer)),
            ft.IconButton(icon=ft.icons.RESTART_ALT, tooltip="Reset Lyrics", on_click=lambda _: reset_lyrics(page))

        ]
        self.leading = ft.IconButton(icon=ft.icons.MENU_ROUNDED, tooltip="Open menu", on_click= lambda _: page.open(drawer))