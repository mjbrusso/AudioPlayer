class _PlatformPlayer():
    def play(self, sound, loop=False):
        '''
        http://stackoverflow.com/a/34568298/901641
        '''
        from AppKit import NSSound
        from Foundation import NSURL

        if '://' not in sound:
            if not sound.startswith('/'):
                from os import getcwd
                sound = getcwd() + '/' + sound
            sound = 'file://' + sound
        url = NSURL.URLWithString_(sound)
        nssound = NSSound.alloc().initWithContentsOfURL_byReference_(url, True)
        if not nssound:
            raise IOError('Unable to load sound named: ' + sound)
        nssound.play()
