from abstractaudioplayer import AbstractAudioPlayer
from ctypes import windll


class AudioPlayer(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        self._alias = "A{}".format(id(self))

    def _mciSendString(self, command):
        return windll.winmm.mciSendStringW(command, 0, 0, 0)

    def _load_player(self):
        return self._mciSendString('open "{}" alias {}'.format(self._filename, self._alias))

    def _doplay(self, loop=False, block=False):
        sloop = 'repeat' if loop else ''
        swait = 'wait' if block else ''
        self._mciSendString('play {} {} {}'.format(
            self._alias, sloop, swait))

    def _dopause(self):
        self._mciSendString('pause {}'.format(self._alias))

    def _doresume(self):
        self._mciSendString('resume {}'.format(self._alias))

    def _dostop(self):
        self._mciSendString('close {}'.format(self._alias))
