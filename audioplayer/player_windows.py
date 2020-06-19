from abstractaudioplayer import AbstractAudioPlayer
from ctypes import windll


class AudioPlayer(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        self._alias = "A{}".format(id(self))
        self._mciSendString('open "{}" alias {}'.format(filename, self._alias))

    def __del__(self):
        self._do_stop()

    def _mciSendString(self, command):
        return windll.winmm.mciSendStringW(command, 0, 0, 0)

    def _do_play(self, loop=False, block=False):
        sloop = 'repeat' if loop else ''
        swait = 'wait' if block else ''
        self._mciSendString('play {} {} {}'.format(
            self._alias, sloop, swait))

    def _do_pause(self):
        self._mciSendString('pause {}'.format(self._alias))

    def _do_resume(self):
        self._mciSendString('resume {}'.format(self._alias))

    def _do_stop(self):
        self._mciSendString('close {}'.format(self._alias))
