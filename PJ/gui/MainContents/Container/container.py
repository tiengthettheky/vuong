
from datetime import datetime
from re import X
from tkinter import BOTTOM, CENTER, END, LEFT, NS, NSEW, RAISED, RIGHT, S, TOP, W, Y, Button, Frame, Label, Text, messagebox
from urllib import request
from tkinterhtml import HtmlFrame
from gui.MainContents.Container.CauHoi.formdatcauhoi import formdatcauhoi
from gui.MainContents.Container.CauHoi.framedscauhoi import FrameDanhSachCauHoi
from gui.MainContents.Container.TraLoi.frameformtraloi import FormCauTraLoi
from models.cauHoiModel import CauHoiModel
from modules.utils.srcollbarFrame import ScrollableFrame

from modules.utils.utils import cleanhtml, getAPI


class ContainerFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.danhsachcauhoi = []
        self.danhsachtraloi = []

    def LoadPostByCate(self, item):
        self.removeAll()
        # self.frameMain =  ScrollableFrame(self.parent)
        # self.frameMain.grid(row=1,sticky='ns')
        page = 1
        size = 10
        self.idcate = str(item.get('id'))
        url = "/post/api/get-by-cate?id={0}&page={1}&limit={2}&sort=ASC".format(
            self.idcate, page, size)

        response = getAPI(url, None).json()
        self.posts = response
        for idx in range(len(response['data'])):
            self.renderItemPost(idx, response['data'][idx])

    def renderItemPost(self, idex, item):
        frame = Frame(self.frameMain, borderwidth=1,
                      relief="solid", pady=5, padx=5)
        frame.grid(row=idex, sticky='ew')
        labeltieude = Label(
            frame, text=item['title'], wraplength=500, justify=LEFT)
        labeltieude.grid(row=0,  sticky=W)
        framebtn = Frame(frame, borderwidth=1, pady=5, padx=5)
        framebtn.grid(row=1, sticky=W)
        btnDatCauHoi = Button(framebtn, text="Đặt câu hỏi", padx=10, width=10, pady=10,
                              command=lambda c=item: self.showDatCauHoi(str(item['id']), None))
        btnxemcauhoi = Button(framebtn, text="Xem Câu Hỏi", padx=10, width=10, pady=10,
                              command=lambda c=item: self.showdanhsachcauhoi(str(item['id']), str(item['title'])))
        btnDatCauHoi.grid(row=0, column=1, sticky=W)
        btnxemcauhoi.grid(row=0, column=2, sticky=W)
        labeltieude.bind(
            "<Button-1>", lambda c=item: self.xemchitiet(str(item['content']), str(item['title'])))

    def xemchitiet(self, content, title):
        self.removeAll()
        frame = Frame(self.frameMain, borderwidth=1, relief="solid", pady=3)
        frame.grid(row=0, column=0, sticky='nsew')
        labelTitle = Label(frame, text=title, wraplength=500, justify=LEFT)
        labelContent = Label(frame, text=cleanhtml(
            content), wraplength=500, justify=LEFT)
        labelTitle.pack()
        labelContent.pack()

    def removeAll(self):
        for widget in self.frameMain.winfo_children():
            widget.destroy()

    def initUI(self):
        self.frameMain = Frame(self.parent, padx=3, pady=3)
        self.frameMain.grid(row=0, column=1, sticky='nsew')
        self.frameMain.columnconfigure(index=0, weight=1)

    def showDatCauHoi(self, idPost, idcauhoi):
        """Hiển thị form đặt câu hỏi """
        self.removeAll()
        cauhoi = None
        if(idcauhoi is not None):
            cauhoi = self.timcauhoi(idcauhoi)
            print(cauhoi)

        formcauhoi = formdatcauhoi(self, idPost, cauhoi)

    def submitCauHoi(self, idPost, tieude, noidung, idcauhoi):
        if(idcauhoi is None):
            id = 0
            if(len(self.danhsachcauhoi) == 0):
                id = 1
            else:
                id = int(self.danhsachcauhoi[len(self.danhsachcauhoi)-1].id) + 1
            cauhoi = CauHoiModel(id, tieude, noidung, idPost, datetime.now())
            self.danhsachcauhoi.append(cauhoi)
            messagebox.showinfo("Thông báo", "Thêm Thành Công")
        else:
            id = idcauhoi
            for i in range(len(self.danhsachcauhoi)):
                if(self.danhsachcauhoi[i].id == id):
                    cauhoi = CauHoiModel(
                        id, tieude, noidung, idPost, datetime.now())
                    self.danhsachcauhoi[i] = cauhoi
                    break
            messagebox.showinfo("Thông báo", "Thay Đổi Thành Công")

    def huydatcauhoi(self):
        self.removeAll()
        for idx in range(len(self.posts['data'])):
            self.renderItemPost(idx, self.posts['data'][idx])

    def showdanhsachcauhoi(self, idpost, title):
        self.removeAll()
        self.frameDSCauHoi = FrameDanhSachCauHoi(self, title, idpost)

        self.frameDSCauHoi.loaddanhsachcauhoi(
            self.timcauhoitheobaiviet(idpost))

    def timcauhoi(self, idcauhoi):
        for i in range(len(self.danhsachcauhoi)):
            if(self.danhsachcauhoi[i].id == idcauhoi):
                return self.danhsachcauhoi[i]

    def timcauhoitheobaiviet(self, idpost):
        dsnew = []
        for i in range(len(self.danhsachcauhoi)):
            if(self.danhsachcauhoi[i].postid == idpost):
                dsnew.append(self.danhsachcauhoi[i])
        return dsnew

    def xoaCauHoi(self,idpost,title,idcauhoi):
        for i in range(len(self.danhsachcauhoi)):
            if(self.danhsachcauhoi[i].id == idcauhoi):
                self.danhsachcauhoi.remove(self.danhsachcauhoi[i])
                break
        self.showdanhsachcauhoi(idpost, title)
    
    def showFormTraLoi(self,idcauhoi,postid):
        self.formtraloi = FormCauTraLoi(self,self.timcauhoi(idcauhoi))
       
    