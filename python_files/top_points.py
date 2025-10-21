import requests
import pandas as pd

players = pd.read_csv("players.csv")

top_players = players[['first_name', 'second_name', 'now_cost', 'total_points']] \
                .sort_values(by="total_points", ascending=False) \
                .head(10)

top_goalkeepers = players[players['element_type'] == 1][['first_name', 'second_name', 'now_cost', 'total_points']] \
                .sort_values(by="total_points", ascending=False) \
                .head(10)

top_defenders = players[players['element_type'] == 2][['first_name', 'second_name', 'now_cost', 'total_points']] \
                .sort_values(by="total_points", ascending=False) \
                .head(10)

top_midfielders = players[players['element_type'] == 3][['first_name', 'second_name', 'now_cost', 'total_points']] \
                .sort_values(by="total_points", ascending=False) \
                .head(10)

top_attackers = players[players['element_type'] == 4][['first_name', 'second_name', 'now_cost', 'total_points']] \
                .sort_values(by="total_points", ascending=False) \
                .head(10)

print("Top 10 players by points:")
print("")
print(top_players)

print("")
print("Top 10 Goalkeepers:")
print("")
print(top_goalkeepers)

print("")
print("Top 10 Defenders:")
print("")
print(top_defenders)

print("")
print("Top 10 Midfielders:")
print("")
print(top_midfielders)

print("")
print("Top 10 Attackers:")
print("")
print(top_attackers)


