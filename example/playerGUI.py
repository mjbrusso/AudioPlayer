from audioplayer import AudioPlayer
import tkinter
from tkinter import filedialog
import os

paused = False
player = None


def load():
    global player, root
    fname = filedialog.askopenfilename()
    if fname:
        player = AudioPlayer(fname)
        changevolume(0)  # update UI
        namelabel.config(text=os.path.basename(player.fullfilename))
        player.play()


def tooglepause():
    global player, paused
    if not player is None:
        if paused:
            player.resume()
        else:
            player.pause()
        paused = not paused


def play():
    global player
    if not player is None:
        player.play()


def stop():
    global player
    if not player is None:
        player.stop()


def changevolume(delta):
    global player, vollabel
    if not player is None:
        player.volume += delta
        vollabel.config(text='{}%'.format(player.volume))


btnfont = (None, 30)
lblfont = (None, 8)

# Build UI
root = tkinter.Tk()
root.title('Music Player')
root.attributes('-topmost', True)
root.resizable(False, False)

botframe = tkinter.Frame()
botframe.pack(fill=tkinter.X, side=tkinter.TOP)
namelabel = tkinter.Label(botframe, text='No file open',
                          anchor=tkinter.W, font=lblfont)
namelabel.pack(fill=tkinter.X, expand=1, side=tkinter.LEFT, padx=2)
vollabel = tkinter.Label(botframe, text='100%', anchor=tkinter.E, font=lblfont)
vollabel.pack(side=tkinter.LEFT, padx=3)

toolbar = tkinter.Frame(root)
toolbar.pack(side=tkinter.TOP)
tkinter.Button(toolbar, text='⏏', font=btnfont, width=2,
               command=load).pack(side=tkinter.LEFT)
tkinter.Button(toolbar, text='⏵', font=btnfont, width=2,
               command=play).pack(side=tkinter.LEFT)
tkinter.Button(toolbar, text='⏯', font=btnfont, width=2,
               command=tooglepause).pack(side=tkinter.LEFT)
tkinter.Button(toolbar, text='⏹', font=btnfont, width=2,
               command=stop).pack(side=tkinter.LEFT)

volframe = tkinter.Frame(toolbar)
volframe.pack(side=tkinter.LEFT)
tkinter.Button(volframe, text='+', height=1, width=2,
               command=lambda: changevolume(10)).pack(side=tkinter.TOP)
tkinter.Button(volframe, text='-', height=1, width=2,
               command=lambda: changevolume(-10)).pack(side=tkinter.TOP)

root.mainloop()
