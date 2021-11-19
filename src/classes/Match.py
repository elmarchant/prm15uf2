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
    
    def displayHighLights(self) -> None:
        print(self.local.name, self.visitor.name, sep=" - ")
        print(self.local.goals, self.visitor.goals, sep=" goals ")
        print(self.local.attempts, self.visitor.attempts, sep=" attempts ")
        print(self.local.onTarget, self.visitor.onTarget, sep=" on target ")
        print(str(self.local.possesion)+"%", str(self.visitor.possesion)+"%", sep=" possession % ")
        print(self.local.passes, self.visitor.passes, sep=" passes ")
        print(str(self.local.passAccuracy)+"%", str(self.visitor.passAccuracy)+"%", sep=" pass accuracy %")
        print(self.local.yellowCard, self.visitor.yellowCard, sep=" yellow cards ")
        print(print(self.local.red, self.visitor.red, sep=" red cards "))

        

    def __eq__(self, other: object) -> bool:
        if self.getID() == other.getID():
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.getID()