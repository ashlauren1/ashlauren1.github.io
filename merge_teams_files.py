import os

# Base directory for teams
teams_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\teams'

# Loop through each team's folder in the teams directory
for team_folder in os.listdir(teams_dir):
    team_folder_path = os.path.join(teams_dir, team_folder)

    # Check if it is a directory (i.e., a team's folder)
    if os.path.isdir(team_folder_path):
        index_file_path = os.path.join(team_folder_path, 'index.html')
        penalties_file_path = os.path.join(team_folder_path, f'{team_folder}_penalties.html')
        scoring_file_path = os.path.join(team_folder_path, f'{team_folder}_scoring.html')
        
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
            <title>{team_folder} Profile</title>
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

        # Write the merged content to a new file with the team's name
        new_file_path = os.path.join(teams_dir, f'{team_folder}.html')
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(merged_content)

        print(f"Created {new_file_path}")
