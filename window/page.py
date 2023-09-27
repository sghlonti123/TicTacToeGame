from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image


class Window:
    WIDTH = 400
    HEIGHT = 480
    SIZE=f"{WIDTH}x{HEIGHT}"
    tk = Tk()
    line_color = "white"
    globalCanvas = None
    user_side = "x"

    def __init__(self):
        self.tk.geometry(self.SIZE)
        self.tk.title("Tic Tac Toe")
        Button(self.tk,text="Start Game", command=self.playGame).pack()
        mainloop()

    def playGame(self):
        self.destroyElements(self.tk)
        self.globalCanvas = self.drawScene(self.tk)
        self.globalCanvas.bind("<Button-1>", self.inputSymbol)




    def destroyElements(self, window):
        for item in window.winfo_children():
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
            if width_index==0:
                canvas.create_line(5, 0, 0, height, fill=self.line_color, width=5)
            else:
                canvas.create_line(width_index*100, 0, width_index*100, height, fill=self.line_color, width=5)
        Button(window,text="Restart The Game", command=self.playGame).pack()
        Button(window,text="Exit", command=quit).pack()
        return canvas

    def inputSymbol(self, event):
        if event.x < 100 and event.y < 100:
            self.insert_image(self.globalCanvas, 30, 30)
        elif event.y < 100 < event.x < 200:
            self.insert_image(self.globalCanvas, 130, 30)
        elif event.y < 100 < event.x < 300:
            self.insert_image(self.globalCanvas, 230, 30)
        elif event.x < 100 < event.y < 200:
            self.insert_image(self.globalCanvas, 30, 130)
        elif 100 < event.x < 200 and 100 < event.y < 200:
            self.insert_image(self.globalCanvas, 130, 130)
        elif 100 < event.y < 200 < event.x :
            self.insert_image(self.globalCanvas, 230, 130)
        elif event.x < 100 < 200 < event.y < 300:
            self.insert_image(self.globalCanvas, 30, 230)
        elif 100 < event.x < 200 < event.y < 300:
            self.insert_image(self.globalCanvas, 130, 230)
        elif 200 < event.x < 300 and 200 < event.y < 300:
            self.insert_image(self.globalCanvas, 230, 230)

    def insert_image(self, canvas, x, y, symbol=user_side):
        print("inserts image at coordinates", x, y, symbol)
        img = ImageTk.PhotoImage(Image.open(f"resources/{symbol}.png"))
        canvas.create_image(x, y, anchor=NW, image=img).pack()