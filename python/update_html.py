import os
import re

# Define the new head and nav content
new_head_and_nav = """<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stats</title>
    <link rel="stylesheet" href="/assets/styles.css">
    <script src="/assets/searchBar.js"></script>
    <script src="/assets/tableSort.js"></script>
</head>
<body>

<!-- Navigation Bar -->
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
	<!-- Search Bar -->
	<li>
	  <input type="text" id="searchBar" placeholder="Search for players or teams..." oninput="performSearch()" autocomplete="off">
	  <div id="searchResults" class="dropdown"></div>
	  <button id="searchButton" onclick="handleSearch()">Search</button>
	</li>  
  </ul>
</nav>

    <!-- Main Content Layout -->
    <main id="content">

        <!-- Players Section -->
        <section class="left-section">
            
			<h2>Players</h2>
            <ul>
			    <li><a href="/players/">Player Index</a></li>
				<li><a href="/leaders/skaters.html">Skaters - Leaders and Stats</a></li>
                <li><a href="/leaders/goalies.html">Goalies - Leaders and Stats</a></li>
				<li><a href="/versus/">Head to Head Stats</a></li>
				<li><a href="/probabilities/">Player Probabilities</a></li>
            </ul>
        </section>

        <!-- Team Section -->
        <section class="right-section">
            <h2>Teams</h2>
            <ul>
                <li><a href="/teams/">Team Index</a></li>
				<li><a href="/seasons/2025/standings.html">Current Standings</a></li>
                <li><a href="/seasons/2025/rosters.html">Team Rosters</a></li>
				<li><a href="/leaders/teams.html">Team Stats</a></li>
				<li><a href="/versus/">Head to Head Stats</a></li>
            </ul>
        </section>
		
		<!-- Games Section -->
        <section class="left-section">
            <h2>Games</h2>
            <ul>
				<li><a href="/boxscores/">Game Results</a></li>
                <li><a href="/seasons/2025/schedule.html">Schedule</a></li>
				<li><a href="/versus/">Head to Head Results</a></li>
            </ul>
        </section>

        <!-- Season Section -->
        <section class="right-section">
            <h2><a href="/seasons/">Season Index</a></h2>
            <h3>2024-25</h3>
			<ul>
                <li><a href="/seasons/2025/">2024-25 Schedule</a></li>
				<li><a href="/seasons/2025/">2024-25 Standings</a></li>
				<li><a href="/seasons/2025/">2024-25 Rosters</a></li>
			</ul>
			<h3>2023-24</h3>
			<ul>
                <li><a href="/seasons/2024/">2023-24 Schedule</a></li>
				<li><a href="/seasons/2024/">2023-24 Standings</a></li>
				<li><a href="/seasons/2024/">2023-24 Rosters</a></li>
			</ul>
			<h3>2022-23</h3>
			<ul>
				<li><a href="/seasons/2023/">2022-23 Schedule</a></li>
				<li><a href="/seasons/2023/">2022-23 Standings</a></li>
				<li><a href="/seasons/2023/">2022-23 Rosters</a></li>
			</ul>
			<h3>2021-22</h3>
			<ul>
				<li><a href="/seasons/2022/">2021-22 Schedule</a></li>
				<li><a href="/seasons/2022/">2021-22 Standings</a></li>
				<li><a href="/seasons/2022/">2021-22 Rosters</a></li>
            </ul>
        </section>
        <!-- Divider -->
        <hr>

        <!-- Schedule Section with Calendar Placeholder -->
        <section id="schedule">
            <h2>Schedule</h2>
            <div id="calendar-placeholder">[Calendar graphic placeholder]</div>
        </section>

    </main>"""

# Define paths to the folders
players_folder = r'C:\Users\ashle\Documents\Projects\githubcopy\players'
teams_folder = r'C:\Users\ashle\Documents\Projects\githubcopy\teams'
boxscores_folder = r'C:\Users\ashle\Documents\Projects\githubcopy\boxscores'
seasons_folder = r'C:\Users\ashle\Documents\Projects\githubcopy\seasons'
leaders_folder = r'C:\Users\ashle\Documents\Projects\githubcopy\leaders'
versus_folder = r'C:\Users\ashle\Documents\Projects\githubcopy\versus'
probabilities_folder = r'C:\Users\ashle\Documents\Projects\githubcopy\probabilities'

# Function to replace the head and nav sections
def update_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expressions to find the existing head and nav
    head_regex = r'<!DOCTYPE html>.*?<body>'
    nav_regex = r'<nav.*?</nav>'

    # Check if both the head and nav exist and replace them
    new_content = re.sub(f'{head_regex}.*?{nav_regex}', new_head_and_nav, content, flags=re.DOTALL)

    # Save the updated file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Function to iterate over all HTML files in a directory
def update_files_in_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                update_html_file(file_path)
                print(f'Updated: {file_path}')

# Update all files in the players, teams, and boxscores folders
update_files_in_folder(players_folder)
update_files_in_folder(teams_folder)
update_files_in_folder(boxscores_folder)
update_files_in_folder(seasons_folder)
update_files_in_folder(leaders_folder)
update_files_in_folder(versus_folder)
update_files_in_folder(probabilities_folder)

print("All files have been updated!")
