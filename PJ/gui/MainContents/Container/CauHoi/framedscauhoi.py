
from tkinter import CENTER, LEFT, Frame
from tkinter.ttk import Label

from gui.MainContents.Container.CauHoi.itemcauhoi import itemcauhoi


class FrameDanhSachCauHoi(Frame):

    def __init__(self, parent, title, postid):
        Frame.__init__(self, parent)
        self.parent = parent
        self.title = title
        self.postid = postid
        self.initUI()

        # self.danhsachcauhoi = parent.danhsachcauhoi

    def initUI(self):
        self.frameMain = Frame(self.parent.frameMain, padx=3, pady=3)
        self.frameMain.columnconfigure(index=0, weight=1)
        self.frameMain.grid(row=0, column=0, sticky='nsew')
        lbltieude = Label(self.frameMain, text=self.title,
                          padding=10, wraplength=500, justify=LEFT)
        lbltieude.grid(row=0, sticky='w')

    def loaddanhsachcauhoi(self, danhsachcauhoi):
        for i in range(len(danhsachcauhoi)):
            itemCauhoi =  itemcauhoi(self,danhsachcauhoi[i],i+1)
            
            # lblnoidung = Label(frameitem, text={danhsachcauhoi[i]['noidung']})

    def removeAll(self):
        for widget in self.frameMain.winfo_children():
            widget.destroy()

    def showSuaCauHoi(self, idcauhoi):
        self.parent.showDatCauHoi(self.postid,idcauhoi)
        
    def xoaCauHoi(self, idcauhoi):
        self.parent.xoaCauHoi(self.postid,self.title,idcauhoi)
    
    def showFormTraLoi(self,idcauhoi):
        self.parent.showFormTraLoi(idcauhoi,self.postid)