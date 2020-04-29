class Team():
    def __init__(self, name):
        self.name = name
        self.m_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0
    def win(self):
        self.m_played += 1
        self.wins += 1
        self.points += 3
    def draw(self):
        self.m_played += 1
        self.draws += 1
        self.points += 1
    def loss(self):
        self.m_played += 1
        self.losses += 1
    def __repr__(self):
        return "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}".format(
            self.name, self.m_played, self.wins, self.draws, self.losses, self.points)
    def __lt__(self, other):
        if self.points != other.points:
            return self.points < other.points
        else:
            return self.name > other.name

class Results:
    @staticmethod
    def draw(team1 : Team, team2 : Team):
        team1.draw()
        team2.draw()
    @staticmethod
    def win(team1 : Team, team2 : Team):
        team1.win()
        team2.loss()
    @staticmethod
    def loss(team1 : Team, team2 : Team):
        team1.loss()
        team2.win()

def tally(rows):
    Teams = {}
    for play in rows:
        play = play.split(";")
        team1 = play[0]
        team2 = play[1]
        result = play[2]
        if team1 not in Teams:
            Teams[team1] = Team(team1)
        if team2 not in Teams:
            Teams[team2] = Team(team2)
        getattr(Results, result)(Teams[team1], Teams[team2])
    headline = ["{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}".format("Team", "MP", "W", "D", "L", "P")]
    return headline + list(map(str, sorted(Teams.values(), reverse = True)))

if __name__ == "__main__":
    L = tally(["legia;lech;win",
    "jagiellonia;legia;loss",
    "legia;arka;win",
    "jagiellonia;arka;draw"])
    for x in L:
        print(x)
    