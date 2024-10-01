import os
import pandas as pd

# Load the CSV files (adjust the file paths as needed)
skaters_csv = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores_skaters.csv'
goalies_csv = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores_goalies.csv'
scoring_csv = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores_scoring.csv'
penalties_csv = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores_penalties.csv'

skaters_df = pd.read_csv(skaters_csv)
goalies_df = pd.read_csv(goalies_csv)
scoring_df = pd.read_csv(scoring_csv)
penalties_df = pd.read_csv(penalties_csv)

# Group data by 'Game_ID' for all files
skaters_games = skaters_df.groupby('Game_ID')
goalies_games = goalies_df.groupby('Game_ID')
scoring_games = scoring_df.groupby('Game_ID')
penalties_games = penalties_df.groupby('Game_ID')

# Set the output directory where the HTML files will be saved
output_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores'

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate rows for skaters, goalies, scoring, and penalties tables
def generate_table_rows(data, column_mappings):
    rows = ""
    for _, row in data.iterrows():
        row_cells = ""
        for col, col_type in column_mappings.items():
            if col_type == 'team':
                row_cells += f'<td><a href="/teams/{row[col]}.html">{row[col]}</a></td>'
            elif col_type == 'player':
                row_cells += f'<td><a href="/players/{row[col]}.html">{row[col]}</a></td>'
            elif col_type == 'goalie':
                row_cells += f'<td><a href="/players/{row["Goalie_ID"]}.html">{row[col]}</a></td>'
            elif col_type == 'link':
                row_cells += f'<td><a href="/boxscores/{row["Game_ID"]}.html">{row[col]}</a></td>'
            else:
                row_cells += f"<td>{row[col]}</td>"
        rows += f"<tr>{row_cells}</tr>\n"
    return rows

# Column mappings for different tables
skaters_columns = {
    "Date": 'link', "Home Team": 'team', "Away Team": 'team', "Player": 'player', "Team": 'team', "G": 'value',
    "A": 'value', "PTS": 'value', "+/-": 'value', "PIM": 'value', "EVG": 'value', "PPG": 'value', "SHG": 'value',
    "GWG": 'value', "EV Assist": 'value', "PP Assist": 'value', "SH Assist": 'value', "SOG": 'value', "S%": 'value',
    "SHFT": 'value', "TOI": 'value', "iCF": 'value', "SAT‑F": 'value', "SAT‑A": 'value', "CF%": 'value', "CRel%": 'value',
    "ZSO": 'value', "ZSD": 'value', "oZS%": 'value', "HIT": 'value', "BLK": 'value'
}

goalies_columns = {
    "Home Team": 'team', "Away Team": 'team', "Goalie": 'goalie', "Team": 'team', "DEC": 'value', "GA": 'value',
    "SA": 'value', "SV": 'value', "SV%": 'value', "SO": 'value', "PIM": 'value', "Goalie TOI": 'value'
}

scoring_columns = {
    "Home Team": 'team', "Away Team": 'team', "Period": 'value', "Time": 'value', "Team": 'team', "Info": 'value',
    "Scorer": 'player', "Assist1": 'player', "Assist2": 'player'
}

penalties_columns = {
    "Home Team": 'team', "Away Team": 'team', "Period": 'value', "Time": 'value', "Team": 'team', "Player": 'player',
    "Penalty": 'value', "PIM": 'value'
}

# Loop through each Game_ID and generate an HTML file
for game_id, skaters_data in skaters_games:
    # Define the output HTML file path
    html_file_path = os.path.join(output_dir, f"{game_id}.html")

    # Build the skaters table rows
    skater_rows = generate_table_rows(skaters_data, skaters_columns)

    # Add the goalies table if available
    goalie_rows = ""
    if game_id in goalies_games.groups:
        goalies_data = goalies_games.get_group(game_id)
        goalie_rows = generate_table_rows(goalies_data, goalies_columns)

    # Add the scoring table if available
    scoring_rows = ""
    if game_id in scoring_games.groups:
        scoring_data = scoring_games.get_group(game_id)
        scoring_rows = generate_table_rows(scoring_data, scoring_columns)

    # Add the penalties table if available
    penalties_rows = ""
    if game_id in penalties_games.groups:
        penalties_data = penalties_games.get_group(game_id)
        penalties_rows = generate_table_rows(penalties_data, penalties_columns)

    # Create the complete HTML structure
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Game {game_id} Boxscore</title>
        <link rel="stylesheet" href="/assets/styles.css">
        <script src="/assets/searchBar.js" defer></script>
        <script src="/assets/tableSort.js"></script>
        <style>
            tr:hover {{background-color: #F0FFF0;}}
        </style>
    </head>
    <body>
        <nav id="navbar">
            <a href="/">Home</a>
            <a href="/players/">Players</a>
            <a href="/teams/">Teams</a>
            <a href="/leaders/">Leaders</a>
            <a href="/probabilities/">Probabilities</a>
            <a href="/boxscores/">Boxscores</a>
            <a href="/schedule/">Schedule</a>

            <div class="search-container">
                <input type="text" id="searchInput" placeholder="Search players or teams..." oninput="searchEntities()" />
                <ul id="suggestions"></ul>
            </div>
        </nav>

        <main id="content">
            <h1>Game {game_id} Boxscore</h1>

            <h2>Skaters</h2>
            <table id="{game_id}_skaters" border="1">
                <thead>
                    <tr>
                        <th>Date</th><th>Home Team</th><th>Away Team</th><th>Player</th><th>Team</th><th>G</th><th>A</th><th>PTS</th>
                        <th>+/-</th><th>PIM</th><th>EVG</th><th>PPG</th><th>SHG</th><th>GWG</th><th>EV Assist</th><th>PP Assist</th>
                        <th>SH Assist</th><th>SOG</th><th>S%</th><th>SHFT</th><th>TOI</th><th>iCF</th><th>SAT‑F</th><th>SAT‑A</th>
                        <th>CF%</th><th>CRel%</th><th>ZSO</th><th>ZSD</th><th>oZS%</th><th>HIT</th><th>BLK</th>
                    </tr>
                </thead>
                <tbody>
                    {skater_rows}
                </tbody>
            </table>

            <h2>Goalies</h2>
            <table id="{game_id}_goalies" border="1">
                <thead>
                    <tr>
                        <th>Home Team</th><th>Away Team</th><th>Goalie</th><th>Team</th><th>DEC</th><th>GA</th><th>SA</th><th>SV</th>
                        <th>SV%</th><th>SO</th><th>PIM</th><th>Goalie TOI</th>
                    </tr>
                </thead>
                <tbody>
                    {goalie_rows}
                </tbody>
            </table>

            <h2>Scoring</h2>
            <table id="{game_id}_scoring" border="1">
                <thead>
                    <tr>
                        <th>Home Team</th><th>Away Team</th><th>Period</th><th>Time</th><th>Team</th><th>Info</th>
                        <th>Scorer</th><th>Assist1</th><th>Assist2</th>
                    </tr>
                </thead>
                <tbody>
                    {scoring_rows}
                </tbody>
            </table>

            <h2>Penalties</h2>
            <table id="{game_id}_penalties" border="1">
                <thead>
                    <tr>
                        <th>Home Team</th><th>Away Team</th><th>Period</th><th>Time</th><th>Team</th><th>Player</th>
                        <th>Penalty</th><th>PIM</th>
                    </tr>
                </thead>
                <tbody>
                    {penalties_rows}
                </tbody>
            </table>
        </main>
    </body>
    </html>
    """

    # Write the HTML content to a file with UTF-8 encoding
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated HTML for Game_ID {game_id}")
