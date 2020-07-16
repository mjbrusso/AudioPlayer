__name__ = "audioplayer"
__package__ = "audioplayer"
__version__ = "0.6"

from platform import system

from .abstractaudioplayer import State, PlayMode
if system() == 'Windows':
    from .audioplayer_windows import AudioPlayerWindows as AudioPlayer
elif system() == 'Darwin':
    from .audioplayer_macos import AudioPlayerMacOS as AudioPlayer
else:
    from .audioplayer_linux import AudioPlayerLinux as AudioPlayer

