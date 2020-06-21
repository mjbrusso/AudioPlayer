from platform import system

if system() == 'Windows':
    from audioplayer_windows import AudioPlayer
elif system() == 'Darwin':
    from audioplayer_macos import AudioPlayer
else:
    from audioplayer_linux import AudioPlayer

