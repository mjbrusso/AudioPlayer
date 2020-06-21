from abstractaudioplayer import AbstractAudioPlayer
from urllib.request import pathname2url

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)


class AudioPlayer(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        self._uri = 'file://{}'.format(pathname2url(self._filename))

    def _load_player(self):
        return Gst.ElementFactory.make('playbin', "playbin")

    def _doplay(self, loop=False, block=False):
        """
         Inspired by https://stackoverflow.com/a/29704692
        """
        if loop:
            self._player.connect("about-to-finish",
                                 lambda msg: self._player.set_property('uri', self._uri))

        self._player.set_property('uri', self._uri)
        self._player.set_state(Gst.State.PLAYING)
        if block:
            self._player.get_bus().timed_pop_filtered(
                Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)

    def _dopause(self):
        self._player.set_state(Gst.State.PAUSED)

    def _doresume(self):
        self._player.set_state(Gst.State.PLAYING)

    def _dostop(self):
        self._player.set_state(Gst.State.NULL)
