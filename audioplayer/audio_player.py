from platform import system

system = system()
if system == 'Windows':
    from player_windows import AudioPlayer
elif system == 'Darwin':
    from player_macos import AudioPlayer
else:
    from player_linux import AudioPlayer
del system
