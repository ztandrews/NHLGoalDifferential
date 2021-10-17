'''
@auth: ztandrews

NHL Goal Differential Grpahs
--------Instructions--------
- Enter the abbreviation for your team in the 'team' variable
- Enter the year that you want to see
- Run
'''

from sportsipy.nhl.schedule import Schedule
from sportsipy.nhl.teams import Team
import matplotlib.pyplot as plt

# Enter team abbreivation here
team = "NYI"
year = "2021"
chosen_team = Team(team)
team_name = chosen_team.name
team_schedule = Schedule(team,year)
game_nums = []
differentials = []
game_num = 0

# The next for loop will check to see if a game has been played yet
# If a game has been played, the goals_scored var will be an integer
# If a game has not been played, its type will be 'NoneType'
games = []
for game in team_schedule:
    if (type(game.goals_scored) == int):
        games.append(game)
    else:
        continue

while game_num < len(games):
    diff = games[game_num].goals_scored - games[game_num].goals_allowed
    differentials.append(diff)
    game_nums.append(game_num)
    game_num += 1

# Style the chart
title_font = {'family': 'normal',
              'weight': 'normal',
              'size': 30}
axis_font = {'family': 'normal',
             'weight': 'normal',
             'size': 25}
col = []
for d in differentials:
    if d < 0:
        col.append('#ff1919')
    else:
        col.append('#00b300')
amt_games = str(game_num)
plt.figure(figsize=(30, 20))
plt.ylim(-6, 6)
plt.title(year + " " + team_name + '\n' + amt_games + " Games Played", fontdict=title_font)
plt.ylabel("Goal Differential", fontdict=axis_font)
plt.xlabel("Game Number", fontdict=axis_font)
plt.bar(game_nums, differentials, color=col)
plt.show()