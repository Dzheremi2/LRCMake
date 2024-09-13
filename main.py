import flet as ft
from src.classes.appbar import appbar
from src.classes.lyricField import lyricField
from src.classes.playerBlock import playerBlock
from src.classes.syncModeFAB import syncModeFAB

# Main Music Variable
now_playing = None

#Main Function
def main(page: ft.Page):
    #App Theming
    page.title = "LRCMake"
    page.scroll = ft.ScrollMode.AUTO
    page.theme = page.dark_theme = ft.Theme(use_material3=True, color_scheme_seed="green")
    page.fonts = {
        "Google Sans": "https://raw.githubusercontent.com/hprobotic/Google-Sans-Font/master/GoogleSans-Regular.ttf",
    }

# TODO: Logic based on string splitting
    def report_inside(args):
        print((lyricField.value).splitlines())

    #Building interface
    page.add(appbar())
    page.add(playerBlock(now_playing))
    page.add(lyricField())
    page.add(syncModeFAB(page, 20))


ft.app(target=main, assets_dir="assets")
