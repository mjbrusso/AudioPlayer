from .abstractaudioplayer import *
from AppKit import NSSound
from time import sleep
from Cocoa import NSObject


class AudioPlayerMacOS(AbstractAudioPlayer):
    class _SoundDelegate(NSObject):
        def __init__(self):
            super().__init__()
            self.callback = None

        def sound_didFinishPlaying_(self, sound, didFinish):
            if didFinish and callable(self.callback):
                self.callback()

    def __init__(self, filename, callback=None):
        super().__init__(filename, callback)
        self._delegate = None

    def _do_load_player(self):
        return NSSound.alloc().initWithContentsOfFile_byReference_(self._filename, True)

    def _get_duration(self):
        return self._player.duration()

    def _get_position(self):
        return self._player.currentTime()

    def _set_position(self, pos):
        return self._player.setCurrentTime_(pos)

    def _set_volume(self, value):
        self._player.setVolume_(value / 100.0)              # 0.0..1.0

    def _doplay(self, mode):
        if mode != PlayMode.LOOP_ASYNC:
            if self._delegate is None:
                self._delegate = self._SoundDelegate.alloc().init()
            self._delegate.callback = self._on_finish
            self._player.setDelegate_(self._delegate)

        self._player.setLoops_(mode == PlayMode.LOOP_ASYNC)
        self._set_position(self._initial_position)
        self._player.resume()
        self._player.play()
        while self.state != State.PLAYING:  # Busy wait!  (Ծ‸ Ծ)
            sleep(0.1)

    def _dopause(self):
        self._player.pause()

    def _doresume(self):
        self._player.resume()

    def _dostop(self):
        self._player.stop()

    def _doclose(self):
        self._player.stop()
