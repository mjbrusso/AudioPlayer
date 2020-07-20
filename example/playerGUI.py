from audioplayer import *
from tkinter import *
from tkinter import filedialog, messagebox
import os
from platform import system


WTITLE = 'Music Player'

class PlayerButton(Button):
    def __init__(self, master=None, imagefile='', **options):
        options.setdefault('border', 0)
        options.setdefault('height', 60)
        options.setdefault('width', 50)
        if type(imagefile) != list and type(imagefile) != tuple:
            imagefile = (str(imagefile), )

        self._image = []
        for name in imagefile:
            self._image.append(PhotoImage(file=os.path.join(
                os.path.dirname(__file__), 'icons', name)))

        options.setdefault('image', self._image[0])
        super().__init__(master, **options)
        self.pack(side=LEFT)

    def change_image(self, pos):
        self.configure(image=self._image[pos])


class Player():
    def __init__(self):
        self.player = None
        self.buildUI()
        self.autorepeat = False

    def on_finish(self):
        if self.autorepeat:
            self.rewind()

    def load(self):
        fname = filedialog.askopenfilename()
        if fname:
            if self.player:
                self.player.close()
            self.player = AudioPlayer(fname, self.on_finish)
            self.namelabel.config(
                text=os.path.basename(self.player.fullfilename))
            try:
                self.rewind()
            except Exception as e:
                messagebox.showerror('Error', e)

    def resetui(self):
        self.poslabel.config(text=self.format_time(0.0))
        self.durationlabel.config(text=self.format_time(self.player.duration))
        self.posscale.config(to=self.player.duration)
        self.posvar.set(0.0)

    def timer(self):
        pos = self.player.position
        self.posvar.set(pos)
        self.poslabel.config(text=self.format_time(pos))
        self.root.title('{}  [{}]'.format(WTITLE, self.player.state))
        if self.player.state == State.PLAYING:        
            self.root.after(100, self.timer)

    def rewind(self):
        if self.player is not None:
            self.player.play()
            self.resetui()
            self.timer()

    def playpause(self):
        if self.player is None:
            self.load()
        else:
            if self.player.state == State.STOPPED:
                self.rewind()
            elif self.player.state == State.PAUSED:
                self.player.resume()
            else:
                self.player.pause()
        self.timer()

    def stop(self):
        if self.player is not None:
            self.player.stop()
            self.posvar.set(0)
            self.poslabel.config(text=self.format_time(0.0))

    def changevolume(self, delta):
        if self.player is not None:
            self.player.volume += delta
            self.vollabel.config(text='{}%'.format(self.player.volume))

    def seek(self, pos):
        if self.player is not None:
            if self.player.state == State.STOPPED:
                self.rewind()
                self.player.pause()
            if self.player.position != self.posscale.get():
                self.player.position = self.posscale.get()
                self.poslabel.config(text=self.format_time(pos))

    def repeat(self):
        self.autorepeat = not self.autorepeat
        self.repeatbutton.change_image(int(self.autorepeat))

    def nop(self):
        pass

    def format_time(self, value):
        value = float(value)
        d = value - int(value)
        value = int(value)
        m = value // 60
        s = value % 60
        return '{:02d}:{:02d}{}'.format(m, s, '{:.1f}'.format(d).replace('0.', '.'))

    def buildUI(self):
        self.root = Tk()
        self.root.title(WTITLE)
        self.root.geometry("600x200")
        self.root.attributes('-topmost', True)
        self.root.resizable(False, False)
        self.root.attributes('-topmost', False)

        self.mainframe = Frame(width=500)
        self.mainframe.pack(fill=BOTH, expand=1)

        self.namelabel = Label(self.mainframe, text="No file opened",
                               anchor=W,
                               font=(None, 16))
        self.namelabel.pack(side=TOP, pady=20)

        self.positionframe = Frame(self.mainframe)
        self.positionframe.pack(side=TOP, fill=BOTH, expand=1, padx=6)
        self.poslabel = Label(self.positionframe, text='00:00.0', width=7,
                              anchor=W)
        self.poslabel.pack(side=LEFT, padx=0)
        self.posvar = DoubleVar()
        self.posscale = Scale(self.positionframe, orient=HORIZONTAL, from_=0,
                              to=5.5, resolution=0.1, showvalue=False,
                              sliderlength=8, command=self.seek, variable=self.posvar)

        self.posscale.pack(side=LEFT, expand=1, fill=X, padx=5)

        self.durationlabel = Label(self.positionframe,
                                   text='00:00.0', width=7, anchor=E)
        self.durationlabel.pack(side=RIGHT, padx=0)

        self.buttonsframe = Frame(self.mainframe)
        self.buttonsframe.pack(side=TOP, padx=5, ipady=10, expand=1, fill=X)

        self.leftbuttonsframe = Frame(self.buttonsframe)
        self.leftbuttonsframe.pack(side=LEFT, expand=1, fill=X)
        self.addbutton = PlayerButton(self.leftbuttonsframe, imagefile='add.png',
                                      command=self.load)
        self.previousbutton = PlayerButton(self.leftbuttonsframe, imagefile='previous.png',
                                           command=self.rewind)
        self.playpausebutton = PlayerButton(self.leftbuttonsframe, width=60, imagefile='pause.png',
                                            command=self.playpause)
        self.stopbutton = PlayerButton(self.leftbuttonsframe, imagefile='stop.png',
                                       command=self.stop)
        # self.nextbutton = PlayerButton(self.leftbuttonsframe, imagefile='next.png',
        #                               command=self.nop)
        self.repeatbutton = PlayerButton(self.leftbuttonsframe, imagefile=('repeat.png', 'repeaton.png'),
                                         command=self.repeat)
        # self.deletebutton = PlayerButton(self.leftbuttonsframe, imagefile='delete.png',
        #                                 command=self.nop)
        # self.shufflebutton = PlayerButton(self.leftbuttonsframe, imagefile='shuffle.png',
        #                                  command=self.nop)

        self.volframe = Frame(self.buttonsframe)
        self.volframe.pack(side=RIGHT, padx=(20, 0))
        self.volumedownbutton = PlayerButton(self.volframe, imagefile='volumedown.png',
                                             command=lambda: self.changevolume(-10))
        self.vollabel = Label(self.volframe, text="100%", width=5)
        self.vollabel.pack(side=LEFT)
        self.volumeupbutton = PlayerButton(self.volframe, imagefile='volumeup.png',
                                           command=lambda: self.changevolume(10))

        #self.playlistbox = Listbox(self.mainframe)
        #self.playlistbox.pack(side=BOTTOM, expand=1, fill=BOTH)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Player().run()
