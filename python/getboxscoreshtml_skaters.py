import os
import pandas as pd

# Load the CSV file (adjust the file path as needed)
skaters_csv = r'C:\Users\ashle\Documents\Projects\fixingtables\assets\boxscores_skaters.csv'
skaters_df = pd.read_csv(skaters_csv)

# Group data by the 'Game_ID' column
games = df.groupby('Game_ID')

# Set the output directory where the HTML files will be saved
output_dir = r'C:\Users\ashle\Documents\Projects\fixingtables\boxscore'

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
        team_link = f'<a href="/teams/{row["Team"]}.html">{row["Team"]}</a>'
        player_link = f'<a href="/players/{row["Player_ID"]}.html">{row["Player"]}</a>'

        # Create each row
        rows += f"""
        <tr>
            <td>{date_link}</td>
            <td>{team_link}</td>
            <td>{player_link}</td>
            <td>{row['G']}</td>
            <td>{row['A']}</td>
            <td>{row['PTS']}</td>
            <td>{row['SOG']}</td>
            <td>{row['HIT']}</td>
            <td>{row['BLK']}</td>
            <td>{row['PIM']}</td>
            <td>{row['TOI']}</td>
            <td>{row['SHFT']}</td>
            <td>{row['EVG']}</td>
            <td>{row['PPG']}</td>
            <td>{row['SHG']}</td>
            <td>{row['EVA']}</td>
            <td>{row['PPA']}</td>
            <td>{row['SHA']}</td>
            <td>{row['iCF']}</td>
            <td>{row['SAT‑F']}</td>
            <td>{row['SAT‑A']}</td>
            <td>{row['CF%']}</td>
            <td>{row['CRel%']}</td>
        </tr>
        """

    # Create the complete HTML structure
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{skaters.iloc[0]['Away Team']} at {skaters.iloc[0]['Home Team']} {skaters.iloc[0]['Date']}</title>
        <link rel="stylesheet" href="/assets/styles.css"> <!-- Assuming a shared stylesheet -->
        <script src="/assets/searchBar.js"></script>
        <script src="/assets/tableSort.js"></script>
    .
    </head>
    <body>
    
    <!-- Navigation Bar -->
    <nav id="navbar">
      <ul>
        <li><a href="/">Home</a></li>
	    <li><a href="/players/">Players</a></li>
	    <li><a href="/teams/">Teams</a></li>
	    <li><a href="/leaders/">Leaders</a></li>
	    <li><a href="/probabilities/">Probabilities</a></li>
	    <li><a href="/boxscores/">Boxscores</a></li>
	    <li><a href="/schedule/">Schedule</a></li>
	<!-- Search Bar -->
    <div class="search-container">
	    <li>
        <input type="text" id="searchBar" placeholder="Search for players or teams..." oninput="performSearch()" autocomplete="off">
        <div id="searchResults" class="dropdown"></div>
        <button id="searchButton" onclick="handleSearch()">Search</button>
        </li>
      </ul>
    </nav>
    
    <main id="content">
    
    <h1>{away_team} at {home_team}</h1>
    <h2>{date}</h2>
    
    <table>
    <thead>
      <tr>
        <th>Date</th>
        <th>Team</th>
        <th>Player</th>
        <th>G</th>
        <th>A</th>
        <th>PTS</th>
        <th>SOG</th>
        <th>HIT</th>
        <th>BLK</th>
        <th>PIM</th>
        <th>TOI</th>
        <th>SHFT</th>
        <th>EVG</th>
        <th>PPG</th>
        <th>SHG</th>
        <th>EVA</th>
        <th>PPA</th>
        <th>SHA</th>
        <th>iCF</th>
        <th>SAT‑F</th>
        <th>SAT‑A</th>
        <th>CF%</th>
        <th>CRel%</th>
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

    # Update skaters tables
    away_team_skaters = skaters[skaters['Team'] == away_team]
    home_team_skaters = skaters[skaters['Team'] == home_team]

    away_skaters_table = generate_table_html(away_team_skaters, skaters.columns, hidden_cols=['Game_ID', 'Player_ID'], id_attr=f'{away_team}_skaters')
    home_skaters_table = generate_table_html(home_team_skaters, skaters.columns, hidden_cols=['Game_ID', 'Player_ID'], id_attr=f'{home_team}_skaters')

    # Insert the tables into the HTML
    soup.body.append(BeautifulSoup(away_skaters_table, 'html.parser'))
    soup.body.append(BeautifulSoup(home_skaters_table, 'html.parser'))


# Iterate over all unique game IDs and update HTML files
unique_game_ids = skaters_df['Game_ID'].unique()

for game_id in unique_game_ids:
    update_game_html(game_id)

    # Write the HTML content to a file with UTF-8 encoding
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated HTML for Game_ID {game_id}")
