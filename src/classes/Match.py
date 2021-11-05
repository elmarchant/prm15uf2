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
        return str(self.date.day) + '-' + str(self.date.month) + '-' + str(self.date.year)

    def matchResult(self):
        return str(self.local.name) + ": " + str(self.local.goals) + " - " + str(self.visitor.name) + ": " + str(self.visitor.goals)

    def __str__(self) -> str:
        return self.getDate() + " | " + str(self.local.name) + " - " + str(self.visitor.name)