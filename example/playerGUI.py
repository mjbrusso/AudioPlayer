from audioplayer import AudioPlayer
import tkinter
from tkinter import filedialog, messagebox
import os
from platform import system

paused = False
player = None
buttons_glyph = ('⏏','▶', '⏯' ,'⏹')  if system() == 'Windows' else ('⏏️', '▶️', '⏯️', '⏹️')

def load():
    global player, root
    fname = filedialog.askopenfilename()
    if fname:
        player = AudioPlayer(fname)
        changevolume(0)  # update UI
        namelabel.config(text=os.path.basename(player.fullfilename))
        try:
            player.play()
        except Exception as e:
            messagebox.showerror('Error', e)


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
        try:
            player.play()
        except Exception as e:
            messagebox.showerror('Error', e)


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
root.attributes('-topmost', False)

botframe = tkinter.Frame()
botframe.pack(fill=tkinter.X, side=tkinter.TOP)
namelabel = tkinter.Label(botframe,
                          anchor=tkinter.W, font=lblfont)
namelabel.pack(fill=tkinter.X, expand=1, side=tkinter.LEFT, padx=2)
vollabel = tkinter.Label(botframe, text='100%', anchor=tkinter.E, font=lblfont)
vollabel.pack(side=tkinter.LEFT, padx=0)

toolbar = tkinter.Frame(root)
toolbar.pack(side=tkinter.TOP)
tkinter.Button(toolbar, text=buttons_glyph[0], font=btnfont, width=2,
               command=load).pack(side=tkinter.LEFT)
tkinter.Button(toolbar, text=buttons_glyph[1], font=btnfont, width=2,
               command=play).pack(side=tkinter.LEFT)
tkinter.Button(toolbar, text=buttons_glyph[2], font=btnfont, width=2,
               command=tooglepause).pack(side=tkinter.LEFT)
tkinter.Button(toolbar, text=buttons_glyph[3], font=btnfont, width=2,
               command=stop).pack(side=tkinter.LEFT)

volframe = tkinter.Frame(toolbar)
volframe.pack(side=tkinter.LEFT, expand=1, fill=tkinter.BOTH)
tkinter.Button(volframe, text='➕', command=lambda: changevolume(10)).pack(side=tkinter.TOP, expand=1, fill=tkinter.BOTH)
tkinter.Button(volframe, text='➖', command=lambda: changevolume(-10)).pack(side=tkinter.TOP, expand=1, fill=tkinter.BOTH)

root.mainloop()
