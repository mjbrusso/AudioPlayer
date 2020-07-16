from .abstractaudioplayer import AbstractAudioPlayer, AudioPlayerError, State
from ctypes import windll, create_unicode_buffer


class AudioPlayerWindows(AbstractAudioPlayer):
    def __init__(self, filename, callback=None):
        super().__init__(filename, callback)
        self._alias = "A{}".format(id(self))
        self._buffer = create_unicode_buffer(255)

    def _mciSendString(self, command):
        result = windll.winmm.mciSendStringW(command, self._buffer, 255, 0)
        return result, self._buffer.value or ""

    def _do_load_player(self):
        ret, _a = self._mciSendString('open "{}" type mpegvideo alias {}'.format(self._filename, self._alias))
        ret = int(ret)
        if ret > 0:
            raise AudioPlayerError( 'Failed to play "{}"'.format(self.fullfilename))
        self._mciSendString('set {} time format ms'.format(self._alias))
        return ret

    def _get_duration(self):
        _, length = self._mciSendString('status {} length'.format(self._alias))
        return float(length or 0) / 1000

    def _get_position(self):
        _, position = self._mciSendString('status {} position'.format(self._alias))
        return float(position or 0) / 1000

    def _set_position(self, pos):
        pos = int(float(pos) * 1000)
        if True or self.state == State.PLAYING:
            self._mciSendString('play {} from {}'.format(self._alias, pos))
            if self.state == State.PAUSED:
                self._dopause()
        else:
            self._mciSendString('seek {} to {}'.format(self._alias, pos))

    def _set_volume(self, value):
        value = int(value * 10)  # MCI volume: 0...1000
        self._mciSendString(
            'setaudio {} volume to {}'.format(self._alias, value))

    def _doplay(self, loop=False, block=False):
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
        self._mciSendString('seek {} to 0'.format(self._alias))

    def _doclose(self):
        self._mciSendString('close {}'.format(self._alias))

# https://stackoverflow.com/questions/5249903/receiving-wm-copydata-in-python