import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


TMP_FILE_NAME = 'current.mp3'
INPUT_FILE_NAME = 'text.txt'


def show_text(text):
    command = f'echo "{text}" | boxes -d girl'
    os.system(command)


def say(text):
    tts = gTTS(text, lang='ru')
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



