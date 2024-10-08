import os
import pandas as pd

# Load the CSV file (adjust the file path as needed)
csv_file = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\gamelogs_teams.csv'
df = pd.read_csv(csv_file)

# Group data by the 'Team' column
teams = df.groupby('Team')

# Set the output directory where the HTML files will be saved
output_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\teams'

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each team and generate an HTML file
for team, team_data in teams:
    # Define the output HTML file path
    html_file_path = os.path.join(output_dir, f"{team}.html")

    # Build the table rows
    rows = ""
    for _, row in team_data.iterrows():
        date_link = f'<a href="/boxscores/{row["Game_ID"]}.html">{row["Date"]}</a>'
        team_link = f'<a href="/teams/{row["Team"]}.html">{row["Team"]}</a>'
        opp_link = f'<a href="/teams/{row["Opp"]}.html">{row["Opp"]}</a>'
        
        # Create each row
        rows += f"""
        <tr>
            <td>{row['Game']}</td>
            <td>{date_link}</td>
            <td>{team_link}</td>
            <td>{row['Location']}</td>
            <td>{opp_link}</td>
            <td>{row['G']}</td>
            <td>{row['GA']}</td>
            <td>{row['Result']}</td>
            <td>{row['OT/SO']}</td>
            <td>{row['SOG']}</td>
            <td>{row['PIM']}</td>
            <td>{row['SOGA']}</td>
            <td>{row['PIMA']}</td>
            <td>{row['CF at Even Strength']}</td>
            <td>{row['CA at Even Strength']}</td>
            <td>{row['CF% at Even Strength']}</td>
            <td>{row['FF at Even Strength']}</td>
            <td>{row['FA at Even Strength']}</td>
            <td>{row['FF% at Even Strength']}</td>
            <td>{row['FOW at Even Strength']}</td>
            <td>{row['FOL at Even Strength']}</td>
        </tr>
        """

    # Create the complete HTML structure
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{team} Stats</title>
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
            <h1>{team} Gamelogs</h1>
            <table border="1">
                <thead>
                    <tr>
                        <th>Game</th>
                        <th>Date</th>
                        <th>Team</th>
                        <th>Location</th>
                        <th>Opponent</th>
                        <th>G</th>
                        <th>GA</th>
                        <th>Result</th>
                        <th>OT/SO</th>
                        <th>SOG</th>
                        <th>PIM</th>
                        <th>SOGA</th>
                        <th>PIMA</th>
                        <th>CF at Even Strength</th>
                        <th>CA at Even Strength</th>
                        <th>CF% at Even Strength</th>
                        <th>FF at Even Strength</th>
                        <th>FA at Even Strength</th>
                        <th>FF% at Even Strength</th>
                        <th>FOW at Even Strength</th>
                        <th>FOL at Even Strength</th>
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

    print(f"Generated HTML for team {team}")
