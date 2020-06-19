from enum import Enum
from abc import ABC, abstractmethod


class AbstractAudioPlayer(ABC):
    class States(Enum):
        STOPPED = 0
        PLAYING = 1
        PAUSED = 2

    def __init__(self, filename):
        self._filename = filename
        self._state = AbstractAudioPlayer.States.STOPPED
        self._loop = False
        self._block = False

    def state(self):
        return self._state

    def _set_state(self, newstate):
        self._state = newstate

    @abstractmethod
    def _do_play(self, loop=False, block=False):
        pass

    def play(self, loop=False, block=False):
        self._loop = loop
        self._block = block
        self._state = AbstractAudioPlayer.States.PLAYING
        self._do_play(loop, block)

    @abstractmethod
    def _do_pause(self):
        pass

    def pause(self):
        self._state = AbstractAudioPlayer.States.PAUSED
        self._do_pause()

    @abstractmethod
    def _do_resume(self):
        pass

    def resume(self):
        self._state = AbstractAudioPlayer.States.PLAYING
        self._do_resume()

    @abstractmethod
    def _do_stop(self):
        pass

    def stop(self):
        self._state = AbstractAudioPlayer.States.STOPPED
        self._do_stop()
