

import json
from tkinter import BOTTOM, LEFT, RAISED, TOP, Button, Frame, Label, StringVar
from urllib import response

from modules.utils.utils import getAPI

class SideBar(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background="red")
        self.parent = parent
        self.btns = []
        self.controller = controller
        self.initUI()
        
    
    def clickdanhmuc(self,item):
        self.controller.LoadPostByCate(item)

   
    def LoadMenu(self):
        url = "/category/api/get-all"
        response =  getAPI(url,None)
        arrDanhMuc = response.json()
        
        for i in range(len(arrDanhMuc)):
            self.btns.append(Button(frame, text=arrDanhMuc[i]['name'], font=(15), command= lambda c=arrDanhMuc[i] : self.clickdanhmuc(c)))
            # button = Button( frame,text = item['name'], font=(15), command= lambda: print(self.item['name']) )
            self.btns[i].pack(anchor="w")



    def initUI(self):
        global frame
        frame = Frame(self.parent, width=100,bg='red', padx=3, pady=3)

        frame.grid(row=0,column=0, sticky="nsew")
        self.LoadMenu()     
        
        # for i in range(3):
        #     var = StringVar()
        #     label = Label( frame, textvariable=var, font=(15) )
        #     var.set("Hỗ trợ đầu tư")
        #     label.pack( )
        # var = StringVar()
        # label = Label( frame, textvariable=var, font=(15) )

        # var.set("Hỗ trợ đầu tư")
        # label.pack(side = BOTTOM )
    
    



        