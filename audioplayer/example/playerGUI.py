from audioplayer import AudioPlayer
import tkinter
from tkinter import filedialog
import os

dirname = os.path.join(os.path.dirname(__file__), 'img')
paused = False
player = None


def load():
    global player, root
    fname = filedialog.askopenfilename()
    if fname:
        player = AudioPlayer(fname)
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


def addvolume(inc):
    global player, vollabel
    if not player is None:
        player.volume += inc
        vollabel.config(text='{}%'.format(player.volume))


root = tkinter.Tk()
root.title('Music Player')
root.attributes('-topmost', True)
btnfont = (None, 30)
lblfont = (None, 8)

botframe = tkinter.Frame()
botframe.pack(fill=tkinter.X, side=tkinter.TOP)
namelabel = tkinter.Label(botframe, text='No file open',
                          anchor=tkinter.W, font=lblfont)
namelabel.pack(fill=tkinter.X, expand=1, side=tkinter.LEFT, padx=2)
vollabel = tkinter.Label(botframe, text='100%', anchor=tkinter.E, font=lblfont)
vollabel.pack(side=tkinter.LEFT, padx=3)

toolbar = tkinter.Frame(root)
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
               command=lambda: addvolume(10)).pack(side=tkinter.TOP)
tkinter.Button(volframe, text='-', height=1, width=2,
               command=lambda: addvolume(-10)).pack(side=tkinter.TOP)
toolbar.pack(side=tkinter.TOP)

root.resizable(False, False)
root.mainloop()
