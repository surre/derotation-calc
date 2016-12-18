from tkinter import *
from tkinter.messagebox import askokcancel

class QuitApp(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Confirm exit', "Quit Application?")
        if ans:
            Frame.quit(self)

if __name__=='__main__':
    QuitApp().mainloop() 
