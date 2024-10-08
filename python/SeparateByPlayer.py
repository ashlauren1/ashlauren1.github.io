import os
import pandas as pd

# File paths
input_folder = r'C:\Users\ashle\Documents\Projects\statscopy\tables'
output_folder = r'C:\Users\ashle\Documents\Projects\statscopy\players'

# Load CSV files with UTF-8 encoding
gamelogs_skaters_df = pd.read_csv(os.path.join(input_folder, 'gamelogs_skaters.csv'), encoding='utf-8')
totals_skaters_df = pd.read_csv(os.path.join(input_folder, 'seasontotals_skaters.csv'), encoding='utf-8')

# Helper functions for creating links
def create_team_link(team):
    return f'<a href="/teams/{team}.html">{team}</a>'

def create_opp_link(opp):
    return f'<a href="/teams/{opp}.html">{opp}</a>'

def create_game_link(date, game_id):
    return f'<a href="/boxscores/{game_id}.html">{date}</a>'

def create_player_link(player, player_id):
    return f'<a href="/players/{player_id}.html">{player}</a>'

# Function to generate the HTML header
def create_html_header(player_name):
    title = f"{player_name} Stats 2023-24"
    header = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="/assets/styles.css">
<script src="/assets/searchBar.js"></script>
<script src="/assets/tableSort.js"></script>
</head>
<body>
<nav id="navbar">
<ul>
<li><a href="/">Home</a></li>
<li><a href="/players/">Players</a></li>
<li><a href="/teams/">Teams</a></li>
<li><a href="/probabilities/">Probabilities</a></li>
<li><a href="/boxscores/">Boxscores</a></li>
<li><a href="/versus/">Head to Head Stats</a></li>
<li><a href="/leaders/">Leaders</a></li>
<li><a href="/seasons/2025/schedule.html">Schedule and Results</a></li>
<li><a href="/seasons/2025/standings.html">Current Standings</a></li>
<li><a href="/seasons/2025/rosters.html">Team Rosters</a></li>
<li>
<input type="text" id="searchBar" placeholder="Search for players or teams..." oninput="performSearch()" autocomplete="off">
<div id="searchResults" class="dropdown"></div>
<button id="searchButton" onclick="handleSearch()">Search</button>
</li>
</ul>
</nav>
<main id="content">
<div class="gamelog">
"""
    return header

# Function to create the season totals table for a specific player
def create_totals_table(df, player_id):
    totals_df = df[df['PlayerID'] == player_id]
    table_html = '<table id="totals">\n<tr><th>Team</th><th>GP</th><th>G</th><th>A</th><th>PTS</th><th>SOG</th><th>HIT</th><th>BLK</th><th>PIM</th><th>TOI</th><th>ATOI</th><th>S%</th><th>EVG</th><th>PPG</th><th>SHG</th><th>GWG</th><th>EVA</th><th>PPA</th><th>SHA</th></tr>\n'
    for _, row in totals_df.iterrows():
        team_link = create_team_link(row['Team'])
        table_html += f"<tr><td>{team_link}</td><td>{row['GP']}</td><td>{row['G']}</td><td>{row['A']}</td><td>{row['PTS']}</td><td>{row['SOG']}</td><td>{row['HIT']}</td><td>{row['BLK']}</td><td>{row['PIM']}</td><td>{row['TOI']}</td><td>{row['ATOI']}</td><td>{row['S%']}</td><td>{row['EVG']}</td><td>{row['PPG']}</td><td>{row['SHG']}</td><td>{row['GWG']}</td><td>{row['EVA']}</td><td>{row['PPA']}</td><td>{row['SHA']}</td></tr>\n"
    table_html += '</table>\n'
    return table_html

# Function to create the game log table for a specific player
def create_skaters_gamelog_table(df, player_id):
    skater_df = df[df['PlayerID'] == player_id]
    table_html = f'<table id="{player_id}_gamelog">\n<tr><th>Date</th><th>Player</th><th>Team</th><th>Location</th><th>Opp</th><th>Result</th><th>OT/SO</th><th>G</th><th>A</th><th>PTS</th><th>SOG</th><th>HIT</th><th>BLK</th><th>TOI</th><th>PIM</th><th>S%</th><th>EVG</th><th>PPG</th><th>SHG</th><th>GWG</th><th>EVA</th><th>PPA</th><th>SHA</th></tr>\n'
    for _, row in skater_df.iterrows():
        game_link = create_game_link(row['Date'], row['GameID'])
        player_link = create_player_link(row['Player'], row['PlayerID'])
        team_link = create_team_link(row['Team'])
        opp_link = create_opp_link(row['Opp'])
        table_html += f"<tr><td>{game_link}</td><td>{player_link}</td><td>{team_link}</td><td>{row['Location']}</td><td>{opp_link}</td><td>{row['Result']}</td><td>{row['OT/SO']}</td><td>{row['G']}</td><td>{row['A']}</td><td>{row['PTS']}</td><td>{row['SOG']}</td><td>{row['HIT']}</td><td>{row['BLK']}</td><td>{row['TOI']}</td><td>{row['PIM']}</td><td>{row['S%']}</td><td>{row['EVG']}</td><td>{row['PPG']}</td><td>{row['SHG']}</td><td>{row['GWG']}</td><td>{row['EVA']}</td><td>{row['PPA']}</td><td>{row['SHA']}</td></tr>\n"
    table_html += '</table>\n'
    return table_html

# Function to write data to HTML files
def write_to_html(player_id, player_name, tables):
    header = create_html_header(player_name)
    file_path = os.path.join(output_folder, f"{player_id}.html")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(header)
        for table in tables:
            file.write(table)
        file.write('</div>\n</main>\n</body>\n</html>')

# Process each unique player in the gamelogs or totals data
unique_players = pd.concat([gamelogs_skaters_df[['PlayerID', 'Player']], totals_skaters_df[['PlayerID', 'Player']]]).drop_duplicates()

for _, player_row in unique_players.iterrows():
    player_id = player_row['PlayerID']
    player_name = player_row['Player']

    # Generate the season totals and game log tables for the player
    skaters_total_table = create_totals_table(totals_skaters_df, player_id)
    skaters_gamelog_table = create_skaters_gamelog_table(gamelogs_skaters_df, player_id)

    # Combine tables and write to the player's HTML file
    tables = [skaters_total_table, skaters_gamelog_table]
    write_to_html(player_id, player_name, tables)
