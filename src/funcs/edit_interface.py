import flet as ft
from ..classes.lyricField import lyricField

def edit_interface(page, lines_cnt):
    from ..classes.syncModeFAB import syncModeFAB
    page.remove_at(2)
    page.remove_at(2)
    page.insert(2, lyricField())
    page.insert(3, syncModeFAB(page, lines_cnt))
    page.scroll = ft.ScrollMode.AUTO
    page.update()
