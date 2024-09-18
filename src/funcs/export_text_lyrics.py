def to_clipboard(page):
    lyrics = ''
    for i in range(len(page.controls[2].controls)):
        lyrics = lyrics + f'{page.controls[2].controls[i].controls[0].controls[0].controls[0].value}\n'
    lyrics = lyrics[:-2]
    page.set_clipboard(lyrics)