import datetime

class Match:
    date = datetime.datetime.now()
    localName = ""
    visitorName = ""

    def __init__(self, localName, visitorName):
        self.localName = localName
        self.visitorName = visitorName

    def setDate(self, year, month, day):
        self.date = datetime.datetime(year, month, day)