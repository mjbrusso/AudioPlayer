from .abstractaudioplayer import AbstractAudioPlayer
from AppKit import NSSound
from time import sleep


class AudioPlayerMacOS(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        # self._url = NSURL.URLWithString_('file://{}'.format(self._filename))
        # or ? self._url = NSURL.fileURLWithPath_(sound)    # this seems to work

    def _load_player(self):
        return NSSound.alloc().initWithContentsOfFile_byReference_(self._filename, True)

    def _do_setvolume(self, value):
        self._player.volume = value / 100.0              # 0.0..1.0

    def _doplay(self, loop=False, block=False):
        self._player.loops = loop
        self._player.play()
        while block and self._player.isPlaying():
            sleep(0.2)

    def _dopause(self):
        self._player.pause()

    def _doresume(self):
        self._player.resume()

    def _dostop(self):
        self._player.stop()

    def _doclose(self):
        self._player.stop()