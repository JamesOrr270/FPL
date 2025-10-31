import pandas as pd

players = pd.read_csv("players.csv")

players['cost_millions'] = players['now_cost'] / 10

players['value'] = players['total_points'] / players['cost_millions']

position_map = {
    1: "Goalkeeper",
    2: "Defender",
    3: "Midfielder",
    4: "Forward"
}
players['position'] = players['element_type'].map(position_map)

print("Welcome to the FPL Scout!\n")
print("Choose a position:")
print("1 = Goalkeeper, 2 = Defender, 3 = Midfielder, 4 = Forward")
pos_choice = int(input("Enter a number (1–4): "))
budget = float(input("Enter your budget in £m (e.g. 6.0): "))

filtered = players[(players['element_type'] == pos_choice) & 
                   (players['cost_millions'] <= budget)]

best_options_value = filtered[['first_name', 'second_name', 'position', 
                         'cost_millions', 'total_points', 'value']] \
    .sort_values(by="value", ascending=False) \
    .head(10)

best_options_points = filtered[['first_name', 'second_name', 'position', 
                         'cost_millions', 'total_points', 'value']] \
    .sort_values(by="total_points", ascending=False) \
    .head(10)

print(f"\nTop {position_map[pos_choice]}s under £{budget:.1f}m:")
print(best_options_points)

print(f"\nTop value {position_map[pos_choice]}s under £{budget:.1f}m:")
print(best_options_value)


