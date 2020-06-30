from abc import ABC, abstractmethod
import os
import sys


class AudioPlayerError(Exception):
    """Basic exception for errors raised by Player"""
    pass


class AbstractAudioPlayer(ABC):
    """
    Abstract Base Class (ABC) for AudioPlayer,
    Must create a subclass for every platform.
    """
    @abstractmethod
    def __init__(self, filename):
        """
        Only store filename and fullfilename.
        The actual player is lazy loaded - created in the first call to .play() 
        """
        self._player = None         # Lazy loaded
        self._filename = filename   # The file name as provided
        self._volume = 100          # 100%
        if not os.path.sep in filename:
            self._fullfilename = os.path.join(
                os.getcwd(), filename)  # Full file name (with path)
        else:
            self._fullfilename = os.path.abspath(filename)
        if not os.path.exists(self._fullfilename):
            raise FileNotFoundError(
                'File does not exist: "{}"'.format(self._fullfilename))

    def __del__(self):
        """
        Stops the player when the object gets destroyed.
        """
        if not self._player is None:
            self.close()

    # region Properties

    @property
    def filename(self):
        """
        The file name as provided in the constructor.
        """
        return self._filename

    @property
    def fullfilename(self):
        """
        Full file name with full path.
        """
        return self._fullfilename

    @property
    def volume(self):
        """

        Gets or sets the current volume (in %) of the audio (0 — 100))

        :type: int
        """
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = max(min(value, 100), 0)  # clamp to [0..100]
        if not self._player is None:
            self._do_setvolume(value)

    @abstractmethod
    def _do_setvolume(self, value):
        """
        Platform dependent code to setting volume.
        """
        pass

    # endregion Properties

    # region Methods
    @abstractmethod
    def _load_player(self):
        """
        Platform dependent code
        """
        pass

    def load_player(self):
        player = self._load_player()
        if player is None:
            raise AudioPlayerError(
                'Error loading player for file "{}"'.format(self._fullfilename))
        return player

    @abstractmethod
    def _doplay(self, loop=False, block=False):
        """
        Platform dependent code
        """
        pass

    def play(self, loop=False, block=False):
        """
        Starts audio playback.
            - loop:  bool – Sets whether to repeat the track automatically when finished.
            - block: bool – If true, blocks the thread until playback ends.
        """
        if self._player is None:                     # Lazy loading
            self._player = self.load_player()

        self._do_setvolume(self._volume)
        self._doplay(loop, block)

    @abstractmethod
    def _dopause(self):
        """
        Platform dependent code
        """
        pass

    def pause(self):
        """
        Pauses audio playback.
        """
        if not self._player is None:
            self._dopause()

    @abstractmethod
    def _doresume(self):
        """
        Platform dependent code
        """
        pass

    def resume(self):
        """
        Resumes audio playback.
        """
        if not self._player is None:
            self._doresume()

    @abstractmethod
    def _dostop(self):
        """
        Platform dependent code
        """
        pass

    def stop(self):
        """
        Stops audio playback. Can play again.
        """
        if not self._player is None:
            self._dostop()

    @abstractmethod
    def _doclose(self):
        """
        Platform dependent code
        """
        pass

    def close(self):
        """
        Closes device, releasing resources. Can't play again.
        """
        if not self._player is None:
            self._doclose()
            self._player = None

    # endregion Methods
