import flet as ft
import requests
import hashlib
from binascii import unhexlify
from ..classes.publishAlert import publishAlert
from ...variables import variables

def verify_nonce(result, target):
    if len(result) != len(target):
        return False

    for i in range(len(result)):
        if result[i] > target[i]:
            return False
        elif result[i] < target[i]:
            break

    return True

def solve_challenge(prefix, target_hex):
    target = unhexlify(target_hex.upper())
    nonce = 0

    while True:
        input_data = f"{prefix}{nonce}".encode()
        hashed = hashlib.sha256(input_data).digest()

        if verify_nonce(hashed, target):
            break
        else:
            nonce += 1

    return str(nonce)

def publish(metadata, page):
    challenge_data = requests.post(url="https://lrclib.net/api/request-challenge")
    challenge_data_json = challenge_data.json()
    print(challenge_data_json)
    nonce = solve_challenge(prefix=challenge_data_json['prefix'], target_hex=challenge_data_json['target'])
    print(f"X-Publish-Token: {challenge_data_json['prefix']}:{nonce}")
    response = requests.post(url="https://lrclib.net/api/publish", headers={"X-Publish-Token": f"{challenge_data_json['prefix']}:{nonce}", "Content-Type": "application/json"}, params={'keep_headers': 'true'}, json={
        "trackName": metadata['track'],
        "artistName": metadata['artist'],
        "albumName": metadata['album'],
        "duration": metadata['duration_s'],
        "plainLyrics": "\n".join(variables.plain_lyrics),
        "syncedLyrics": variables.synced_lyrics
    })

    if response.status_code == 201:
        page.open(publishAlert(page, "Exit code: 201", "Lyrics published successfully"))
    elif response.status_code == 400:
        page.open(publishAlert(page, "Exit code: 400", "Incorrect public token"))
    else:
        page.open(publishAlert(page, "Exit code: None", "Unknown error occured"))