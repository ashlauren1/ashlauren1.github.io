import pandas as pd
import json

# Load your CSV files
games_df = pd.read_csv('C:\Users\ashle\Documents\Projects\New folder\gameinfo.csv')
skaters_df = pd.read_csv('C:\Users\ashle\Documents\Projects\New folder\boxscores_skaters.csv')
goalies_df = pd.read_csv('C:\Users\ashle\Documents\Projects\New folder\boxscores_goalies.csv')
scoring_df = pd.read_csv('C:\Users\ashle\Documents\Projects\New folder\boxscores_scoring.csv')
penalties_df = pd.read_csv('C:\Users\ashle\Documents\Projects\New folder\boxscores_penalties.csv')

# Convert data to a structured JSON format
games = []

# Assume 'boxscores_skaters.csv' has a 'Game_ID' column to group data
unique_game_ids = games_df['GameID'].unique()

for game_id in unique_game_ids:
    game_data = {
        "game_id": game_id,
        "date": games_df.loc[games_df['GameID'] == game_id, 'Date'].values[0],
        "teams": {
            "home": games_df.loc[games_df['GameID'] == game_id, 'HomeID'].values[0],
            "away": games_df.loc[games_df['GameID'] == game_id, 'AwayID'].values[0]
        },
        "players": {}  # Populate with player stats later
    }
    games.append(game_data)

# Write to JSON file
with open('gamedata.json', 'w') as outfile:
    json.dump({"games": games}, outfile, indent=4)

print("Data successfully converted to JSON format!")
