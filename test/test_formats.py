from audioplayer import AudioPlayer
import os

for fmt in ('mp3', 'ogg', 'wav', 'mid'):
    # https://opengameart.org/content/orient-theme-jingle
    soundfile = 'Orient Theme.' + fmt
    file = os.path.join(os.path.dirname(__file__), 'audio',  soundfile)
    try:
        p = AudioPlayer(file)
        print('Playing {} file: {}'.format(fmt, soundfile))
        p.play(block=True)
    except Exception as e:
        print(e)
