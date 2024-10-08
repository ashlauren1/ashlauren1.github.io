import os
import pandas as pd

# File paths
input_folder = r'C:\Users\ashle\Documents\Projects\statscopy\tables'
output_folder = r'C:\Users\ashle\Documents\Projects\statscopy\players'

# Load the goalfinder CSV file with UTF-8 encoding
goalfinder_df = pd.read_csv(os.path.join(input_folder, 'goalfinder.csv'), encoding='utf-8')

# Helper functions to create links
def create_game_link(date, game_id):
    return f'<a href="/boxscores/{game_id}.html">{date}</a>'

def create_player_link(player, player_id):
    return f'<a href="/players/{player_id}.html">{player}</a>'

def create_team_link(team):
    return f'<a href="/teams/{team}.html">{team}</a>'

def create_opp_link(opp):
    return f'<a href="/teams/{opp}.html">{opp}</a>'

# Function to create the scoring table for a specific player
def create_scoring_table(df, player_id):
    relevant_df = df[(df['ScorerID'] == player_id) | (df['Assist1ID'] == player_id) | 
                     (df['Assist2ID'] == player_id) | (df['GoalieID'] == player_id)]
    
    if relevant_df.empty:
        return None  # Return None if the player is not involved in any scoring events
    
    table_html = '<table id="scoring">\n<tr><th>Date</th><th>Team</th><th>Location</th><th>Opp</th><th>Result</th><th>Scorer</th><th>Assist1</th><th>Assist2</th><th>Goalie</th><th>Time</th></tr>\n'
    for _, row in relevant_df.iterrows():
        date_link = create_game_link(row['Date'], row['GameID'])
        team_link = create_team_link(row['Team'])
        opp_link = create_opp_link(row['Opp'])
        scorer_link = create_player_link(row['Scorer'], row['ScorerID'])
        assist1_link = create_player_link(row['Assist1'], row['Assist1ID'])
        assist2_link = create_player_link(row['Assist2'], row['Assist2ID'])
        goalie_link = create_player_link(row['Goalie'], row['GoalieID'])
        
        table_html += f"<tr><td>{date_link}</td><td>{team_link}</td><td>{row['Location']}</td><td>{opp_link}</td><td>{row['Result']}</td><td>{scorer_link}</td><td>{assist1_link}</td><td>{assist2_link}</td><td>{goalie_link}</td><td>{row['Time']}</td></tr>\n"
    table_html += '</table>\n'
    return table_html

# Function to append the scoring table to the player's HTML file
def append_scoring_table_to_html(player_id, scoring_table_html):
    file_path = os.path.join(output_folder, f"{player_id}.html")
    if not os.path.exists(file_path):
        return  # Skip if the player's HTML file does not exist

    # Read the existing HTML file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Insert the scoring table before the closing </main> tag
    new_content = content.replace('</main>', scoring_table_html + '\n</main>')

    # Write the updated content back to the HTML file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Process each unique player involved in the scoring data
player_ids = pd.concat([goalfinder_df['ScorerID'], goalfinder_df['Assist1ID'], 
                        goalfinder_df['Assist2ID'], goalfinder_df['GoalieID']]).unique()

for player_id in player_ids:
    scoring_table_html = create_scoring_table(goalfinder_df, player_id)
    if scoring_table_html:
        append_scoring_table_to_html(player_id, scoring_table_html)
