import flet as ft
from src.overall.classes.sideMenu import menu
from src.lyrics_mode.classes.appbar import appbar
from src.lyrics_mode.classes.lyricField import lyricField
from src.lyrics_mode.classes.playerBlock import playerBlock
from src.lyrics_mode.classes.syncModeFAB import syncModeFAB
from src.lyrics_mode.classes.bottomControls import bottomControls
from src.lyrics_mode.funcs.music import change_src, get_track_info, update_track_info, get_duration, update_current_timing_frontend
from src.lyrics_mode.funcs.play_pause import update_state_pause
from src.lyrics_mode.funcs.slider_postion import update_slider, slider_init

# Main Music Variable Init
now_playing = None

#Main Function
def main(page: ft.Page):
    #App Theming
    page.title = "LRCMake"
    page.scroll = ft.ScrollMode.ALWAYS
    page.theme = page.dark_theme = ft.Theme(use_material3=True, color_scheme_seed="green")
    page.fonts = {
        "Google Sans": "https://raw.githubusercontent.com/hprobotic/Google-Sans-Font/master/GoogleSans-Regular.ttf",
    }

    # Initing invisible parts
    permissions = ft.PermissionHandler()
    file_picker = ft.FilePicker(on_result=lambda e: (change_src(audioplayer, page, songFile=e.files[0].path), update_track_info(get_track_info(songFile=e.files[0].path, now_playing=now_playing), page), slider_init(page, get_duration(e.files[0].path))))
    audioplayer = ft.Audio(on_position_changed=lambda e: (update_slider(page, value=e.position), update_current_timing_frontend(page, timing=e.position)), src="Silence.ogg", volume=0.5, on_duration_changed=lambda e: print(e.data), on_loaded=lambda _: update_state_pause(page, audioplayer))
    page.overlay.append(audioplayer)
    page.overlay.append(file_picker)
    page.overlay.append(permissions)
    page.update()
    # Building interface
    drawer = menu(page)
    page.add(appbar(audioplayer, page, drawer))
    page.add(playerBlock(now_playing, file_picker, audioplayer, page, permissions))
    page.add(lyricField())
    page.add(syncModeFAB(page, 0, audioplayer))
    page.insert(4, bottomControls(page, audioplayer))

ft.app(target=main, assets_dir="assets")
