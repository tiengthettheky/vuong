
from tkinter import CENTER, Button, Frame, Label,Text, messagebox

from models.cauHoiModel import CauHoiModel


class formdatcauhoi(Frame):
    def __init__(self, parent, idPost, cauhoi):
        Frame.__init__(self, parent)
        self.parent = parent
        self.cauhoi = None
        if(cauhoi is not None):
            self.cauhoi = cauhoi
            
        self.initUI(idPost)

    def initUI(self, idPost):
        frame = Frame(self.parent.frameMain, borderwidth=1,
                       relief="solid", pady=5, padx=5)
        frame.grid(row=0,column=0,sticky='nsew')
        tieude = Label(frame, text='Đặt Câu Hỏi',  justify=CENTER)
        lblvande = Label(frame, text="Tiêu đề")
        lblnoidung = Label(frame, text="Nội dung")
        
        self.txttieude = Text(frame,height=1, width=50)
        self.txtnoidung = Text(frame,height=8, width=50)
        
        btnsubmit = Button(frame,text="Đặt câu hỏi",padx=10, pady=10,  command = lambda : self.submitCauHoi(idPost, None if (self.cauhoi is None ) else  self.cauhoi.id  ))
        btnhuy = Button(frame,text="Hủy",padx=10, pady=10,  command = lambda : self.parent.huydatcauhoi())
        
        tieude.grid(row=0, columnspan=2)
        lblvande.grid(row=1, column=0)
        self.txttieude.grid(row=1, column=1)
        lblnoidung.grid(row=2, column=0)
        self.txtnoidung.grid(row=2, column=1)
        btnsubmit.grid(row=3, column=0)
        btnhuy.grid(row=3, column=1)
        if(self.cauhoi is not None):
            btnsubmit['text'] = "Thay đổi"
            self.txttieude.insert("end-1c",self.cauhoi.tieude)
            self.txtnoidung.insert("end-1c",self.cauhoi.noidung)
    
    def submitCauHoi(self,idPost,idcauhoi):
        tieude =  self.txttieude.get("1.0",'end-1c')
        noidung = self.txtnoidung.get("1.0",'end-1c')
        if(tieude == "" or noidung == "" ):
            return messagebox.showinfo("Thông báo", "Vui Lòng Nhập Thông Tin")
        else:     
            self.parent.submitCauHoi(idPost,tieude,noidung,idcauhoi)