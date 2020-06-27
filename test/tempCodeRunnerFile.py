from audioplayer import AudioPlayer
import os

mp3 = os.path.join(os.path.dirname(__file__), 'audio', 'toquesuave.mp3') # ringtone by felipebbrusso'

p = AudioPlayer(mp3)

print('Playing {} in loop'.format(p.fullfilename))
p.play(block=False, loop=True)