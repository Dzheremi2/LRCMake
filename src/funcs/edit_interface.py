import flet as ft
from ..classes.lyricField import lyricField
from .export_text_lyrics import get_lyrics

def edit_interface(page, lines_cnt, audioplayer):
    from ..classes.syncModeFAB import syncModeFAB
    text = get_lyrics(page)
    page.remove_at(2)
    page.remove_at(3)
    page.controls[0].actions.pop(2)
    page.controls[0].actions.pop(2)
    page.insert(2, lyricField())
    page.controls[2].value = text
    page.insert(3, syncModeFAB(page, lines_cnt, audioplayer))
    page.scroll = ft.ScrollMode.ALWAYS
    page.update()
