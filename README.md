# AudioPlayer
**audioplayer** is a cross platform Python 3 module for playing sounds (mp3, wav, ...)

Inspired by (and with a few lines of codes from) the [playsound module](https://github.com/TaylorSMarks/playsound).

## Installation

Install the latest release by cloning the repository:

```bash
git clone https://github.com/mjbrusso/audioplayer.git 
cd audioplayer
python3 setup.py install --user
```


## Requirements

To do

## Usage

The API is documented [bellow](#API) and within the docstrings. 

After install, you you can really test with this code:

```python
from audioplayer import AudioPlayer

p = AudioPlayer("music.mp3")
p.play(block=True)

```

## API

### Creation

- `audioplayer.AudioPlayer(filename)`<br>
Creates the player.
  - `filename` : *str* – The file name, with extension  (.mp3, .wav, ...)


### Methods

- `play(loop=False, block=False)`<br>
Sarts audio playback.
    - `loop` (*bool*) – Sets whether to repeat the track automatically when finished.
    - `block` (*bool*) – If true, blocks the thread until playback ends.

- `pause()`<br>
Pauses audio playback.

- `pause()`<br>
Resumes audio playback.
  
- `stop()`<br>
Stops audio playback.


## How to Contribute

### Submitting an issue

Use the [issue tracker](https://github.com/mjbrusso/audioplayer/issues) to submit bug reports and features or enhancements requests.


### Translating

You can contribute by translating this document into other languages ​​(except *en* and *pt_br*).

### Submitting a pull request

If you can improve anything in this project, feel free to add a [pull request](https://github.com/mjbrusso/audioplayer/pulls).


## License

audioplayer is under [MIT license](https://github.com/mjbrusso/audioplayer/blob/master/LICENSE). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
