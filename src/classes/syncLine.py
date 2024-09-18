import flet as ft
from ..funcs.sync_funcs import get_current_sync_row

class syncLine(ft.Column):
    def __init__(self, i, string):
        super().__init__()

        self.controls = [
            ft.Row(
                controls= [
                    ft.TextField(
                        text_size = 12, 
                        read_only = True,
                        multiline=False,
                        border_color=ft.colors.SECONDARY, 
                        label=f"{i}",
                        value=string,
                        on_focus=lambda e: get_current_sync_row(int(e.control.label))
                    ),
                    ft.IconButton(
                        icon=ft.icons.FAST_REWIND_ROUNDED,
                        bgcolor=ft.colors.PRIMARY_CONTAINER,
                        style=ft.ButtonStyle(visual_density=ft.VisualDensity.COMPACT)
                    ),
                    ft.IconButton(
                        icon=ft.icons.FAST_FORWARD_ROUNDED,
                        bgcolor=ft.colors.PRIMARY_CONTAINER,
                        style=ft.ButtonStyle(visual_density=ft.VisualDensity.COMPACT)
                    )
                ]
            )
        ]