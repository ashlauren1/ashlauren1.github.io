import os
import pandas as pd
from bs4 import BeautifulSoup

# Load the GoalFinder CSV file
goalfinder_csv = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\goalfinder.csv'
goalfinder_df = pd.read_csv(goalfinder_csv)

# Set the players directory where the HTML files are stored
players_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\players'

# Make sure the players directory exists
if not os.path.exists(players_dir):
    os.makedirs(players_dir)

# Function to generate rows for the scoring table
def generate_scoring_table_rows(player_id, player_data):
    rows = ""
    for _, row in player_data.iterrows():
        date_link = f'<td><a href="/boxscores/{row["Game_ID"]}.html">{row["Date"]}</a></td>'
        team_link = f'<td><a href="/teams/{row["Team"]}.html">{row["Team"]}</a></td>'
        opp_link = f'<td><a href="/teams/{row["Opp"]}.html">{row["Opp"]}</a></td>'
        scorer_link = f'<td><a href="/players/{row["Scorer_ID"]}.html">{row["Scorer"]}</a></td>'
        assist1_link = f'<td><a href="/players/{row["Assist1_ID"]}.html">{row["Assist1"]}</a></td>'
        assist2_link = f'<td><a href="/players/{row["Assist2_ID"]}.html">{row["Assist2"]}</a></td>'
        goalie_link = f'<td><a href="/players/{row["Goalie_ID"]}.html">{row["Goalie"]}</a></td>'
        
        rows += f"""
        <tr>
            {date_link}
            {team_link}
            <td>{row["Location"]}</td>
            {opp_link}
            <td>{row["Result"]}</td>
            {scorer_link}
            {assist1_link}
            {assist2_link}
            {goalie_link}
            <td>{row["Per."]}</td>
            <td>{row["Time"]}</td>
        </tr>
        """
    return rows

# Function to append a scoring table to the player's existing HTML file
def append_scoring_table(player_id, player_name, player_data):
    # Path to the player's HTML file
    html_file_path = os.path.join(players_dir, f"{player_id}.html")

    print(f"Attempting to process file: {html_file_path}")
    
    # If the file exists, append the new table
    if os.path.exists(html_file_path):
        print(f"File found: {html_file_path}")
        # Read the existing HTML file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Check if the HTML was parsed correctly
        if soup:
            print(f"HTML parsed successfully for {html_file_path}")
        else:
            print(f"Failed to parse HTML for {html_file_path}")

        # Generate the rows for the scoring table
        rows = generate_scoring_table_rows(player_id, player_data)

        # Create the new scoring table with a unique ID
        new_table_html = f"""
        <h2>Scoring Log</h2>
        <table id="{player_id}_scoring" border="1">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Team</th>
                    <th>Location</th>
                    <th>Opp</th>
                    <th>Result</th>
                    <th>Scorer</th>
                    <th>Assist1</th>
                    <th>Assist2</th>
                    <th>Goalie</th>
                    <th>Per.</th>
                    <th>Time</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
        """

        # Append the new table to the existing content section
        content_section = soup.find('main', {'id': 'content'})
        if content_section:
            print(f"Content section found in {html_file_path}, appending table...")
            new_table = BeautifulSoup(new_table_html, 'html.parser')
            content_section.append(new_table)

        else:
            print(f"<main> section not found, creating <main> section in {html_file_path}")
            # Create a new <main> section
            new_main = soup.new_tag('main', id='content')
            new_main.append(BeautifulSoup(new_table_html, 'html.parser'))

            # Append the <main> section before the closing </body> tag
            body_section = soup.find('body')
            if body_section:
                body_section.append(new_main)

        # Write the updated HTML back to the file
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup.prettify()))

        print(f"Appended scoring table to {html_file_path}")
    else:
        print(f"File {html_file_path} not found.")

# Loop through each player in the GoalFinder.csv data
for player_id in goalfinder_df['Scorer_ID'].unique():
    # Get the player's relevant data from Scorer_ID, Assist1_ID, Assist2_ID, and Goalie_ID
    player_data = goalfinder_df[(goalfinder_df['Scorer_ID'] == player_id) |
                                (goalfinder_df['Assist1_ID'] == player_id) |
                                (goalfinder_df['Assist2_ID'] == player_id) |
                                (goalfinder_df['Goalie_ID'] == player_id)]

    # Extract the player's name from the data
    player_name = player_data['Scorer'].iloc[0]  # Assuming the name can be taken from 'Scorer' column

    # Print which player is being processed
    print(f"Processing player: {player_id} - {player_name}")

    # Append the scoring table to the player's existing HTML file
    append_scoring_table(player_id, player_name, player_data)
