
from tkinter import BOTTOM, CENTER, RAISED, TOP, Frame, Label, StringVar


class TopBar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="red")
        self.parent = parent
        self.initUI()

    def initUI(self):
        frame = Frame(self.parent,bg='cyan', width=450, height=50, pady=3 )

        frame.grid(row=0, sticky="ew")
        label = Label(frame, text='Hỗ Trợ Đầu Tư', anchor=CENTER)
        label.pack()
        # var = StringVar()
        # label = Label( frame, textvariable=var, font=(15) )

        # var.set("Hỗ trợ đầu tư")
        # label.pack(side = BOTTOM )


        