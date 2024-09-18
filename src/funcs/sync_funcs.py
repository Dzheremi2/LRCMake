from ..variables import Variables

def get_timing_string(audioplayer):
    timing = audioplayer.get_current_position()
    return f"[{timing // 60000:02d}:{(timing % 60000) // 1000:02d}.{timing % 1000:03d}] "

def get_current_sync_row(id):
    Variables.current_sync_row = id

def make_line(string, page):
    Variables.current_lyrics_list[Variables.current_sync_row] = string + Variables.current_lyrics_list[Variables.current_sync_row]
    page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value = string + page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value
    try:
        page.controls[2].controls[Variables.current_sync_row+1].controls[0].controls[0].controls[0].focus()
        page.controls[2].scroll_to(key=page.controls[2].controls[Variables.current_sync_row+1].key)
    except IndexError:
        pass
    page.update()