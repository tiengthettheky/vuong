from datetime import datetime


class CauHoiModel:
    # Properties

    def __init__(self, id, tieude, noidung, postid, datecreated):
        self.id = id
        self.noidung = noidung
        self.tieude = tieude
        self.postid = postid
        self.datecreated = datecreated
        
    def SetCauHoi(self, id, tieude, noidung, postid, datecreated):
        self.id = id
        self.noidung = noidung
        self.tieude = tieude
        self.postid = postid
        self.datecreated = datecreated

    def ThayDoiThongTin(self, cauhoi):
        if(cauhoi.id == self.id):
            self.noidung = cauhoi.noidung
            self.postid = cauhoi.postid
            self.datecreated = cauhoi.datecreated

    def getthongtin(self):
        return CauHoiModel(self.id, self.tieude, self.noidung, self.postid, self.datecreated)