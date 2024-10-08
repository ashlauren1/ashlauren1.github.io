import os
import pandas as pd

# File paths
input_folder = r'C:\Users\ashle\Documents\Projects\statscopy\tables'
output_folder = r'C:\Users\ashle\Documents\Projects\statscopy\boxscores'

# Load CSV files with UTF-8 encoding
gameinfo_df = pd.read_csv(os.path.join(input_folder, 'gameinfo.csv'), encoding='utf-8')
boxscores_skaters_df = pd.read_csv(os.path.join(input_folder, 'boxscores_skaters.csv'), encoding='utf-8')
boxscores_goalies_df = pd.read_csv(os.path.join(input_folder, 'boxscores_goalies.csv'), encoding='utf-8')
boxscores_scoring_df = pd.read_csv(os.path.join(input_folder, 'boxscores_scoring.csv'), encoding='utf-8')
boxscores_penalties_df = pd.read_csv(os.path.join(input_folder, 'boxscores_penalties.csv'), encoding='utf-8')

# Helper function to create team links
def create_team_link(team):
    return f'<a href="/teams/{team}.html">{team}</a>'

# Helper function to create player links
def create_player_link(player, player_id):
    return f'<a href="/players/{player_id}.html">{player}</a>'

# Function to generate the HTML header and scorebox for each game
def create_html_header(game_row):
    title = f"{game_row['Away']} at {game_row['Home']}: {game_row['Date']}"
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
<div class="scorebox">
<div class="team"><div>{create_team_link(game_row['AwayID'])}</div><div class="score">{game_row['AwayG']}</div></div>
<div class="team"><div>{create_team_link(game_row['HomeID'])}</div><div class="score">{game_row['HomeG']}</div></div>
<div class="date">{game_row['Date']}</div>
</div>
"""
    return header

# Function to create skaters table filtered by GameID and team
def create_skaters_table(df, game_id, team, table_id):
    team_df = df[(df['GameID'] == game_id) & (df['Team'] == team)]
    table_html = f'<table id="{table_id}_skaters">\n<tr><th>Team</th><th>Player</th><th>G</th><th>A</th><th>PTS</th><th>SOG</th><th>HIT</th><th>BLK</th><th>TOI</th><th>PIM</th><th>SAT-F</th><th>SAT-A</th><th>CF%</th><th>CRel%</th></tr>\n'
    for _, row in team_df.iterrows():
        player_link = create_player_link(row['Player'], row['PlayerID'])
        team_link = create_team_link(row['Team'])
        table_html += f"<tr><td>{team_link}</td><td>{player_link}</td><td>{row['G']}</td><td>{row['A']}</td><td>{row['PTS']}</td><td>{row['SOG']}</td><td>{row['HIT']}</td><td>{row['BLK']}</td><td>{row['TOI']}</td><td>{row['PIM']}</td><td>{row['SAT-F']}</td><td>{row['SAT-A']}</td><td>{row['CF%']}</td><td>{row['CRel%']}</td></tr>\n"
    table_html += '</table>\n'
    return table_html

# Function to create goalies table filtered by GameID and team
def create_goalies_table(df, game_id, team, table_id):
    team_df = df[(df['GameID'] == game_id) & (df['Team'] == team)]
    table_html = f'<table id="{table_id}_goalies">\n<tr><th>Team</th><th>Goalie</th><th>DEC</th><th>GA</th><th>SA</th><th>SV</th><th>SV%</th><th>SO</th><th>PIM</th><th>TOI</th></tr>\n'
    for _, row in team_df.iterrows():
        player_link = create_player_link(row['Goalie'], row['PlayerID'])
        team_link = create_team_link(row['Team'])
        table_html += f"<tr><td>{team_link}</td><td>{player_link}</td><td>{row['DEC']}</td><td>{row['GA']}</td><td>{row['SA']}</td><td>{row['SV']}</td><td>{row['SV%']}</td><td>{row['SO']}</td><td>{row['PIM']}</td><td>{row['TOI']}</td></tr>\n"
    table_html += '</table>\n'
    return table_html

# Function to create scoring table filtered by GameID
def create_scoring_table(df, game_id):
    game_df = df[df['GameID'] == game_id]
    table_html = '<table id="scoring">\n<tr><th>Team</th><th>Time</th><th>Info</th><th>Scorer</th><th>Assist 1</th><th>Assist 2</th></tr>\n'
    for _, row in game_df.iterrows():
        team_link = create_team_link(row['Team'])
        scorer_link = create_player_link(row['Scorer'], row['ScorerID'])
        assist1_link = create_player_link(row['Assist 1'], row['Assist1ID'])
        assist2_link = create_player_link(row['Assist 2'], row['Assist2ID'])
        table_html += f"<tr><td>{team_link}</td><td>{row['Time']}</td><td>{row['Info']}</td><td>{scorer_link}</td><td>{assist1_link}</td><td>{assist2_link}</td></tr>\n"
    table_html += '</table>\n'
    return table_html

# Function to create penalties table filtered by GameID
def create_penalties_table(df, game_id):
    game_df = df[df['GameID'] == game_id]
    table_html = '<table id="penalties">\n<tr><th>Team</th><th>Time</th><th>Player</th><th>Penalty</th><th>PIM</th></tr>\n'
    for _, row in game_df.iterrows():
        team_link = create_team_link(row['Team'])
        player_link = create_player_link(row['Player'], row['PlayerID'])
        table_html += f"<tr><td>{team_link}</td><td>{row['Time']}</td><td>{player_link}</td><td>{row['Penalty']}</td><td>{row['PIM']}</td></tr>\n"
    table_html += '</table>\n'
    return table_html

# Function to write data to HTML files
def write_to_html(game_id, header, tables):
    file_path = os.path.join(output_folder, f"{game_id}.html")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(header)
        for table in tables:
            file.write(table)
        file.write('</main>\n</body>\n</html>')

# Process each game in gameinfo.csv
for _, game_row in gameinfo_df.iterrows():
    game_id = game_row['GameID']
    header = create_html_header(game_row)

    # Generate tables filtered by GameID and team
    skaters_table_away = create_skaters_table(boxscores_skaters_df, game_id, game_row['AwayID'], game_row['AwayID'])
    skaters_table_home = create_skaters_table(boxscores_skaters_df, game_id, game_row['HomeID'], game_row['HomeID'])
    goalies_table_away = create_goalies_table(boxscores_goalies_df, game_id, game_row['AwayID'], game_row['AwayID'])
    goalies_table_home = create_goalies_table(boxscores_goalies_df, game_id, game_row['HomeID'], game_row['HomeID'])
    scoring_table = create_scoring_table(boxscores_scoring_df, game_id)
    penalties_table = create_penalties_table(boxscores_penalties_df, game_id)

    # Combine tables
    tables = [skaters_table_away, skaters_table_home, goalies_table_away, goalies_table_home, scoring_table, penalties_table]

    # Write to HTML file
    write_to_html(game_id, header, tables)
