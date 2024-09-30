import flet as ft
from .classes.pbAppbar import pbAppbar
from .classes.dataBlock import dataBlock
from .classes.lyricsMode import lyricsTabs

def publish_page(page, drawer):
    page.close(drawer)
    page.overlay.clear()
    page.controls.clear()
    page.add(pbAppbar(page, drawer))
    page.add(dataBlock(data=None))
    page.add(lyricsTabs())
    page.update()