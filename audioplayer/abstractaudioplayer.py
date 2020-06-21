from abc import ABC, abstractmethod
import os
import sys


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
        if not os.path.sep in filename:
            self._fullfilename = os.path.join(
                os.getcwd(), filename)  # Full file name (with path)
        else:
            self._fullfilename = os.path.abspath(filename)

    def __del__(self):
        """
        Stops the player when the object object gets destroyed.
        """
        self.stop()
        self._player = None

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

    # endregion Properties

    # region Methods
    @abstractmethod
    def _load_player(self):
        """
        Create and return the actual, platform dependent, player object.
        """
        pass

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
            self._player = self._load_player()

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
        self._doresume()

    @abstractmethod
    def _dostop(self):
        """
        Platform dependent code
        """
        pass

    def stop(self):
        """
        Stops audio playback.
        """
        self._dostop()

    # endregion Methods
