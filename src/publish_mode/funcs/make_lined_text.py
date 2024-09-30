import re
import flet as ft
from ...variables import Variables

def split_text_on_lines(page):
    list = ((page.controls[2].tabs[0].content.value).splitlines())
    list.append("")
    return list

def make_plain_text(lyrics, page):
    if page.controls[2].tabs[1].content.controls[0].value == "":
        pattern = r'\[.*?\] '
        plain_lyrics = []
        for string in lyrics:
            plain_lyrics.append(re.sub(pattern, "", string))
        Variables.plain_lyrics = plain_lyrics
        print("\n".join(plain_lyrics))
        page.controls[2].tabs[1].content.controls[0].value = "\n".join(plain_lyrics)
        page.update()
    else:
        page.snack_bar = ft.SnackBar(ft.Text("Import failed. Plain text field is not empty"))
        page.snack_bar.open = True
        page.update()

def save_synced_lyrics_for_publish(page):
    Variables.synced_lyrics = page.controls[2].tabs[0].content.value