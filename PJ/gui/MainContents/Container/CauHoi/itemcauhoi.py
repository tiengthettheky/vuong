from tkinter import LEFT, Button, Frame, Label



class itemcauhoi(Frame):
    def __init__(self, parent,item, idx):
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI(item,idx)

    def initUI(self,item,idx):
        frameitem = Frame(self.parent.frameMain, borderwidth=1,
                          relief="solid", padx=3, pady=3)
        frameitem.grid(row=idx, sticky='nwne')

        lbltieude = Label(frameitem, text='tiêu đề:')
        lbltieude.grid(row=0, sticky='w')

        lbltieudetext = Label(
            frameitem, text=str(item.tieude))
        lbltieudetext.grid(row=0,column= 1, columnspan=2, sticky='w')

        lblngay = Label(frameitem, text='ngày tạo:')
        lblngay.grid(row=2, sticky='w')

        lblngaytext = Label(frameitem, text=str(
            item.datecreated),wraplength=500, justify=LEFT)
        lblngaytext.grid(row=2,column= 1, columnspan=2, sticky='w')

        lblnoidung = Label(frameitem, text='nội dung:')
        lblnoidung.grid(row=1, sticky='w')

        lblnoidungtext = Label(
            frameitem, text=str(item.noidung),wraplength=500, justify=LEFT)
        lblnoidungtext.grid(row=1,column= 1, columnspan=2, sticky='w')

        btnsuacauhoi = Button(frameitem, text="Sửa", command = lambda c=item :  self.suacauhoi(item.id))
        btnsuacauhoi.grid(row=3, column=0, sticky='w')
        
        btntraloi = Button(frameitem, text="Trả lời", command = lambda :  self.traloicauhoi(item.id))
        btntraloi.grid(row=3, column=1, sticky='w')
        
        btntraloi = Button(frameitem, text="Xóa", command = lambda c=item  :  self.xoacauhoi(item.id))
        btntraloi.grid(row=3, column=2, sticky='w')

        dscautraloi = self.locautraloicuacauhoi(item.id) 
        if(len(dscautraloi)>0):
            frametraloimain = Frame(frameitem,borderwidth=1,relief="solid")
            frametraloimain.grid(row=4, columnspan=3, sticky='nwne')
            for i in range(len(dscautraloi)) :
                frametraloiitem = Frame(frametraloimain,borderwidth=1,relief="solid")
                frametraloiitem.grid(row=i,sticky='nwne')
                lblngay = Label(frametraloiitem, text='ngày trả lời:')
                lblngay.grid(row=0, sticky='w')

                lblngayvalue = Label(frametraloiitem, text=dscautraloi[i].datecreated)
                lblngayvalue.grid(row=0,column= 1,sticky='w')

                lblnoidung = Label(frametraloiitem, text='nội dung')
                lblnoidung.grid(row=1,column= 0, sticky='w')

                lblnoidungvalue = Label(frametraloiitem, text=dscautraloi[i].noidung,wraplength=500, justify=LEFT)
                lblnoidungvalue.grid(row=1,column= 1,sticky='w')

        
    def suacauhoi(self,idcauhoi):
        self.parent.showSuaCauHoi(idcauhoi)
        

    def traloicauhoi(self,idcauhoi):
        self.parent.showFormTraLoi(idcauhoi)
       
    
    def xoacauhoi(self,idcauhoi):
        self.parent.xoaCauHoi(idcauhoi)

    def locautraloicuacauhoi(self,idcauhoi):
        arrNew = []
        dscautraloi = self.parent.parent.danhsachtraloi
        for i in range(len(dscautraloi)):
            if(dscautraloi[i].cauhoiid == idcauhoi):
                arrNew.append(dscautraloi[i])
        return arrNew