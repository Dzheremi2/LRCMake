import flet as ft
from ..funcs.handlers import change_handler

class menu(ft.NavigationDrawer):
    def __init__(self, page):
        super().__init__()

        self.controls = [
            ft.Container(
                height=12
            ),
            ft.NavigationDrawerDestination(
                label="Lyrics mode",
                icon=ft.icons.LYRICS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.LYRICS_ROUNDED)
            ),
            ft.NavigationDrawerDestination(
                label="Publish mode",
                icon=ft.icons.CLOUD_UPLOAD_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.CLOUD_UPLOAD_ROUNDED)
            ),
            ft.Divider(
                thickness=2
            ),
            ft.NavigationDrawerDestination(
                label="About app",
                icon=ft.icons.ASSIGNMENT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ASSIGNMENT_ROUNDED)
            )
        ]
        self.on_change = lambda e: change_handler(page, self.selected_index, self)
