class FootballTeam:
    name = ""
    number_of_players = 0
    head_coach = ""
    continent = ""

    def __init__(self, name = "FC None" ) -> None:
        self.name = name
        self.head_coach = "Unknown"
        
    def __eq__(self, other: object) -> bool:
        if self.name == other.name:
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.name

class National(FootballTeam):
    country = ""

    def __init__(self, name="Selección de Fútbol de España") -> None:
        super().__init__(name=name)

    def setCountry(self, country) -> None:
        self.country = country

class Club(FootballTeam):
    league = ""
    academy = False

    def __init__(self, name="FC Barcelona") -> None:
        super().__init__(name=name)

    def setLeague(self, league) -> None:
        self.league = league

    def switchAcademy(self) -> None:
        self.academy = not self.academy