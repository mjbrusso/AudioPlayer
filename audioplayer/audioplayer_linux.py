# Inspired by https://stackoverflow.com/a/29704692
#            https://gstreamer.freedesktop.org/documentation/additional/design/states.html?gi-language=python

from .abstractaudioplayer import AbstractAudioPlayer, AudioPlayerError
from urllib.request import pathname2url

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)


class AudioPlayerLinux(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        self._uri = self.fullfilename if 'file:' in self.fullfilename else 'file://{}'.format(
            pathname2url(self.fullfilename))
        self._signal = None

    def _load_player(self):
        return Gst.ElementFactory.make('playbin', None)

    def _do_setvolume(self, value):
        volume = value / 100.0              # 0.0..1.0
        self._player.set_property('volume', volume)

    def _doplay(self, loop=False, block=False):
        """
        Starts audio playback.
            - loop:  bool – Sets whether to repeat the track automatically when finished.
            - block: bool – If true, blocks the thread until playback ends.
        """
        if not self._signal is None:
            self._player.disconnect(self._signal)
            self._signal = None
        if loop:
            self._signal = self._player.connect('about-to-finish',
                                                lambda msg: self._player.set_property('uri', self._uri))  # Repeat

        self._player.set_state(Gst.State.READY)
        self._player.set_property('uri', self._uri)
        self._player.set_state(Gst.State.PLAYING)
        status = self._player.get_state(Gst.CLOCK_TIME_NONE)
        if status[0] == Gst.StateChangeReturn.FAILURE:
            raise AudioPlayerError(
                'Failed to play "{}"'.format(self.fullfilename))

        if block:
            self._player.get_bus().timed_pop_filtered(   # block until a matching message was posted on the bus
                Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)

    def _dopause(self):
        self._player.set_state(Gst.State.PAUSED)

    def _doresume(self):
        self._player.set_state(Gst.State.PLAYING)

    def _dostop(self):
        self._player.set_state(Gst.State.NULL)

    def _doclose(self):
        self._dostop()
