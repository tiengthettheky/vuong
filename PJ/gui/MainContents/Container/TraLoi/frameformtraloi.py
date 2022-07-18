from datetime import datetime
from tkinter import Button, Frame, Label, Toplevel,Text, messagebox

from models.cauTraLoiModel import TraLoiModel


class FormCauTraLoi(Frame):
    def __init__(self,parent, cauhoi):
        Frame.__init__(self, parent)

        self.cauhoi = cauhoi
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.newWindow = Toplevel(self.parent.parent)
        self.newWindow.title("Trả lời câu hỏi")
        self.newWindow.geometry("400x200")
        self.frameMain = Frame(self.newWindow, padx=3, pady=3)
        self.frameMain.columnconfigure(index=0, weight=1)
        self.frameMain.columnconfigure(index=1, weight=1)
        self.frameMain.grid(row=0, column=0, sticky='nsew')

        lbltieude = Label( self.frameMain, text='Tiêu đề câu hỏi:' ,padx=3,pady=3)
        lbltieude.grid(row=0, column=0, sticky='w')

        lbltieudecauhoi = Label( self.frameMain, text=self.cauhoi.tieude ,padx=3,pady=3)
        lbltieudecauhoi.grid(row=0, column=1, sticky='w')
        
        lbltraloi = Label( self.frameMain, text='Nội dung: ',padx=3,pady=3)
        lbltraloi.grid(row=1, column=0, sticky='w')

        self.txtnoidung = Text(self.frameMain,height=8, width=50)
        self.txtnoidung.grid(row=1, column=1, sticky='')

        btnsubmit = Button(self.frameMain,text="Trả lời",padx=10, pady=10,  command = lambda : self.submitTraLoi())
        btnhuy = Button(self.frameMain,text="Hủy",padx=10, pady=10,  command = lambda : self.huytraloi())
        btnsubmit.grid(row=2, column=0, sticky='w')
        btnhuy.grid(row=2, column=1, sticky='w')

    def submitTraLoi(self ):
        # id, cauhoiid, noidung, postid, datecreated
        noidung = self.txtnoidung.get("1.0",'end-1c')
        dscautraloi = self.parent.danhsachtraloi
        if(noidung == ""):
            return messagebox.showinfo("Thông báo", "Vui Lòng Nhập Thông Tin")
        idtrl = 0
        if(len(dscautraloi) == 0):
            idtrl = 1
        else:
            idtrl = int(dscautraloi[len(dscautraloi)-1].id) + 1
        traloi = TraLoiModel(idtrl, self.cauhoi.id,noidung,self.cauhoi.postid,datetime.now())
        self.parent.danhsachtraloi.append(traloi)
        self.parent.showdanhsachcauhoi( self.cauhoi.postid, self.cauhoi.tieude)
        self.huytraloi()

    def huytraloi(self):
        self.newWindow.destroy()
