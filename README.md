# AudioPlayer
**audioplayer** is a cross platform Python 3 module for playing sounds (mp3, wav, ...).

I created this package to provide sound functionality to my game library [game2dboard](https://github.com/mjbrusso/game2dboard), but I decided to publish it separately.

Suported systems (see [full list](#Suported-Systems)):
- GNU/Linux 
- Windows
- MacOS

Inspired by (and with a few lines of codes from) the [playsound module](https://github.com/TaylorSMarks/playsound).


## Installation

Install the latest release by cloning the repository:

```bash
git clone https://github.com/mjbrusso/audioplayer.git 
cd audioplayer
python3 setup.py install --user
```


### Requirements

In Linux, you need to install PyGObject and others dependencies. Follow the instructions from [PyGObject web site](https://pygobject.readthedocs.io/en/latest/getting_started.html).

### Usage

The API is documented [bellow](#API) and within the docstrings. 

After install, you can use this code to test (replace "path/to/somemusic.mp3"):

```python
from audioplayer import AudioPlayer

AudioPlayer("path/to/somemusic.mp3").play(block=True)

```

## API

### Creation

- `audioplayer.AudioPlayer(filename)`<br>
Creates the player.
  - `filename` : *str* – The file name, with extension  (.mp3, .wav, ...)

### Properties

- `filename` : *str*  (readonly)<br> 
The file name as provided in the constructor.


- `fullfilename` : *str*  (readonly)<br> 
The file name with full path.

### Methods

- `play(loop=False, block=False)`<br>
Starts audio playback.
    - `loop` (*bool*) – Sets whether to repeat the track automatically when finished.
    - `block` (*bool*) – If true, blocks the thread until playback ends.

- `pause()`<br>
Pauses audio playback.

- `resume()`<br>
Resumes audio playback.
  
- `stop()`<br>
Stops audio playback.

## Suported Systems

**audioPlayer** has been tested on the following platforms:

- GNU/Linux
  - Mint 19 (Cinnamon)
- Windows
  - Windows 10 x64
- MacOS
  - Not tested yet

Let me know if using on another system or distro!

## How to Contribute

### Submitting an issue

Use the [issue tracker](https://github.com/mjbrusso/audioplayer/issues) to submit bug reports and features or enhancements requests.


### Translating

You can contribute by translating this document into other languages ​​(except *en* and *pt_br*).

### Submitting a pull request

If you can improve anything in this project, feel free to add a [pull request](https://github.com/mjbrusso/audioplayer/pulls).


## License

**audioplayer** is under [MIT license](https://github.com/mjbrusso/audioplayer/blob/master/LICENSE). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
