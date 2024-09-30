import flet as ft

class lyricsTabs(ft.Tabs):
    def __init__(self):
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
                    border_color=ft.colors.SECONDARY
                )
            ),
            ft.Tab(
                text="Plain Lyrics",
                content=ft.TextField(
                    label="Paste plain lyrics here or import it from synced",
                    icon=ft.icons.TEXT_SNIPPET,
                    multiline=True,
                    border_color=ft.colors.SECONDARY
                )
            )
        ]