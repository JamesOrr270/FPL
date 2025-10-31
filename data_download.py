import requests
import pandas as pd

url = "https://fantasy.premierleague.com/api/bootstrap-static/"
data = requests.get(url).json()

players = pd.DataFrame(data['elements'])  
teams = pd.DataFrame(data['teams'])        
events = pd.DataFrame(data['events'])      

players.to_csv("players.csv", index=False)
teams.to_csv("teams.csv", index=False)
events.to_csv("events.csv", index=False)




