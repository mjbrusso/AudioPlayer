# AudioPlayer
**audioplayer** is a cross platform Python 3 package for playing sounds (mp3, wav, ...). It provides the key features of an audio player, such as opening a media file, playing (loop/block), pausing, resuming, stopping, and setting the playback volume.

I created this package to provide sound functionality to my game library [game2dboard](https://github.com/mjbrusso/game2dboard), but I decided to publish it separately.

Suported systems (see [full list](#suported-systems)):
- GNU/Linux (PC, Raspberry Pi, ...)
- Windows
- macOS

Inspired by (and with a few lines of codes from) the [playsound module](https://github.com/TaylorSMarks/playsound).

Read this in another languages: [🇧🇷](README-pt_BR.md) [🇬🇧 🇺🇸](README.md)

## Table of contents
* [Install](#Install)
* [API](#API)
* [Suported Systems](#Suported-Systems)
* [Changelog](#changelog)
* [What's in the roadmap?](#whats-in-the-roadmap)
* [How to Contribute](#how-to-contribute)
* [License](#license)
  

## Install

### Prerequisites

#### GNU/Linux
In Linux, you need to install PyGObject and others dependencies.

Ubuntu/Debian/Raspberry Pi OS:
```bash
sudo apt install python-gst-1.0 gstreamer1.0-plugins-base                
```

Redhat/Centos/Fedora:
```bash
sudo yum install -y python-gstreamer1 gstreamer1-plugins-base
```

#### macOS

In macOS, you need to install PyObjC bridge.

```bash
pip3 install PyObjC --user
```

### Install

The recommended way to install `audioplayer` is using the Python **pip** (or **pip3**) installer.

```
pip3 install audioplayer
```

If you don't have administrator privileges, install in your home folder.

```
pip3 install audioplayer --user
```


You can install the latest release by cloning this repository.

```bash
git clone https://github.com/mjbrusso/audioplayer.git 
cd audioplayer
python3 setup.py install --user
```

### Usage

The API is documented [bellow](#API) and within the docstrings. 

After install, you can use this code to test (replace "path/to/somemusic.mp3"):

```python
from audioplayer import AudioPlayer

# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
AudioPlayer("path/to/somemusic.mp3").play(block=True)

```

See the [playerGUI](https://github.com/mjbrusso/AudioPlayer/blob/master/example/) for a full example.

[playerGUI](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/docs/playerGUI.png) 

## API

### States

```python3
    State(Enum):
        STOPPED = 0     # Position at 00:00.0, ready to start playing
        PLAYING = 1     # Playing
        PAUSED = 2      # Paused
        CLOSED = 3      # Can't play again
```

[State Diagram](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/docs/state_diagram.png) 


### Creation

- `audioplayer.AudioPlayer(filename, callback)`<br>
  Creates the player.
    - `filename` : *str* – The file name with extension  (.mp3, .wav, ...)
    - `callback` : *function()* – Callback function to be called when playback ends (it's called only if the play mode is PlayMode.ONCE_ASYNC)
  
  Raise: `FileNotFoundError()` :  The file does not exist.

### Properties

- `filename` : *str*  (readonly)<br> 
  The file name as provided in the constructor.

- `fullfilename` : *str*  (readonly)<br> 
  The file name with full path.

- `state` : *str*  (readonly)<br> 
  Gets the current [state](#states).

- `duration` : *float* <br> 
  Gets the duration of the track, in seconds.

- `position` : *float* <br> 
  Gets or sets the current playback position, in seconds.

- `volume` : *int* <br> 
  Gets or sets the current volume (in %) of the audio (0 — 100)


### Methods

- `play(mode=PlayMode.ONCE_ASYNC)`<br>
  Starts audio playback.
    - `mode`:  (*PlayMode*) –  ONCE_ASYNC or LOOP_ASYNC or ONCE_BLOCKING 

  Raise: `AudioPlayerError()`: Failed to play.

- `pause()`<br>
  Pauses audio playback.

- `resume()`<br>
  Resumes audio playback.
  
- `stop()`<br>
  Stops audio playback. Can play again.

- `close()`<br>
  Closes device, releasing resources. Can't play again.


## Suported Systems

**audioPlayer** has been tested, using `test/test_formats.py` script, on the following platforms:

| OS        | Details                |  mp3  |  wav  |  ogg  |  mid  |  flac  |  wma  |
| --------- | ---------------------- | :---: | :---: | :---: | :---: | :---: | :---: |
| GNU/Linux | Mint 19 (Cinnamon)     |   ✓   |   ✓  |   ✓   |   ✕   |   ✓   |   ✓   |
| GNU/Linux | Xubuntu 20.04          |   ✓   |   ✓  |   ✓   |   ✓   |   ✓   |   ✓   |
| GNU/Linux | Raspberry Pi OS        |   ✓   |   ✓  |   ✓   |   ✓   |   ✓   |   ✕   |
| Windows   | Windows 10 x64         |   ✓   |   ✓  |   ✕   |   ✓   |   ✕   |   ✓   |
| macOS     | Catalina (Python 3.8)  |   ✓   |   ✓  |   ✕   |   ✕   |   ✓   |   ✕   |

`?`: *Not yet tested*

Let me know if you are using on another system/distro/version! 

## Changelog

- [[0.6] 2020-07-01](CHANGELOG.md#06---2020-07-01)

## What's in the roadmap? 
- `.seek(position)` : Moves playback to the specified position.
- `.state` :  Current state (playing, stopped, paused, ...)
- `.speed = value` : Gets/sets playback speed.
- Callbacks: when state changed, when position changed by a delta, ...

## How to Contribute

### Submitting an issue

Use the [issue tracker](https://github.com/mjbrusso/audioplayer/issues) to submit bug reports and features or enhancements requests.


### Translating

You can contribute by translating this document into other languages ​​(except *en* and *pt_br*).

### Submitting a pull request

If you can improve anything in this project, feel free to add a [pull request](https://github.com/mjbrusso/audioplayer/pulls).


## License

**audioplayer** is under [MIT license](https://github.com/mjbrusso/audioplayer/blob/master/LICENSE). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
