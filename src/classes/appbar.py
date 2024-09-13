import flet as ft

class appbar(ft.AppBar):
    def __init__(self):
        super().__init__()

        self.title = ft.Text("LRCMake")
        self.bgcolor = ft.colors.ON_PRIMARY
        self.title_text_style = ft.TextStyle(font_family="Google Sans", size=20, weight=ft.FontWeight.W_400)
        self.actions = [
            ft.IconButton(icon=ft.icons.RESTART_ALT, tooltip="Reset Lyrics")
        ]