from lib.util import getTeamsFromCSV, getRelativePath
import itertools

class LeagueData:

    def __init__(self):
        # { int : string }
        self.__teams = getTeamsFromCSV(getRelativePath("support/1920_team_id.csv"))

    def getTeams(self):
        return self.__teams

    # [ ( int, int ) ]
    def getTeamsPermutation(self):
        # get all matches combination in terms of teams_id tuple, (home_team_id, away_team_id)
        return list(itertools.permutations(list(self.getTeams().keys()), 2))

