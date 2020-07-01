from .abstractaudioplayer import AbstractAudioPlayer, AudioPlayerError
from ctypes import windll


class AudioPlayerWindows(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        self._alias = "A{}".format(id(self))

    def _mciSendString(self, command):
        return windll.winmm.mciSendStringW(command, 0, 0, 0)

    def _load_player(self):
        ret = self._mciSendString('open "{}" type mpegvideo alias {}'.format(self._filename, self._alias))
        if ret > 0:
            raise AudioPlayerError( 'Failed to play "{}"'.format(self.fullfilename))
        return ret

    def _do_setvolume(self, value):
        volume = int(value * 10)  # MCI volume: 0...1000
        self._mciSendString(
            'setaudio {} volume to {}'.format(self._alias, volume))

    def _doplay(self, loop=False, block=False):
        """
        Starts audio playback.
            - loop:  bool – Sets whether to repeat the track automatically when finished.
            - block: bool – If true, blocks the thread until playback ends.
        """
        sloop = 'repeat' if loop else ''
        swait = 'wait' if block else ''
        self._mciSendString('play {} from 0 {} {}'.format(
            self._alias, sloop, swait))

    def _dopause(self):
        self._mciSendString('pause {}'.format(self._alias))

    def _doresume(self):
        self._mciSendString('resume {}'.format(self._alias))

    def _dostop(self):
        self._mciSendString('stop {}'.format(self._alias))

    def _doclose(self):
        self._mciSendString('close {}'.format(self._alias))
