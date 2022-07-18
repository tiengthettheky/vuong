from tkinter import *
from gui.MainContents.Container.container import ContainerFrame
from gui.MainContents.SideBar.sidebar import SideBar

from gui.MainContents.TopBar.topbar import TopBar
from modules.utils.utils import *

from modules.pj_config import ProjectConfig

window = Tk()
window.title(ProjectConfig["ProjectName"])

#Đặt kích thước của cửa sổ
window.geometry('800x600')

window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=4)
window.grid_rowconfigure(0,weight=1)
# window.wm_attributes('-transparentcolor','black')

#top_frame
# topbar =  TopBar(window)

container = ContainerFrame(window)
sidebar =  SideBar(window,container)


window.mainloop()

# Link tham khảo
# https://www.journaldev.com/48165/tkinter-working-with-classes