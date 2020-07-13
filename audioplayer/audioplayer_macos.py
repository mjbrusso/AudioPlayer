from .abstractaudioplayer import AbstractAudioPlayer
from AppKit import NSSound
from time import sleep


class AudioPlayerMacOS(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)

    def _do_load_player(self):
        return NSSound.alloc().initWithContentsOfFile_byReference_(self._filename, True)

    def _get_duration(self):
        return self._player.duration()

    def _get_position(self):
        return self._player.currentTime()

    def _set_position(self, pos):
        return self._player.setCurrentTime(pos)

    def _set_volume(self, value):
        self._player.setVolume_(value / 100.0)              # 0.0..1.0

    def _doplay(self, loop=False, block=False):
        self._player.setLoops_(loop)
        self._player.play()
        while block:
            sleep(self._player.duration())
            block = loop # block && loop = infinite loop!!!!

    def _dopause(self):
        self._player.pause()

    def _doresume(self):
        self._player.resume()

    def _dostop(self):
        self._player.stop()

    def _doclose(self):
        self._player.stop()

    # https://github.com/elvis-epx/paimorse/blob/master/morse/audio_nsaudio.py