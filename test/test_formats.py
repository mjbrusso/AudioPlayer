from audioplayer import AudioPlayer
import os

for fmt in ('mp3', 'wav', 'ogg', 'mid', 'flac', 'wma'): # ringtone by felipebbrusso'
    soundfile = 'toquesuave.' + fmt
    file = os.path.join(os.path.dirname(__file__), 'audio',  soundfile)
    try:
        p = AudioPlayer(file)
        print('Playing {} file: {}'.format(fmt, soundfile))
        p.play(block=True)
    except Exception as e:
        print(e)
