import flet as ft
from ..funcs.make_lined_text import make_plain_text, split_text_on_lines, save_synced_lyrics_for_publish

class lyricsTabs(ft.Tabs):
    def __init__(self, page):
        super().__init__()

        self.animation_duration = 300
        self.tab_alignment = ft.TabAlignment.FILL
        self.padding = ft.Padding.top = 10
        self.indicator_padding = 5
        self.tabs = [
            ft.Tab(
                text="Synced Lyrics",
                content=ft.TextField(
                    label="Paste synced lyrics here",
                    icon=ft.icons.LYRICS_ROUNDED,
                    multiline=True,
                    border_color=ft.colors.SECONDARY,
                    on_change= lambda _: save_synced_lyrics_for_publish(page)
                )
            ),
            ft.Tab(
                text="Plain Lyrics",
                content=ft.Column(
                    controls = [
                        ft.TextField(
                            label="Paste plain lyrics here or import it from synced",
                            icon=ft.icons.TEXT_SNIPPET,
                            prefix = ft.IconButton(icon=ft.icons.IMPORT_EXPORT_ROUNDED, tooltip="Import from synced lyrics", on_click=lambda _: make_plain_text(split_text_on_lines(page), page)),
                            multiline=True,
                            border_color=ft.colors.SECONDARY,
                            on_change=lambda _: save_synced_lyrics_for_publish(page)
                        )
                    ],
                    expand=True
                )
            )
        ]