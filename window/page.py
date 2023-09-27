from tkinter import *
from tkinter.ttk import *


class Window:
    WIDTH = 400
    HEIGHT = 480
    SIZE=f"{WIDTH}x{HEIGHT}"
    tk = Tk()
    line_color = "white"

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
        height = self.HEIGHT-80
        canvas = Canvas(window,width=300, height=300)
        canvas.pack()
        # Draw horizontal lines
        for height_index in range(4):
            if height_index==0:
                canvas.create_line(0, 5, self.WIDTH, 5, fill=self.line_color, width=5)
            else:
                canvas.create_line(0, height_index*100, self.WIDTH, height_index*100, fill=self.line_color, width=5)

        # Draw vertical lines
        for width_index in range(4):
            print(height, width_index)
            if width_index==0:
                canvas.create_line(5, 0, 0, height, fill=self.line_color, width=5)
            else:
                canvas.create_line(width_index*100, 0, width_index*100, height, fill=self.line_color, width=5)
        Button(window,text="Restart The Game", command=self.playGame).pack()
        Button(window,text="Exit", command=quit).pack()