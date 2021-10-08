#_author_= JH  (AMDG) 9/28/21

Team1_wins = int(input("team 1 number of wins"))
Team1_ties = int(input("team 1 number of ties"))
Team2_wins = int(input("team 2 number of wins"))
Team2_ties = int(input("team 2 number of ties"))

T1_points = int(Team1_wins * 3) + int(Team1_ties)
T2_points = int(Team2_wins * 3) + int(Team2_ties)\

if T1_points > T2_points:
    print("Team 1 wins")
else:
    print("Team 2 wins")

