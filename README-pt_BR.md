# AudioPlayer
**audioplayer** é uma package Python 3 multi-plataforma para executar sons em diversos formatos (mp3, wav, ...). Fornece as principais características de um reprodutor de mídia, como abrir um arquivo de áudio, tocar (com loop/bloquante), pausar, despausar, finalizar e definir o volume da reprodução.

Esta packagefoi criada para prover funcionalidades sonoras à minha biblioteca de games [game2dboard](https://github.com/mjbrusso/game2dboard), mas eu decidi pblicá-la separadamente.

Sistemas suportados (veja [full list](#sistemas-suportados)):
- GNU/Linux (PC, Raspberry Pi, ...)
- Windows
- macOS

Inspirado por (e com algumas linasde código de) [playsound module](https://github.com/TaylorSMarks/playsound).

Leia esta documentação em outra linguagem: [🇧🇷](README-pt_BR.md) [🇬🇧 🇺🇸](README.md)

## Sumário
* [Instalação](#Instalação)
* [API](#API)
* [Sistemas Suportados](#sistemas-suportados)
* [Changelog](#changelog)
* [Planos para o futuro](#planos-para-o-futuro)
* [Como contribuir](#como-contribuir)
* [Licença](#licença)
  

## Instalação

### Pré-requisitos

#### GNU/Linux
No GNU/Linus, você precisa instalar PyGObject e outras dependências.

Ubuntu/Debian/Raspberry Pi OS:
```bash
sudo apt install python-gst-1.0 gstreamer1.0-plugins-base 
```     

Redhat/Centos/Fedora:
```bash
sudo yum install -y python-gstreamer1 gstreamer1-plugins-base
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

# A reprodução para quando o objeto é destruído pelo coletor de lixo, então guarde uma referência para reproduções não bloqueantes.
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
  O nome do arquivo, tal qual fornecido na criação.


- `fullfilename` : *str*  (readonly)<br> 
  O nome do arquivo, com caminho completo.


- `state` : *str*  (readonly)<br> 
  Obtém o estado atual.

  ```python3
    States(Enum):
        STOPPED = 0    
        PLAYING = 1
        PAUSED = 2
        CLOSED = 3
  ```
  **Atenção**: Atualmente, `playaudio` não muda automaticamente o estade de PLAYING para STOPPED quando termina a reprodução.

- `duration` : *float* <br> 
  Obtém o tempo de duração do trilha, em segundos.

- `position` : *float* <br> 
  Obtém ou altera a posição atual da reprodução, em segundos.

- `volume` : *int* <br> 
  Obtém ou altera o volume atual do audio (em %): 0 — 100

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

**audioPlayer** foi testado com o script `test/test_formats.py`, nas seguintes plataformas:

| SO        | Detalhes               |  mp3  |  wav  |  ogg  |  mid  |  flac  |  wma  |
| --------- | ---------------------- | :---: | :---: | :---: | :---: | :---: | :---: |
| GNU/Linux | Mint 19 (Cinnamon)     |   ✓   |   ✓  |   ✓   |   ✕   |   ✓   |   ✓   |
| GNU/Linux | Xubuntu 20.04          |   ✓   |   ✓  |   ✓   |   ✓   |   ✓   |   ✓   |
| GNU/Linux | Raspberry Pi OS        |   ✓   |   ✓  |   ✓   |   ✓   |   ✓   |   ✕   |
| Windows   | Windows 10 x64         |   ✓   |   ✓  |   ✕   |   ✓   |   ✕   |   ✓   |
| macOS     | Catalina (Python 3.8)  |   ✓   |   ✓  |   ✕   |   ✕   |   ✓   |   ✕   |

`?`: *Ainda não testado*

Deixe-me saber se você está usando em outro sistema/distro/versão!

## Changelog

- [[0.6] 2020-07-01](CHANGELOG.md#06---2020-07-01)
  
  
## Planos para o futuro 
- `.seek(position)` : Move a reprodução para a posição indicada.
- `.state` :  Estado atual (executando, parado, pausado, ...)
- `.speed = value` : Obtêm/Define a velocidade da reprodução.
- Callbacks: quando o estado é alterado, quando a posição é alterada, ...

## Como contribuir

### Submetendo uma issue

Use o [issue tracker](https://github.com/mjbrusso/audioplayer/issues) para relatar bugs e para requisitar novas features ou aprimoramentos.


### Traduzindo

Você pode contribuir traduzindo este documento para outras línguas (exceto *en* e *pt_br*).

### Submetendo um pull request

Se você aprimorar algo neste projeto, sinta-se à vontade para fazer um [pull request](https://github.com/mjbrusso/audioplayer/pulls).


## Licença

**audioplayer** é licensiado sob a [MIT license](https://github.com/mjbrusso/audioplayer/blob/master/LICENSE). 
"It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice."
