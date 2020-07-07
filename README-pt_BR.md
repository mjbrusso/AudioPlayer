# AudioPlayer
**audioplayer** é uma package Python 3 multi-plataforma para executar sons em diversos formatos (mp3, wav, ...). Fornece as principais características de um reprodutor de mídia, como abrir um arquivo de áudio, tocar (com loop/bloquante), pausar, despausar, finalizar e definir o volume da reprodução.

Esta packagefoi criada para prover funcionalidades sonoras à minha biblioteca de games [game2dboard](https://github.com/mjbrusso/game2dboard), mas eu decidi pblicá-la separadamente.

Sistemas suportados (veja [full list](#sistemas-suportados)):
- GNU/Linux (PC, Raspberry Pi, ...)
- Windows
- macOS

Inspirado por (e com algumas linasde código de) [playsound module](https://github.com/TaylorSMarks/playsound).

Leia esta documentação em outra linguagem

[🇧🇷](README-pt_BR.md) [🇬🇧/🇺🇸](README.md)

## Sumário
* [Instalação](#Instalação)
* [API](#API)
* [Sistemas Suportados](#sistemas-suportados)
* [What's in the roadmap?](#whats-in-the-roadmap)
* [How to Contribute](#how-to-contribute)
* [License](#license)
  

## Instalação

### Pré-requisitos

#### GNU/Linux
No GNU/Linus, você precisa instalar PyGObject e outras dependências.

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

No macOS, voê precisa instalar a bridge PyObjC .

```bash
pip3 install PyObjC --user
```

### Instalação

Recomendamos instalar `audioplayer` usando o instalador **pip** (or **pip3**).

```
pip3 install audioplayer
```

Se você não tem privilégios de administrador, instale-o em sua pasta pessoal.

```
pip3 install audioplayer --user
```

Você também pode instalar clonando a versão mais recente deste repositório.

```bash
git clone https://github.com/mjbrusso/audioplayer.git 
cd audioplayer
python3 setup.py install --user
```

### Usando

A API está documentada [abaixo](#API) e nos comentários docstrings. 

Após a instalação, você pode usar este código para testar (substitua "path/to/somemusic.mp3" por um nome real de arquivo):

```python
from audioplayer import AudioPlayer

# A reprodução para quando o objeto é destruído pelo coletor de lixo, então guarde uma referência para reproduçõs não bloqueantes.
AudioPlayer("path/to/somemusic.mp3").play(block=True)

```

## API

### Criação

- `audioplayer.AudioPlayer(filename)`<br>
  Cria o player.
    - `filename` : *str* – Nome do arquivo, com extensão  (.mp3, .wav, ...)
  
  Raise: `FileNotFoundError()` :  O arquivo não existe.

### Propriedades

- `filename` : *str*  (readonly)<br> 
  O nome do arquivo, tal quel formecido na criação.


- `fullfilename` : *str*  (readonly)<br> 
  O nome do arquivo, com caminho completo.


- `volume` : *int* <br> 
  ObtÇem ou define o volume atual do audio (em %): 0 — 100

### Métodos

- `play(loop=False, block=False)`<br>
  Inicia a reprodução.
    - `loop` (*bool*) – Repetir automaticamente a faixa quando concluída?
    - `block` (*bool*) – Bloquear a thread durante a execução?

  Raise: `AudioPlayerError()`: Falha ao executar.

- `pause()`<br>
  Pausa a reprodução.

- `resume()`<br>
  Retorna da pausa.
  
- `stop()`<br>
  Para a reprodução do áudio. Pode ser executado novamente.

- `close()`<br>
  Fecha o dispositivo de reprodução, liberando recursos. Não poderá ser executado novamente.


## Sistemas Suportados

**audioPlayer** foi testado nas seguintes plataformas:

| OS        | Detalhes               |  mp3  |  wav  |  ogg  |  mid  |
| --------- | ---------------------- | :---: | :---: | :---: | :---: |
| GNU/Linux | Mint 19 (Cinnamon)     |   ✓   |   ✓   |   ✓   |   ✕   |
| GNU/Linux | Xubuntu 20.04          |   ✓   |   ✓   |   ✓   |   ✓   |
| GNU/Linux | Raspberry Pi OS        |   ✓   |   ✓   |   ✓   |   ✓   |
| Windows   | Windows 10 x64         |   ✓   |   ✓   |   ✕   |   ✓   |
| macOS     | Catalina (Python 3.8)  |   ✓   |   ✓   |   ✕   |   ✕   |

`?`: *Ainda não testado*

Deixe-me saber se você est'usando em outro sistema/distro/versão!

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
