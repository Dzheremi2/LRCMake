import flet as ft
from ..classes.lyricField import lyricField

def edit_interface(page, lines_cnt, audioplayer):
    from ..classes.syncModeFAB import syncModeFAB
    page.remove_at(2)
    page.remove_at(2)
    page.controls[0].actions.pop(2)
    page.insert(2, lyricField())
    page.insert(3, syncModeFAB(page, lines_cnt, audioplayer))
    page.scroll = ft.ScrollMode.ALWAYS
    page.update()
