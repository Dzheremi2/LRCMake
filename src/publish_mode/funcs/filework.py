import flet as ft
import eyed3
import base64
from pydub import AudioSegment
from ...variables import variables

def update_data(page, file):
    audiofile = eyed3.load(file)
    sound = AudioSegment.from_file(file)
    variables.metadata = {}
    variables.metadata['artist'] = audiofile.tag.artist
    variables.metadata['track'] = audiofile.tag.title
    variables.metadata['album'] = audiofile.tag.album
    variables.metadata['duration_s'] = len(sound) // 1000
    variables.metadata['duration'] = f"{variables.metadata['duration_s'] // 60}:{variables.metadata['duration_s'] % 60:02d}"
    variables.metadata['cover'] = audiofile.tag.images[0].image_data
    page.controls[1].controls[0].title.value = variables.metadata['track']
    page.controls[1].controls[0].subtitle.value = variables.metadata['artist']
    page.controls[1].controls[0].trailing.controls[0].value = variables.metadata['duration']
    page.controls[1].controls[0].trailing.controls[1].value = str(variables.metadata['duration_s'])
    page.controls[1].controls[0].leading.src_base64 = base64.b64encode(variables.metadata['cover']).decode('utf-8')
    page.update()