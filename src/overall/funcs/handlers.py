from ...publish_mode.publish_page import publish_page

def change_handler(page, index, drawer):
    if index == 1:
        publish_page(page, drawer)
    elif index == 2:
        pass