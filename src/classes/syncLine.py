import flet as ft

class syncLine(ft.Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            ft.Row(
                controls= [
                    ft.TextField(
                        multiline=False,
                        border_color=ft.colors.SECONDARY
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
                ], wrap=True
            )
        ]