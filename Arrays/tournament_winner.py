"""
  There's an algorithms tournament taking place in which teams of programmers
  compete against each other to solve algorithmic problems as fast as possible.
  Teams compete in a round robin, where each team faces off against all other
  teams. Only two teams compete against each other at a time, and for each
  competition, one team is designated the home team, while the other team is the
  away team. In each competition there's always one winner and one loser; there
  are no ties. A team receives 3 points if it wins and 0 points if it loses. The
  winner of the tournament is the team that receives the most amount of points.

  Given an array of pairs representing the teams that have competed against each
  other and an array containing the results of each competition, write a
  function that returns the winner of the tournament. The input arrays are named
  competitions and results respectively. The competitions array has elements in the form of
  [homeTeam, awayTeam], where each team is a string of at most 30
  characters representing the name of the team. The results array
  contains information about the winner of each corresponding competition in the competitions
  array. Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results array
  means that the home team in the corresponding competition won and a 0 means that the away team won.

  It's guaranteed that exactly one team will win the tournament and that each
  team will compete against all other teams exactly once. It's also guaranteed
  that the tournament will always have at least two teams.
"""

# Basic approach
# Time: O(n) | Space: O(n)
############################
# Set teams = empty dictionary
# Set index as 0
# Loop through every competition
#   Get the result from results array with index
#   Get the home team and away team names from competition array
#   If result = 0
#       Add 3 to away team in teams dictionary
#   else
#       Add 3 to home team in teams dictionary
#   increment index by 1
#   Set winner = key with max value in teams dictionary
# return winner
#############################


def tournamentWinner(competitions, results):
    # Write your code here.
    i = 0
    teams = {}
    for competition in competitions:
        result = results[i]
        home_team = competition[0]
        away_team = competition[1]
        if result == 0:
            if away_team in teams:
                teams[away_team] += 3
            else:
                teams[away_team] = 3
        else:
            if home_team in teams:
                teams[home_team] += 3
            else:
                teams[home_team] = 3
        i += 1
    winner = max(teams, key=teams.get)
    return winner


