import flet as ft
from ..classes.syncLine import syncLine
from ..classes.editModeFAB import editModeFAB

def sync_interface(page, lines_cnt):
    lines_column = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    for i in range(lines_cnt):
        lines_column.controls.append(ft.Row(controls=[syncLine()],expand=True))
    page.remove_at(2)
    page.remove_at(2)
    page.insert(2, lines_column)
    page.insert(3, editModeFAB(page, lines_cnt))
    page.scroll = None
    page.update()