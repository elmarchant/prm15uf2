import datetime, Team
class Match:
    date = datetime.datetime.now()
    local = Team("local")
    visitor = Team("visitor")

    def __init__(self, local, visitor):
        self.local = local
        self.visitor = visitor

    def setDate(self, year, month, day):
        self.date = datetime.datetime(year, month, day)

    def matchResult(self):
        return self.local.name + ":" + self.local.goals + "-" + self.visitor.name + ":" + self.visitor.goals