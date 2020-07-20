# Inspired by https://stackoverflow.com/a/29704692
#            https://gstreamer.freedesktop.org/documentation/additional/design/State.html?gi-language=python

from .abstractaudioplayer import *
from urllib.request import pathname2url
from threading import Thread

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
Gst.init(None)


class AudioPlayerLinux(AbstractAudioPlayer):
    _gloop_thread = None    # Class (static) field

    def __init__(self, filename, callback=None):
        super().__init__(filename, callback)
        self._uri = self.fullfilename if 'file:' in self.fullfilename else 'file://{}'.format(
            pathname2url(self.fullfilename))
        self._about_to_finish_signal = None
        self._message_signal = None
        self._saved_duration = 0.0
        self._bus = None
        if AudioPlayerLinux._gloop_thread is None:
            # https://stackoverflow.com/a/7283584
            # "If you don't plan on using GTK with the program, you will have to run a gobject.Mainloop() in order to get messages from the bus."
            AudioPlayerLinux._gloop_thread = Thread(
                target=GObject.MainLoop().run)
            AudioPlayerLinux._gloop_thread.daemon = True
            AudioPlayerLinux._gloop_thread.start()

    def _do_load_player(self):
        return Gst.ElementFactory.make('playbin', None)

    def _get_position(self):
        res, time = self._player.query_position(Gst.Format.TIME)
        return time / Gst.SECOND if res else 0.0

    def _set_position(self, position):
        self._player.seek_simple(
            Gst.Format.TIME, Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT, position * Gst.SECOND)

    def _get_duration(self):
        ok, duration = self._player.query_duration(Gst.Format.TIME)
        if not ok and self._bus is not None:
            self._bus.timed_pop_filtered(0.5 * Gst.SECOND, Gst.MessageType.DURATION_CHANGED)
            ok, duration = self._player.query_duration(Gst.Format.TIME)        

        duration = max(duration / Gst.SECOND, self._saved_duration)
        self._saved_duration = duration
        return duration

    def _set_volume(self, value):
        volume = value / 100.0              # 0.0..1.0
        self._player.set_property('volume', volume)

    def _on_message(self, bus, message):
        if message.type == Gst.MessageType.EOS:
            self._player.set_state(Gst.State.NULL)
            self._on_finish()

    def _doplay(self, mode):
        if self._about_to_finish_signal is not None:
            self._player.disconnect(self._about_to_finish_signal)
            self._about_to_finish_signal = None

        if mode == PlayMode.LOOP_ASYNC:
            self._about_to_finish_signal = self._player.connect('about-to-finish', lambda msg: self._player.set_property(
                'uri', self._uri))                                            #

        self._saved_duration = 0.0
        self._player.set_state(Gst.State.READY)
        self._player.set_property('uri', self._uri)
        self._player.set_state(Gst.State.PLAYING)
        self._bus = self._player.get_bus()

        if self._initial_position > 0:
            self._bus.timed_pop_filtered(
                Gst.CLOCK_TIME_NONE, Gst.MessageType.STREAM_START)
            self._set_position(self._initial_position)

        status = self._player.get_state(Gst.CLOCK_TIME_NONE)
        if status[0] == Gst.StateChangeReturn.FAILURE:
            raise AudioPlayerError(
                'Failed to play "{}"'.format(self.fullfilename))

        if mode == PlayMode.ONCE_BLOCKING:
            # block until a matching message was posted on the bus
            self._bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE,
                                         Gst.MessageType.ERROR | Gst.MessageType.EOS)
            self._on_finish()
        elif mode == PlayMode.ONCE_ASYNC:
            self._bus.add_signal_watch()
            if self._message_signal is not None:
                self._bus.disconnect(self._message_signal)
            self._message_signal = self._bus.connect(
                "message", self._on_message)

    def _dopause(self):
        self._player.set_state(Gst.State.PAUSED)

    def _doresume(self):
        self._player.set_state(Gst.State.PLAYING)

    def _dostop(self):
        self._player.set_state(Gst.State.NULL)

    def _doclose(self):
        self._dostop()
