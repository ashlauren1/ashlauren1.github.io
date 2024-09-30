import os

# Base directory
players_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\players'

# Loop through each player's folder in the players directory
for player_folder in os.listdir(players_dir):
    player_folder_path = os.path.join(players_dir, player_folder)

    # Check if it is a directory (i.e., a player's folder)
    if os.path.isdir(player_folder_path):
        index_file_path = os.path.join(player_folder_path, 'index.html')
        penalties_file_path = os.path.join(player_folder_path, f'{player_folder}_penalties.html')
        scoring_file_path = os.path.join(player_folder_path, f'{player_folder}_scoring.html')
        
        # Read the content of the index.html file
        if os.path.exists(index_file_path):
            with open(index_file_path, 'r', encoding='utf-8') as index_file:
                index_content = index_file.read()
        else:
            index_content = "<p>No index content available</p>"

        # Append the penalties table if it exists
        if os.path.exists(penalties_file_path):
            with open(penalties_file_path, 'r', encoding='utf-8') as penalties_file:
                penalties_content = penalties_file.read()
        else:
            penalties_content = "<p>No penalties table available</p>"

        # Append the scoring table if it exists
        if os.path.exists(scoring_file_path):
            with open(scoring_file_path, 'r', encoding='utf-8') as scoring_file:
                scoring_content = scoring_file.read()
        else:
            scoring_content = "<p>No scoring table available</p>"

        # Merge the contents into a new file
        merged_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{player_folder} Profile</title>
        </head>
        <body>
            {index_content}
            <h2>Penalties</h2>
            {penalties_content}
            <h2>Scoring</h2>
            {scoring_content}
        </body>
        </html>
        """

        # Write the merged content to a new file with the player's name
        new_file_path = os.path.join(players_dir, f'{player_folder}.html')
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(merged_content)

        print(f"Created {new_file_path}")
