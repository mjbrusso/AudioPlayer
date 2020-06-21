from audioplayer import AudioPlayer
import os

mp3 = os.path.join(os.path.dirname(__file__), "smooth.mp3") # ringtone by felipebbrusso

p = AudioPlayer(mp3)

print("Playing {} in loop".format(p.fullfilename))
p.play(block=False, loop=True)

input("Press Enter to pause")
p.pause()

input("Press Enter to resume")
p.resume()

input("Press Enter to stop")
p.stop()

input("Press Enter to play once")
p.play(block=True)
