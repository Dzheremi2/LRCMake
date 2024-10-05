import flet as ft
from .classes.pbAppbar import pbAppbar
from .classes.dataBlock import dataBlock
from .classes.lyricsMode import lyricsTabs
from .classes.publishFAB import publishFAB
from .funcs.filework import update_data

def publish_page(page, drawer):
    page.close(drawer)
    page.overlay.clear()
    page.controls.clear()
    file_picker = ft.FilePicker(on_result= lambda e: update_data(page, e.files[0].path))
    page.overlay.append(file_picker)
    page.add(pbAppbar(page, drawer))
    page.add(dataBlock(file_picker))
    page.add(lyricsTabs(page))
    page.add(publishFAB(page))
    page.update()