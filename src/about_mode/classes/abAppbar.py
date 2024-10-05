import flet as ft

class abAppbar(ft.AppBar):
    def __init__(self, page, drawer):
        super().__init__()

        self.title = ft.Text("About")
        self.bgcolor = ft.colors.ON_PRIMARY
        self.title_text_style = ft.TextStyle(font_family="Google Sans", size=20, weight=ft.FontWeight.W_400)
        self.leading = ft.IconButton(icon=ft.icons.MENU_ROUNDED, tooltip="Open menu", on_click= lambda _: page.open(drawer))