from datetime import datetime


class TraLoiModel:
    # Properties

    def __init__(self, id, cauhoiid, noidung, postid, datecreated):
        self.id = id
        self.noidung = noidung
        self.cauhoiid = cauhoiid
        self.postid = postid
        self.datecreated = datecreated
        
    def SetCauTraLoi(self, id, cauhoiid, noidung, postid, datecreated):
        self.id = id
        self.noidung = noidung
        self.cauhoiid = cauhoiid
        self.postid = postid
        self.datecreated = datecreated

    def ThayDoiThongTin(self, cautraloi):
        if(cautraloi.id == self.id):
            self.noidung = cautraloi.noidung
            self.postid = cautraloi.postid
            self.datecreated = cautraloi.datecreated
