import pandas as pd

players = pd.read_csv("players.csv")

players['cost_millions'] = players['now_cost'] / 10

players['value'] = players['total_points'] / players['cost_millions']

top_value_players = players[['first_name', 'second_name', 'cost_millions', 'total_points', 'value']] \
    .sort_values(by="value", ascending=False) \
    .head(10)

top_value_goalkeepers = players[players['element_type'] == 1][['first_name', 'second_name', 'cost_millions', 'total_points', 'value']] \
    .sort_values(by="value", ascending=False) \
    .head(10)

top_value_defenders = players[players['element_type'] == 2][['first_name', 'second_name', 'cost_millions', 'total_points', 'value']] \
    .sort_values(by="value", ascending=False) \
    .head(10)

top_value_midfielders = players[players['element_type'] == 3][['first_name', 'second_name', 'cost_millions', 'total_points', 'value']] \
    .sort_values(by="value", ascending=False) \
    .head(10)

top_value_attackers = players[players['element_type'] == 4][['first_name', 'second_name', 'cost_millions', 'total_points', 'value']] \
    .sort_values(by="value", ascending=False) \
    .head(10)

print("Top 10 best value players (points per £m):")
print("")
print(top_value_players)

print("")
print("Top 10 best value goalkeepers (points per £m):")
print("")
print(top_value_goalkeepers)

print("")
print("Top 10 best value defenders (points per £m):")
print("")
print(top_value_defenders)

print("")
print("Top 10 best value midfielders (points per £m):")
print("")
print(top_value_midfielders)

print("")
print("Top 10 best value attackers (points per £m):")
print("")
print(top_value_attackers)
