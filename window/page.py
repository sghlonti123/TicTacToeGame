from tkinter import *
from tkinter.ttk import *


class Window:
    WIDTH = 400
    HEIGHT = 400
    SIZE=f"{WIDTH}x{HEIGHT}"
    tk = Tk()

    def __init__(self):
        self.tk.geometry(self.SIZE)
        self.tk.title("Tic Tac Toe")
        Button(self.tk,text="Start Game", command=self.playGame).pack()
        mainloop()

    def playGame(self):
        self.destroyElements(self.tk)
        self.drawScene(self.tk)


    def destroyElements(self, window):
        for item in window.winfo_children():
            print("Destroying Element", item)
            item.destroy()

    def drawScene(self, window):
        canvas = Canvas(window,width=300, height=300)
        canvas.pack()
        for i in range(1,5):
            canvas.create_line(0, 5, self.WIDTH, 5, fill="white", width=5)
        Button(self.tk,text="Restart The Game", command=self.playGame).pack()

