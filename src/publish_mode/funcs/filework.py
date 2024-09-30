import flet as ft
import eyed3
import base64
from pydub import AudioSegment

def update_data(data, page, file):
    audiofile = eyed3.load(file)
    sound = AudioSegment.from_file(file)
    data = {}
    data['artist'] = audiofile.tag.artist
    data['track'] = audiofile.tag.title
    data['album'] = audiofile.tag.album
    data['duration_s'] = len(sound) // 1000
    data['duration'] = f"{data['duration_s'] // 60}:{data['duration_s'] % 60}"
    data['cover'] = audiofile.tag.images[0].image_data
    page.controls[1].controls[0].title.value = data['track']
    page.controls[1].controls[0].subtitle.value = data['artist']
    page.controls[1].controls[0].trailing.controls[0].value = data['duration']
    page.controls[1].controls[0].trailing.controls[1].value = str(data['duration_s'])
    page.controls[1].controls[0].leading.src_base64 = base64.b64encode(data['cover']).decode('utf-8')
    page.update()