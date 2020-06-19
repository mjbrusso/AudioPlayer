# https://lawlessguy.wordpress.com/2016/02/10/play-mp3-files-with-python-windows/
# https://social.msdn.microsoft.com/Forums/vstudio/en-US/1abd0100-a2ec-4e62-b66f-d6d574a4a258/play-pause-restart-amp-stop-an-audio-file?forum=vbgeneral

class PlaysoundException(Exception):
    pass

class _PlatformPlayer():

    def play(self, sound, loop=False):
        '''
        Inspired by (but not copied from) Michael Gundlach <gundlach@gmail.com>'s mp3play:
        https://github.com/michaelgundlach/mp3play


        '''
        from ctypes import c_buffer, windll
        from random import random
        from time import sleep
        from sys import getfilesystemencoding

        def winCommand(*command):
            buf = c_buffer(255)
            command = ' '.join(command).encode(getfilesystemencoding())
            errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
            if errorCode:
                errorBuffer = c_buffer(255)
                windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
                exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                                    '\n        ' + command.decode() +
                                    '\n    ' + errorBuffer.value.decode())
                raise PlaysoundException(exceptionMessage)
            return buf.value

        alias = 'playsound_' + str(random())
        winCommand('open "' + sound + '" alias', alias)
        winCommand('set', alias, 'time format milliseconds')
        durationInMS = winCommand('status', alias, 'length')
        winCommand('play', alias, 'from 0 to', durationInMS.decode())

