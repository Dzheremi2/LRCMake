import flet as ft
from ..funcs.sync_funcs import rew_100_ms, forw_100_ms
from ..funcs.music import replay_line

class bottomControls(ft.BottomAppBar):
    def __init__(self, page, audioplayer):
        super().__init__()

        self.bgcolor = ft.colors.PRIMARY_CONTAINER
        self.shape = ft.NotchShape.AUTO
        self.height = 70

        self.content = ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.FAST_REWIND_ROUNDED, tooltip="Sync 100ms back", on_click=lambda _: rew_100_ms(page, audioplayer)),
                ft.IconButton(icon=ft.icons.FAST_FORWARD_ROUNDED, tooltip="Sync 100ms forward", on_click=lambda _: forw_100_ms(page, audioplayer)),
                ft.IconButton(icon=ft.icons.REPLAY_ROUNDED, tooltip="Replay selected line", on_click=lambda _: replay_line(page, audioplayer))
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=2
        )