class Team:
    name = ""
    goals = 0
    possesion = 0
    attempts = 0
    onTarget = 0
    offTarget = 0
    blocked = 0
    corners = 0
    offsides = 0
    freekicks = 0
    saves = 0
    passAccuracy = 0
    passes = 0
    distanceCovered = 0
    yellowCard = 0
    yellowAndRed = 0
    red = 0

    def __init__(self, name):
        self.name = name

    def getPossesion(self):
        return self.possesion + "%"

    def setPossesion(self, posession = 50):
        if posession < 0:
            self.possesion = 0
        elif posession > 100:
            self.posession = 100
        else:
            self.posession = posession

    def setPosessionByOponent(self, oponent):
        self.posession = 100 - oponent.posession

    def getPassAccuracy(self):
        return self.passAccuracy + "%"

    def getDistanceCovered(self):
        return self.distanceCovered + "%"