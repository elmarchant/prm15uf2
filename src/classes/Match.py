import datetime
from src.classes.Team import Team
class Match:
    date = datetime.datetime.now()
    local = Team("local")
    visitor = Team("visitor")

    def __init__(self, local = Team("local"), visitor = Team("visitor")):
        self.local = local
        self.visitor = visitor

    def setDate(self, year, month, day):
        self.date = datetime.datetime(year, month, day)

    def getDate(self) -> str:
        month = str(self.date.month)
        day = str(self.date.day)
        
        if self.date.month < 10:
            month = '0' + month
        
        if self.date.day < 10:
            day = '0' + day

        return  day + '-' + month + '-' + str(self.date.year)

    def matchResult(self):
        return str(self.local.name) + ": " + str(self.local.goals) + " - " + str(self.visitor.name) + ": " + str(self.visitor.goals)

    def getID(self) -> str:
        return self.getDate() + " | " + str(self.local.name) + " - " + str(self.visitor.name)
    
    def __equal__(self, other) -> bool:
        if self.getID() == other.getID():
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.getID()