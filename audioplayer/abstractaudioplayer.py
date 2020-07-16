from abc import ABC, abstractmethod
import os
import sys
from enum import Enum


class AudioPlayerError(Exception):
    """Basic exception for errors raised by Player"""
    pass

class PlayMode(Enum):
    ONCE_ASYNC = 0
    LOOP_ASYNC = 1
    ONCE_BLOCKING = 2

class State(Enum):
    STOPPED = 0     # Position at 00:00.0, ready to start playing
    PLAYING = 1     # Playing
    PAUSED = 2      # Paused
    CLOSED = 3      # Can't play again


class AbstractAudioPlayer(ABC):
    """
    Abstract Base Class (ABC) for AudioPlayer,
    Must create a subclass for every platform.
    """
    @abstractmethod
    def __init__(self, filename, callback=None):
        """
        Only store filename and fullfilename.
        The actual player is lazy loaded - created in the first call to .play() 
        """
        self._player = None         # Lazy loaded
        self._filename = filename   # The file name as provided
        self._volume = 100          # 100%
        self._state = State.STOPPED
        self._finish_callback = callback
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
        if self.loaded:
            self.close()

    # region Properties

    @property
    def loaded(self):
        """
        Gets whether the player is already created
        """
        return self._player is not None

    @property
    def filename(self):
        """
        Gets the file name as provided in the constructor.
        """
        return self._filename

    @property
    def fullfilename(self):
        """
        Gets the full file name with full path.
        """
        return self._fullfilename

    @property
    def state(self):
        """
        Gets the current state
        """
        return self._state

    @abstractmethod
    def _get_duration(self):
        """
        Platform dependent code to get duration.
        """
        pass

    @property
    def duration(self):
        """
        Gets the duration of the track, in seconds.
        """
        return self._get_duration()

    @abstractmethod
    def _get_position(self):
        """
        Platform dependent code to query current position.
        """
        pass

    @abstractmethod
    def _set_position(self, position):
        """
        Platform dependent code to set playback position.
        """

    @property
    def position(self):
        """
        Gets or sets the current playback position, in seconds.
        """
        return self._get_position()

    @position.setter
    def position(self, value):
        if self.loaded:
            value = max(min(value, self.duration), 0)
            self._set_position(value)

    @abstractmethod
    def _set_volume(self, value):
        """
        Platform dependent code to setting volume.
        """
        pass

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
        if self.loaded:
            self._set_volume(self._volume)

    # endregion Properties

    # region Methods
    @abstractmethod
    def _do_load_player(self):
        """
        Platform dependent code
        """
        pass

    def load_player(self):
        """
        Alloc/Load resources
        """
        self._player = self._do_load_player()
        if self._player is None:
            self._state = State.CLOSED
            raise AudioPlayerError(
                'Error loading player for file "{}"'.format(self._fullfilename))

    @abstractmethod
    def _doplay(self, mode):
        """
        Platform dependent code
        """
        pass

    def play(self, mode=PlayMode.ONCE_ASYNC):
        """
        Starts audio playback.
            - mode:  PlayMode –  ONCE_ASYNC or LOOP_ASYNC or ONCE_BLOCKING 
        """
        if self._player is None:                     # Lazy loading
            self.load_player()

        self._set_volume(self._volume)
        self._state = State.PLAYING
        self._doplay(mode)

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
        if self.loaded:
            if self.state == State.PLAYING:
                self._state = State.PAUSED
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
        if self.loaded:
            if self.state == State.PAUSED:
                self._state = State.PLAYING
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
        if self.loaded:
            self._state = State.STOPPED
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
        if self.loaded:
            self._state = State.CLOSED
            self._doclose()
            self._player = None

    def _on_finish(self):
        """
        Called by platfom code when playback is finished.
        """
        self._state = State.STOPPED
        if callable(self._finish_callback):
            self._finish_callback()

    # endregion Methods
