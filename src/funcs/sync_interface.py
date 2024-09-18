import flet as ft
from ..classes.syncLine import syncLine
from ..classes.editModeFAB import editModeFAB
from ..classes.makeSyncFAB import makeSyncFAB
from ..classes.exportTextLyricsButton import exportTextLyrcis
from .make_lined_text import split_text_on_lines

def sync_interface(page, lines_cnt, audioplayer):
    lines_column = ft.Column(scroll=ft.ScrollMode.AUTO, height=640)
    for i in range(lines_cnt):
        string = split_text_on_lines(page)[i]
        lines_column.controls.append(ft.Row(controls=[syncLine(i, string)], key=i))
    print(lines_column.controls[3].key)
    page.remove_at(2)
    page.remove_at(2)
    page.insert(2, lines_column)
    page.controls[0].actions.append(exportTextLyrcis(page))
    page.controls[0].actions.append(editModeFAB(page, lines_cnt, audioplayer))
    page.add(makeSyncFAB(audioplayer, page))
    page.scroll = None
    page.update()