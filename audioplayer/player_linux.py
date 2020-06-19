import os
from abstractaudioplayer import AbstractAudioPlayer
from urllib.request import pathname2url
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)


class AudioPlayer(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        self.__class__.State = AbstractAudioPlayer.States
        self._player = Gst.ElementFactory.make('playbin', "playbin")
        self._uri = 'file://' + pathname2url(os.path.abspath(filename))

    def __del__(self):
        self._do_stop()
        
    def _do_play(self, loop=False, wait=False):
        """
        https://stackoverflow.com/a/29704692
        https://valadoc.org/gstreamer-1.0/Gst.State.NULL.html
        """

        if loop:
            self._player.connect("about-to-finish",
                                 lambda msg: self._player.set_property('uri', self._uri))
        else:
            self._player.connect("about-to-finish",
                                 lambda msg: self._set_state(AbstractAudioPlayer.States.STOPPED))

        self._player.set_property('uri', self._uri)
        self._player.set_state(Gst.State.PLAYING)
        if wait:
            self._bus = self._player.get_bus()
            self._bus.timed_pop_filtered(
                Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)

    def _do_pause(self):
        self._player.set_state(Gst.State.PAUSED)

    def _do_resume(self):
        self._player.set_state(Gst.State.PLAYING)

    def _do_stop(self):
        self._player.set_state(Gst.State.NULL)


