import os
import pandas as pd

# Load the CSV file (adjust the file path as needed)
csv_file = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores_skaters.csv'
df = pd.read_csv(csv_file)

# Group data by the 'Game_ID' column
games = df.groupby('Game_ID')

# Set the output directory where the HTML files will be saved
output_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores'

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each Game_ID and generate an HTML file
for game_id, game_data in games:
    # Define the output HTML file path
    html_file_path = os.path.join(output_dir, f"{game_id}.html")

    # Build the table rows
    rows = ""
    for _, row in game_data.iterrows():
        date_link = f'<a href="/boxscores/{row["Game_ID"]}.html">{row["Date"]}</a>'
        home_team_link = f'<a href="/teams/{row["Home Team"]}.html">{row["Home Team"]}</a>'
        away_team_link = f'<a href="/teams/{row["Away Team"]}.html">{row["Away Team"]}</a>'
        player_link = f'<a href="/players/{row["Player_ID"]}.html">{row["Player"]}</a>'
        team_link = f'<a href="/teams/{row["Team"]}.html">{row["Team"]}</a>'

        # Create each row
        rows += f"""
        <tr>
            <td>{date_link}</td>
            <td>{home_team_link}</td>
            <td>{away_team_link}</td>
            <td>{player_link}</td>
            <td>{team_link}</td>
            <td>{row['G']}</td>
            <td>{row['A']}</td>
            <td>{row['PTS']}</td>
            <td>{row['+/-']}</td>
            <td>{row['PIM']}</td>
            <td>{row['EVG']}</td>
            <td>{row['PPG']}</td>
            <td>{row['SHG']}</td>
            <td>{row['GWG']}</td>
            <td>{row['EV Assist']}</td>
            <td>{row['PP Assist']}</td>
            <td>{row['SH Assist']}</td>
            <td>{row['SOG']}</td>
            <td>{row['S%']}</td>
            <td>{row['SHFT']}</td>
            <td>{row['TOI']}</td>
            <td>{row['iCF']}</td>
            <td>{row['SAT‑F']}</td>
            <td>{row['SAT‑A']}</td>
            <td>{row['CF%']}</td>
            <td>{row['CRel%']}</td>
            <td>{row['ZSO']}</td>
            <td>{row['ZSD']}</td>
            <td>{row['oZS%']}</td>
            <td>{row['HIT']}</td>
            <td>{row['BLK']}</td>
        </tr>
        """

    # Create the complete HTML structure
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Game {game_id} Boxscore</title>
        <link rel="stylesheet" href="/assets/styles.css"> <!-- Assuming a shared stylesheet -->
        <script src="/assets/searchBar.js" defer></script>
        <script src="/assets/tableSort.js"></script>
        <style>
            tr:hover {{background-color: #F0FFF0;}}
        </style>
    </head>
    <body>
        <!-- Navigation Bar -->
        <nav id="navbar">
            <a href="/">Home</a>
            <a href="/players/">Players</a>
            <a href="/teams/">Teams</a>
            <a href="/leaders/">Leaders</a>
            <a href="/probabilities/">Probabilities</a>
            <a href="/boxscores/">Boxscores</a>
            <a href="/schedule/">Schedule</a>

            <!-- Search Bar -->
            <div class="search-container">
                <input type="text" id="searchInput" placeholder="Search players or teams..." oninput="searchEntities()" />
                <ul id="suggestions"></ul> <!-- This will show the search suggestions -->
            </div>
        </nav>

        <main id="content">
            <h1>Game {game_id} Boxscore</h1>
            <table border="1">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Home Team</th>
                        <th>Away Team</th>
                        <th>Player</th>
                        <th>Team</th>
                        <th>G</th>
                        <th>A</th>
                        <th>PTS</th>
                        <th>+/-</th>
                        <th>PIM</th>
                        <th>EVG</th>
                        <th>PPG</th>
                        <th>SHG</th>
                        <th>GWG</th>
                        <th>EV Assist</th>
                        <th>PP Assist</th>
                        <th>SH Assist</th>
                        <th>SOG</th>
                        <th>S%</th>
                        <th>SHFT</th>
                        <th>TOI</th>
                        <th>iCF</th>
                        <th>SAT‑F</th>
                        <th>SAT‑A</th>
                        <th>CF%</th>
                        <th>CRel%</th>
                        <th>ZSO</th>
                        <th>ZSD</th>
                        <th>oZS%</th>
                        <th>HIT</th>
                        <th>BLK</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
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
