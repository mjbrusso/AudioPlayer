from audioplayer import AudioPlayer
import os

for fmt in ('mp3', 'ogg', 'wav', 'mid'):
    soundfile = 'Orient Theme.' + fmt  # https://opengameart.org/content/orient-theme-jingle
    file = os.path.join(os.path.dirname(__file__), 'audio',  soundfile) 
    p = AudioPlayer(file)
    input('Press ENTER to play {} file: {}'.format(fmt, soundfile))
    p.play(block=True, loop=False)


