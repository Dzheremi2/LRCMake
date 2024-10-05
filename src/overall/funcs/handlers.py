from ...publish_mode.publish_page import publish_page
from ...lyrics_mode.lyrics_page import lyrics_page
from ...about_mode.about_page import about_page

def change_handler(page, index, drawer):
    if index == 1:
        publish_page(page, drawer)
    elif index == 0:
        lyrics_page(page, drawer)
    elif index == 2:
        about_page(page, drawer)