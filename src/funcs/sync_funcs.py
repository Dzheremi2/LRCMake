import re
from ..variables import Variables
from .timing_parser import get_ms
from .music import seek_to_ms

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

def rew_100_ms(page, audioplayer):
    pattern = r'\[([^\[\]]+)\]'
    if get_ms(page) >= 100: # Checks if current timing more than 100ms to prevent going to negative numbers
        timing = get_ms(page) - 100
        new_prefix = f"{timing // 60000:02d}:{(timing % 60000) // 1000:02d}.{timing % 1000:03d}"
        replacement = fr'[{new_prefix}]'
        page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value = re.sub(pattern, replacement, page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value)
        seek_to_ms(audioplayer, timing)
        print(f"seeked to {new_prefix}")
    else: # Sets to 00:00.000 if less than 100ms
        replacement = fr'[00:00.000]'
        page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value = re.sub(pattern, replacement, page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value)
        seek_to_ms(audioplayer, 0)
        print(f"seeked to [00:00.000]")

def forw_100_ms(page, audioplayer):
    pattern = r'\[([^\[\]]+)\]'
    timing = get_ms(page) + 100
    new_prefix = f"{timing // 60000:02d}:{(timing % 60000) // 1000:02d}.{timing % 1000:03d}"
    replacement = fr'[{new_prefix}]'
    page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value = re.sub(pattern, replacement, page.controls[2].controls[Variables.current_sync_row].controls[0].controls[0].controls[0].value)
    seek_to_ms(audioplayer, timing)
    print(f"seeked to {new_prefix}")