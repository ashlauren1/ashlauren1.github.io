import os
import pandas as pd
from bs4 import BeautifulSoup

# Define file paths
players_folder = r"C:\Users\ashle\Documents\Projects\ashlauren1.github.io\players"
gamelogs_file = "gamelogs_skaters.csv"

# Load the CSV file
gamelogs_df = pd.read_csv(gamelogs_file)

# Replace NaN with empty strings
gamelogs_df = gamelogs_df.fillna("")

# Define the navigation bar HTML
navbar_html = '''
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
'''

# Function to generate HTML for each player
def generate_player_html(player_id, player_name, gamelog_data):
    # Create a new BeautifulSoup HTML structure
    soup = BeautifulSoup(features="html.parser")

    # Add the document structure
    doc_type = soup.new_tag("!DOCTYPE", lang="en")
    soup.append(doc_type)

    html = soup.new_tag("html", lang="en")
    soup.append(html)

    head = soup.new_tag("head")
    html.append(head)

    # Add meta and title tags
    meta_charset = soup.new_tag("meta", charset="UTF-8")
    meta_viewport = soup.new_tag("meta", attrs={"name": "viewport", "content": "width=device-width, initial-scale=1.0"})
    title_tag = soup.new_tag("title")
    title_tag.string = f"{player_name} Profile"
    
    # Append to the head tag
    head.append(meta_charset)
    head.append(meta_viewport)
    head.append(title_tag)
    
    # Link to CSS and JS files
    head.append(soup.new_tag("link", rel="stylesheet", href="/assets/styles.css"))
    head.append(soup.new_tag("script", src="/assets/searchBar.js"))
    head.append(soup.new_tag("script", src="/assets/tableSort.js"))

    # Add the navigation bar
    body = soup.new_tag("body")
    html.append(body)
    body.append(BeautifulSoup(navbar_html, 'html.parser'))

    # Add the player name as an H1 heading
    h1 = soup.new_tag("h1")
    h1.string = f"{player_name} Stats"
    body.append(h1)

    # Create the gamelog table
    table = soup.new_tag("table", id=f"{player_id}_gamelog_2023")
    caption = soup.new_tag("caption")
    caption.string = f"{player_name} Gamelogs 2023-24"
    table.append(caption)

    # Create the table header row
    headers = ["Season", "Date", "Team", "Location", "Opp", "Result", "G", "A", "PTS", "+/-", "PIM", "EVG", "PPG", "SHG", "GWG", "EV Assist", "PP Assist", "SH Assist", "SOG", "S%", "SHFT", "TOI", "HIT", "BLK"]
    header_row = soup.new_tag("tr")
    for header in headers:
        th = soup.new_tag("th")
        th.string = header
        header_row.append(th)
    table.append(header_row)

    # Populate the table rows with data
    for _, row in gamelog_data.iterrows():
        tr = soup.new_tag("tr")
        for header in headers:
            td = soup.new_tag("td")

            # Handle hyperlinking for specific columns
            if header == "Season":
                a = soup.new_tag("a", href="/schedule/2023.html")
                a.string = row["Season"]
                td.append(a)
            elif header == "Date":
                a = soup.new_tag("a", href=f"/boxscores/{row['Game_ID']}.html")
                a.string = row["Date"]
                td.append(a)
            elif header == "Team":
                a = soup.new_tag("a", href=f"/teams/{row['Team']}.html")
                a.string = row["Team"]
                td.append(a)
            elif header == "Opp":
                a = soup.new_tag("a", href=f"/teams/{row['Opp']}.html")
                a.string = row["Opp"]
                td.append(a)
            else:
                # Add the value directly, replacing NaN with empty string
                td.string = str(row[header]) if row[header] != "NaN" else ""

            tr.append(td)

        table.append(tr)

    # Add the table to the body
    body.append(table)

    # Write the HTML to a file in the player's folder
    file_path = os.path.join(players_folder, f"{player_id}.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))

# Process the CSV data and generate HTML files for each player
for player_id, player_data in gamelogs_df.groupby("Player_ID"):
    # Get the player name from the first row of the player's data
    player_name = player_data.iloc[0]["Player"]

    # Generate the HTML page for the player
    generate_player_html(player_id, player_name, player_data)

print("Player HTML files have been generated.")
