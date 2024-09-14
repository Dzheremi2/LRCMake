import flet as ft
from ..funcs.music import play_music, seek_to
from ..funcs.play_pause import update_state_pause

class playerBlock(ft.Row):
    def __init__(self, now_playing, file_picker, audioplayer, page):
        super().__init__()

        self.controls = [
            ft.Column(
                controls=[
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.AUDIOTRACK),
                        title=ft.Text(f"{'Select file' if now_playing == None else now_playing['artist']}", font_family="Google Sans", size=17),
                        subtitle=ft.Text(f"{'Click' if now_playing == None else now_playing['track']}", font_family="Google Sans"),
                        trailing=ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, bgcolor=ft.colors.PRIMARY_CONTAINER, tooltip="Play/Pause", on_click=lambda _: (play_music(audioplayer), update_state_pause(page, audioplayer))),
                        on_click=lambda _: file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.AUDIO)
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
                                    max=100 if now_playing == None else now_playing['duration'] / 1000,
                                    on_change_end=lambda e: seek_to(audioplayer, int(float(e.data)))
                                ), expand=True
                            )
                        ]
                    )
                ]
            )
        ]
        self.wrap = True