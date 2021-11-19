import pandas, json
from src.classes.Match import Match
from src.classes.Team import Team
import datetime

class LoadMatchData:
    data = []
    games = []

    def __init__(self, file):
        df = pandas.read_csv(file)
        self.data = json.loads(df.to_json(orient="records"))
        self.getData()
        
    def getData(self):
        games = []

        for i1 in self.data:
            for i2 in self.data:
                if i1['Date'] == i2['Date']:
                    if i1['Team'] == i2['Opponent'] and i1['Opponent'] == i2['Team']:
                        if not ((i1['Date'] + " | " + i1['Team'] + " - " + i1['Opponent']) in games or (i2['Date'] + " | " + i2['Team'] + " - " + i2['Opponent']) in games):
                            local = Team(i1['Team'])
                            visitor = Team(i2['Team'])

                            local.goals = i1['Goal Scored']
                            local.possesion = i1['Ball Possession %']
                            local.attempts = i1['Attempts']
                            local.onTarget = i1['On-Target']
                            local.offTarget = i1['Off-Target']
                            local.blocked = i1['Blocked']
                            local.corners = i1['Corners']
                            local.offsides = i1['Offsides']
                            local.freekicks = i1['Free Kicks']
                            local.saves = i1['Saves']
                            local.passAccuracy = i1['Pass Accuracy %']
                            local.passes = i1['Passes']
                            local.distanceCovered = i1['Distance Covered (Kms)']
                            local.yellowCard = i1['Yellow Card']
                            local.yellowAndRed = i1['Yellow & Red']
                            local.red = i1['Red']

                            visitor.goals = i2['Goal Scored']
                            visitor.possesion = i2['Ball Possession %']
                            visitor.attempts = i2['Attempts']
                            visitor.onTarget = i2['On-Target']
                            visitor.offTarget = i2['Off-Target']
                            visitor.blocked = i2['Blocked']
                            visitor.corners = i2['Corners']
                            visitor.offsides = i2['Offsides']
                            visitor.freekicks = i2['Free Kicks']
                            visitor.saves = i2['Saves']
                            visitor.passAccuracy = i2['Pass Accuracy %']
                            visitor.passes = i2['Passes']
                            visitor.distanceCovered = i2['Distance Covered (Kms)']
                            visitor.yellowCard = i2['Yellow Card']
                            visitor.yellowAndRed = i2['Yellow & Red']
                            visitor.red = i2['Red']

                            date = i1['Date'].split("-")
                            
                            match = Match(local, visitor)
                            match.setDate(int(date[2]), int(date[1]), int(date[0]))
                            
                            self.games.append(match)
                            games.append(i1['Date'] + " | " + i1['Team'] + " - " + i1['Opponent'])
                            
    def getMatchById(self, id) -> Match:
        match = Match()

        for item in self.games:
            if item.getID() == id:
                match = item
                break

        return match

    def getGames(self):
        return self.games