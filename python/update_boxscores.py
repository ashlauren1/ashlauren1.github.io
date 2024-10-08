import os
import pandas as pd
from bs4 import BeautifulSoup

# Paths to your CSV files
skaters_csv = r'C:\Users\ashle\Documents\Projects\fixingtables\assets\boxscores_skaters.csv'
goalies_csv = r'C:\Users\ashle\Documents\Projects\fixingtables\assets\boxscores_goalies.csv'
scoring_csv = r'C:\Users\ashle\Documents\Projects\fixingtables\assets\boxscores_scoring.csv'
penalties_csv = r'C:\Users\ashle\Documents\Projects\fixingtables\assets\boxscores_penalties.csv'

# Path to boxscores folder
boxscores_folder = r'C:\Users\ashle\Documents\Projects\fixingtables\boxscores'

# Load CSV files into dataframes
skaters_df = pd.read_csv(skaters_csv)
goalies_df = pd.read_csv(goalies_csv)
scoring_df = pd.read_csv(scoring_csv)
penalties_df = pd.read_csv(penalties_csv)

# Helper function to generate links
def generate_team_link(team_id):
    return f'/teams/{team_id}.html'

def generate_player_link(player_id):
    return f'/players/{player_id}.html'

def generate_boxscore_link(game_id):
    return f'/boxscores/{game_id}.html'

# Function to generate HTML for each table
def generate_table_html(data, columns, hidden_cols, id_attr=None):
    table = BeautifulSoup('<table></table>', 'html.parser').new_tag('table', id=id_attr)
    thead = BeautifulSoup('<thead></thead>', 'html.parser').new_tag('thead')
    tr = BeautifulSoup('<tr></tr>', 'html.parser').new_tag('tr')
    
    for col in columns:
        th = BeautifulSoup('<th></th>', 'html.parser').new_tag('th')
        th.string = col
        tr.append(th)
    thead.append(tr)
    table.append(thead)

    tbody = BeautifulSoup('<tbody></tbody>', 'html.parser').new_tag('tbody')
    for _, row in data.iterrows():
        tr = BeautifulSoup('<tr></tr>', 'html.parser').new_tag('tr')
        for col in columns:
            td = BeautifulSoup('<td></td>', 'html.parser').new_tag('td')
            val = row[col]
            if col in hidden_cols:  # Skip hidden columns
                continue
            # Handle links for specific columns
            if col == 'Date':
                td.string = row[col]
                td['href'] = generate_boxscore_link(row['Game_ID'])
            elif col == 'Team':
                td.string = row['Team']
                td['href'] = generate_team_link(row['Team'])
            elif col == 'Player' or col == 'Goalie':
                td.string = row[col]
                td['href'] = generate_player_link(row[f"{col}_ID"])
            else:
                td.string = str(val)
            tr.append(td)
        tbody.append(tr)
    table.append(tbody)
    return str(table)

# Function to process each game's HTML file and update the content
def update_game_html(game_id):
    # Get data for the specific game
    skaters = skaters_df[skaters_df['Game_ID'] == game_id]
    goalies = goalies_df[goalies_df['Game_ID'] == game_id]
    scoring = scoring_df[scoring_df['Game_ID'] == game_id]
    penalties = penalties_df[penalties_df['Game_ID'] == game_id]

    # Determine file path for the game
    game_file_path = os.path.join(boxscores_folder, f'{game_id}.html')

    # Read the existing HTML file (if exists)
    if os.path.exists(game_file_path):
        with open(game_file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
    else:
        soup = BeautifulSoup('<html></html>', 'html.parser')

    # Update head section
    soup.head.clear()  # Clear existing head
    new_head = f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{skaters.iloc[0]['Away Team']} at {skaters.iloc[0]['Home Team']} {skaters.iloc[0]['Date']}</title>
    <link rel="stylesheet" href="/assets/styles.css">
    <script src="/assets/searchBar.js"></script>
    <script src="/assets/tableSort.js"></script>
    """
    soup.head.append(BeautifulSoup(new_head, 'html.parser'))

    # Update h1 and h2 tags
    away_team = skaters.iloc[0]['Away Team']
    home_team = skaters.iloc[0]['Home Team']
    date = skaters.iloc[0]['Date']

    # Create the h1 and h2 tags
    h1_tag = soup.new_tag('h1')
    h1_tag.string = f"{away_team} at {home_team}"
    
    h2_tag = soup.new_tag('h2')
    h2_tag.string = date

    # Add the h1 and h2 to the body
    soup.body.insert(0, h1_tag)
    soup.body.insert(1, h2_tag)

    # Move scoring and penalties tables to the top
    scoring_table = generate_table_html(scoring, scoring.columns, hidden_cols=['Game_ID'], id_attr='scoring')
    penalties_table = generate_table_html(penalties, penalties.columns, hidden_cols=['Game_ID'], id_attr='penalties')

    soup.body.insert(2, BeautifulSoup(scoring_table, 'html.parser'))
    soup.body.insert(3, BeautifulSoup(penalties_table, 'html.parser'))

    # Update skaters and goalies tables
    away_team_skaters = skaters[skaters['Skater\'s Team'] == away_team]
    home_team_skaters = skaters[skaters['Skater\'s Team'] == home_team]
    away_team_goalies = goalies[goalies['Team'] == away_team]
    home_team_goalies = goalies[goalies['Team'] == home_team]

    away_skaters_table = generate_table_html(away_team_skaters, skaters.columns, hidden_cols=['Game_ID', 'Player_ID'], id_attr=f'{away_team}_skaters')
    home_skaters_table = generate_table_html(home_team_skaters, skaters.columns, hidden_cols=['Game_ID', 'Player_ID'], id_attr=f'{home_team}_skaters')

    away_goalies_table = generate_table_html(away_team_goalies, goalies.columns, hidden_cols=['Game_ID', 'Goalie_ID'], id_attr=f'{away_team}_goalies')
    home_goalies_table = generate_table_html(home_team_goalies, goalies.columns, hidden_cols=['Game_ID', 'Goalie_ID'], id_attr=f'{home_team}_goalies')

    # Insert the tables into the HTML
    soup.body.append(BeautifulSoup(away_skaters_table, 'html.parser'))
    soup.body.append(BeautifulSoup(away_goalies_table, 'html.parser'))
    soup.body.append(BeautifulSoup(home_skaters_table, 'html.parser'))
    soup.body.append(BeautifulSoup(home_goalies_table, 'html.parser'))

    # Save the updated HTML file
    with open(game_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

# Iterate over all unique game IDs and update HTML files
unique_game_ids = skaters_df['Game_ID'].unique()

for game_id in unique_game_ids:
    update_game_html(game_id)

print("HTML files updated successfully!")
