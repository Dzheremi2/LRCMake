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
                        label=f"Line {i+1}",
                        value=string,
                        on_focus=lambda e: get_current_sync_row(int(e.control.key)),
                        expand=True,
                        key=i
                    )
                ]
            )
        ]
        self.expand=True