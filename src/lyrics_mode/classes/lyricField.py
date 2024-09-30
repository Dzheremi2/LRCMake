import flet as ft

class lyricField(ft.TextField):
    def __init__(self):
        super().__init__()

        self.label = "Input Lyrics Text Here"
        self.icon = ft.icons.TEXT_SNIPPET
        self.multiline = True
        self.border_color = ft.colors.SECONDARY