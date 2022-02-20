from gtts import gTTS
from playsound import playsound
import json
import os


def get_dict(item):
    with open(item) as f:
        D = json.load(f)
    return D


def play(x):
    playsound(x)


def write_mp3(D, item):
    for key, value in D.items():
        sk = gTTS(key, lang='en')
        sv = gTTS(value, lang='ru')
        with open(item.replace('.json', '.mp3'), 'wb') as f:
            sv.write_to_fp(f)
            sk.write_to_fp(f)
    return item.replace('.json', '.mp3')


def main():
    for item in os.listdir():
        if item.endswith('.json'):
            D = get_dict(item)
            lesson = write_mp3(D, item)
            play(lesson)


if __name__ == '__main__':
    main()