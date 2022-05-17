# AudioPlayer

[![Downloads](https://static.pepy.tech/personalized-badge/audioplayer?period=total&units=international_system&left_color=black&right_color=orange&left_text=%20PyPI%20Download%20Stats)](https://pepy.tech/project/audioplayer)

**audioplayer** это кросс плотформенный модуль для Python 3 (mp3, wav, ...). Он предоставляет возможности базового медиа проигрывателя, такие как: открытие медиа файлов, проигрывания (loop/block), пауза, продолжить, остановить, а также настройка громкости.

I created this package to provide sound functionality to my game library
Изначально я создал этот модуль чтобы добавить звуки в мою игровую библиотеку [game2dboard](https://github.com/mjbrusso/game2dboard), но я решил опубликовать его отдельно.

Поддерживаемые системы ([полный лист](#suported-systems)):
- GNU/Linux (PC, Raspberry Pi, ...)
- Windows
- macOS

Вдохновлёно [playsound module](https://github.com/TaylorSMarks/playsound).

Читать это в других языках: [🇧🇷](README-pt_BR.md) [🇬🇧 🇺🇸](README.md)

## Контент
* [Установка](#установка)
* [API](#API)
* [Поддерживаемые системы](#поддерживаемые-системы)
* [Changelog](#changelog)
* [Что в roadmap](#что-в-roadmap)
* [Как внести свой вклад](#как-внести-свой-вклад)
* [Лицензия](#лицензия)
  

## Установка

### Предпосылки

#### GNU/Linux
В Linux, вы должны установить PyGObject и другие зависимости.

Ubuntu/Debian/Raspberry Pi OS:
```bash
sudo apt-get install python-gst-1.0 \ 
                     gir1.2-gstreamer-1.0 \ 
                     gstreamer1.0-tools \
                     gir1.2-gst-plugins-base-1.0 
                     gstreamer1.0-plugins-good \
                     gstreamer1.0-plugins-ugly                     
```

Redhat/Centos/Fedora:
```bash
sudo yum install -y python-gstreamer1 \ 
                    gstreamer1-plugins-good \
                    gstreamer1-plugins-ugly
```

#### macOS

В macOS, вы должны установить PyObjC bridge.

```bash
pip3 install PyObjC --user
```

### Установка

Рекомендованный способ установки `audioplayer` это использование **pip** (or **pip3**).

```
pip3 install audioplayer
```

Если у вас нет админ прав, установите в вашу home папку.

```
pip3 install audioplayer --user
```


Также вы можете установить клонируя этот репозиторий.

```bash
git clone https://github.com/mjbrusso/audioplayer.git 
cd audioplayer
python3 setup.py install --user
```

### Использование

API документирован [ниже](#API). 

После установки вы можете использовать этот код для проверки (замените "path/to/somemusic.mp3"):

```python
from audioplayer import AudioPlayer

# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
AudioPlayer("path/to/somemusic.mp3").play(block=True)

```

## API

### Создание

- `audioplayer.AudioPlayer(filename)`<br>
  Создаёт проигрователь.
    - `filename` : *str* – Файл с расширением (.mp3, .wav, ...)
  
  Raise: `FileNotFoundError()` :  Файл не существует.

### Параметры

- `filename` : *str*  (readonly)<br> 
  Файл.


- `fullfilename` : *str*  (readonly)<br> 
  Полный путь до файла.


- `volume` : *int* <br> 
  Читает или ставит громкость (в %) файла (0 — 100)

### Методы

- `play(loop=False, block=False)`<br>
  Запукает звук/музыку.
    - `loop` (*bool*) – Повторять ли этот файл.
    - `block` (*bool*) – Если True, то текущий Thread будет заморожен на время проигрывания.

  Raise: `AudioPlayerError()`: Не удалось проиграть файл.

- `pause()`<br>
  Ставит на паузу.

- `resume()`<br>
  Продолжает проигрывание, снимает с паузы.
  
- `stop()`<br>
  Прекращает проигрывание, возможно проиграть заного.

- `close()`<br>
  Закрывает файл, проиграть заного не возможно.


## Поддерживаемые системы

**audioPlayer** был протестирован на следущих платформах:

| OS        | Детали                |  mp3  |  wav  |  ogg  |  mid  |
| --------- | ---------------------- | :---: | :---: | :---: | :---: |
| GNU/Linux | Mint 19 (Cinnamon)     |   ✓   |   ✓   |   ✓   |   ✕   |
| GNU/Linux | Xubuntu 20.04          |   ✓   |   ✓   |   ✓   |   ✓   |
| GNU/Linux | Raspberry Pi OS        |   ✓   |   ✓   |   ✓   |   ✓   |
| Windows   | Windows 10 x64         |   ✓   |   ✓   |   ✕   |   ✓   |
| macOS     | Catalina (Python 3.8)  |   ✓   |   ✓   |   ✕   |   ✕   |

`?`: *Ещё не протестировано*

Дайте мне знать если вы используете другую OS!

## Changelog

- [[0.6] 2020-07-01](CHANGELOG.md#06---2020-07-01)

## Что в roadmap 
- `.seek(position)` : Двигает проигрыватель в определенную позицию.
- `.state` :  Текущий статус (проигрывает, остановлен, на паузе, ...)
- `.speed = value` : Читает/Ставит скорость проигрывания.
- Callbacks: когда статус изменён, когда позиция изменена, ...

## Как внести свой вклад

### Issue репорт

Используйте [issue tracker](https://github.com/mjbrusso/audioplayer/issues) чтобы опубликовать баги, ваши идеи и тд


### Перевод

Вы можете перевести этот документ на другой язык ​​(но не *en* и *pt_br*).

### Pull request

Если вы можете улучшить что нибудь в этом проекте, то добавьте [pull request](https://github.com/mjbrusso/audioplayer/pulls).


## Лицензия

**audioplayer** is under [MIT license](https://github.com/mjbrusso/audioplayer/blob/master/LICENSE). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
