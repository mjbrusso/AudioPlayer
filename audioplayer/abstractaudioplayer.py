from abc import ABC, abstractmethod


class AbstractAudioPlayer(ABC):

    def __init__(self, filename):
        self._filename = filename

    @abstractmethod
    def _do_play(self, loop=False, block=False):
        pass

    def play(self, loop=False, block=False):
        self._do_play(loop, block)

    @abstractmethod
    def _do_pause(self):
        pass

    def pause(self):
        self._do_pause()

    @abstractmethod
    def _do_resume(self):
        pass

    def resume(self):
        self._do_resume()

    @abstractmethod
    def _do_stop(self):
        pass

    def stop(self):
        self._do_stop()
