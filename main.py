from lib.leagueData import LeagueData
from lib.requestHelper import RequestHelper

data = LeagueData()

print(data.getTeams())

permutations = data.getTeamsPermutation()


print(permutations)

helper = RequestHelper()

print(helper.getHeadToHeadData(1, 18))