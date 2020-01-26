import csv
import os

# read teams from csv
def getTeamsFromCSV(path):
    teams_dict = {}

    with open(path) as csvfile:
        teams = csv.DictReader(csvfile)
        for team in teams:
            if int(team['tournament_id']) in [ 1, 150 ]:
                teams_dict[int(team['team_id'])] = team['name']
    
    return teams_dict

# get relative path
def getRelativePath(path):
    script_dir = os.path.dirname(__file__)

    return os.path.join(script_dir, path)
    