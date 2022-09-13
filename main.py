import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


TMP_FILE_NAME = 'current.mp3'
INPUT_FILE_NAME = 'text.txt'
DEFAULT_LANG = 'ru'


def show_text(text):
    command = f'echo "{text}" | boxes -d girl'
    os.system(command)


def say(text, separator='/'):
    lang = DEFAULT_LANG
    if separator in text:
        text, lang = text.split(separator)
    print('language - >', lang)
    tts = gTTS(text, lang=lang)
    tts.save(TMP_FILE_NAME)
    sound = AudioSegment.from_file(TMP_FILE_NAME)
    play(sound)


with open(INPUT_FILE_NAME, 'r', encoding='utf-8') as f:
    for line in f:
        text = line.replace('\n', '')
        if text:
            input()
            show_text(text)
            say(text)

while True:
    text = input()
    if text:
        show_text(text)
        say(text)
    else:
        break



