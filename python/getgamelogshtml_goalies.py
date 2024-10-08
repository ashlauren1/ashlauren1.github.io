import os
import pandas as pd

# Define the directory where the files will be saved
output_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\players'

# Read the CSV file
csv_file = 'gamelogs_goalies.csv'
df = pd.read_csv(csv_file)

# Group the data by Player_ID
grouped = df.groupby('Player_ID')

# Loop through each group (goalie) and create an HTML file
for player_id, group in grouped:
    player_name = group['Player'].iloc[0]
    file_path = os.path.join(output_dir, f"{player_id}.html")

    # Start building the HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{player_name}</title>
  <link rel="stylesheet" href="/assets/styles.css">
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

  <h1>{player_name} - Gamelogs</h1>
  <table border="1">
    <thead>
      <tr>
        <th>Season</th>
        <th>Date</th>
        <th>Team</th>
        <th>Location</th>
        <th>Opponent</th>
        <th>Result</th>
        <th>GA</th>
        <th>SA</th>
        <th>SV</th>
        <th>SV%</th>
        <th>TOI</th>
      </tr>
    </thead>
    <tbody>
    """

    # Loop through the rows of the group to create the table rows
    for _, row in group.iterrows():
        season_link = f'<a href="/schedule/{row["Season"]}.html">{row["Season"]}</a>'
        date_link = f'<a href="/boxscores/{row["Game_ID"]}.html">{row["Date"]}</a>'
        team_link = f'<a href="/teams/{row["Team"]}.html">{row["Team"]}</a>'
        opp_link = f'<a href="/teams/{row["Opp"]}.html">{row["Opp"]}</a>'
        
        # Construct each row of the table
        html_content += f"""
        <tr>
          <td>{season_link}</td>
          <td>{date_link}</td>
          <td>{team_link}</td>
          <td>{row["Location"]}</td>
          <td>{opp_link}</td>
          <td>{row["Result"]}</td>
          <td>{row["GA"]}</td>
          <td>{row["SA"]}</td>
          <td>{row["SV"]}</td>
          <td>{row["SV%"]}</td>
          <td>{row["TOI"]}</td>
        </tr>
        """

    # Close the table and the HTML tags
    html_content += """
    </tbody>
  </table>
</body>
</html>
    """

    # Write the HTML content to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated {file_path}")
    

print("All files have been generated.")
