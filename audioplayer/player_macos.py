from abstractaudioplayer import AbstractAudioPlayer
from AppKit import NSSound
from Foundation import NSURL
from time import sleep
'''
    http://stackoverflow.com/a/34568298/901641
'''

class AudioPlayer(AbstractAudioPlayer):
    def __init__(self, filename):
        super().__init__(filename)
        if '://' not in filename:
            if not filename.startswith('/'):
                from os import getcwd
                filename = getcwd() + '/' + filename
            filename = 'file://' + filename
        self._uri = NSURL.URLWithString_(filename)
        self._nssound = NSSound.alloc().initWithContentsOfURL_byReference_(self._uri, True)

    def __del__(self):
        self._nssound = None
        self._do_stop()


    def _do_play(self, loop=False, block=False):
        self._nssound.loops = loop
        self._nssound.play()
        if block:
            sleep(self._nssound.duration())

    def _do_pause(self):
        self._nssound.pause()

    def _do_resume(self):
        self._nssound.resume()

    def _do_stop(self):
        self._nssound.stop()
