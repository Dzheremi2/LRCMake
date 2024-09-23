import eyed3
from pydub import AudioSegment
from .timing_parser import get_ms

def play_music(audioplayer):
    audioplayer.play()

def pause_music(audioplayer):
    audioplayer.pause()

def resume_music(audioplayer):
    audioplayer.resume()

def seek_to(audioplayer, timing):
    audioplayer.seek(timing * 1000)

def seek_to_ms(audioplayer, timing):
    audioplayer.seek(timing)

def change_src(audioplayer, page, songFile):
    print(songFile)
    audioplayer.src = songFile
    audioplayer.play()
    page.update()

def get_track_info(songFile, now_playing):
    audiofile = eyed3.load(songFile)
    sound = AudioSegment.from_file(songFile)
    now_playing = {}
    now_playing['artist'] = audiofile.tag.artist
    now_playing['track'] = audiofile.tag.title
    now_playing['duration'] = len(sound)
    return now_playing

def get_duration(songFile):
    sound = AudioSegment.from_file(songFile)
    return (len(sound) // 1000) + 1

def update_track_info(now_playing, page):
    page.controls[1].controls[0].controls[0].title.value = now_playing['track']
    page.controls[1].controls[0].controls[0].subtitle.value = now_playing['artist']
    page.controls[1].controls[0].controls[1].controls[0].value = f"{now_playing['duration'] // 60000:02d}:{(now_playing['duration'] % 60000) // 1000:02d}"
    page.update()

def replay_line(page, audioplayer):
    timing = get_ms(page)
    seek_to_ms(audioplayer, timing)