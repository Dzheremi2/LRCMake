import flet as ft

class playerBlock(ft.Row):
    def __init__(self, now_playing):
        super().__init__()

        self.controls = [
            ft.Column(
                controls=[
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.AUDIOTRACK),
                        title=ft.Text(f"{'Select file' if now_playing == None else now_playing['artist']}", font_family="Google Sans", size=17),
                        subtitle=ft.Text(f"{'Click' if now_playing == None else now_playing['track']}"),
                        trailing=ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, bgcolor=ft.colors.PRIMARY_CONTAINER, tooltip="Play/Pause")
                    ),
                    ft.Row(
                        controls= [
                            ft.Text(
                                f"{'00:00' if now_playing == None else now_playing['duration']}",
                                font_family="Google Sans",
                                size=17
                            ),
                            ft.Container(
                                content=ft.Slider(
                                    max=100 if now_playing == None else now_playing['duration'] / 1000
                                ), expand=True
                            )
                        ]
                    )
                ]
            )
        ]
        self.wrap = True