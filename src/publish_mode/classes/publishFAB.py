import flet as ft
from ..funcs.publish import publish
from ...variables import variables

class publishFAB(ft.FloatingActionButton):
    def __init__(self, page):
        super().__init__()

        self.icon = ft.icons.PUBLISH_ROUNDED
        self.text = "Publish to LRCLIB"
        self.enable_feedback = True
        self.on_click = lambda _: publish(variables.metadata, page)