from abc import ABC, abstractmethod
import os
import sys


class AbstractAudioPlayer(ABC):
    @abstractmethod
    def __init__(self, filename):
        self._player = None         # Lazy loaded
        if not '/' in filename:
            self._filename = os.path.join(os.getcwd(), filename)
        else:
            self._filename = os.path.abspath(filename)

    def __del__(self):
        self.stop()
        self._player = None

    @abstractmethod
    def _load_player(self):
        pass

    @abstractmethod
    def _doplay(self, loop=False, block=False):
        pass

    def play(self, loop=False, block=False):
        if self._player is None:                     # Lazy loading
            self._player = self._load_player()

        self._doplay(loop, block)

    @abstractmethod
    def _dopause(self):
        pass

    def pause(self):
        self._dopause()

    @abstractmethod
    def _doresume(self):
        pass

    def resume(self):
        self._doresume()

    @abstractmethod
    def _dostop(self):
        pass

    def stop(self):
        self._dostop()
