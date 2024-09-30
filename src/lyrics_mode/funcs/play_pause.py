import flet as ft
from .music import pause_music, resume_music

def update_state_pause(page, audioplayer):
    page.controls[1].controls[0].controls[0].trailing = ft.IconButton(
        icon=ft.icons.PAUSE_ROUNDED, bgcolor=ft.colors.PRIMARY_CONTAINER, tooltip="Play/Pause", on_click=lambda _: (pause_music(audioplayer), update_state_play(page, audioplayer))
    )
    page.update()

def update_state_play(page, audioplayer):
    page.controls[1].controls[0].controls[0].trailing = ft.IconButton(
        icon=ft.icons.PLAY_ARROW_ROUNDED, bgcolor=ft.colors.PRIMARY_CONTAINER, tooltip="Play/Pause", on_click=lambda _: (resume_music(audioplayer), update_state_pause(page, audioplayer))
    )
    page.update()