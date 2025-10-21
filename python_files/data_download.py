import requests
import pandas as pd

# Example: Get general player data
url = "https://fantasy.premierleague.com/api/bootstrap-static/"
data = requests.get(url).json()

players = pd.DataFrame(data['elements'])   # All player info
teams = pd.DataFrame(data['teams'])        # Teams info
events = pd.DataFrame(data['events'])      # Gameweek info

players.to_csv("players.csv", index=False)
teams.to_csv("teams.csv", index=False)
events.to_csv("events.csv", index=False)




