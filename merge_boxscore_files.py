import os

# Base directory for boxscores
boxscores_dir = r'C:\Users\ashle\Documents\Projects\ashlauren1.github.io\boxscores'

# Loop through each game's folder in the boxscores directory
for game_folder in os.listdir(boxscores_dir):
    game_folder_path = os.path.join(boxscores_dir, game_folder)

    # Check if it is a directory (i.e., a game's folder)
    if os.path.isdir(game_folder_path):
        index_file_path = os.path.join(game_folder_path, 'index.html')
        additional_table_path1 = os.path.join(game_folder_path, f'{game_folder}_table1.html')
        additional_table_path2 = os.path.join(game_folder_path, f'{game_folder}_table2.html')
        
        # Read the content of the index.html file
        if os.path.exists(index_file_path):
            with open(index_file_path, 'r', encoding='utf-8') as index_file:
                index_content = index_file.read()
        else:
            index_content = "<p>No index content available</p>"

        # Append additional table 1 if it exists
        if os.path.exists(additional_table_path1):
            with open(additional_table_path1, 'r', encoding='utf-8') as table_file1:
                table_content1 = table_file1.read()
        else:
            table_content1 = "<p>No additional table 1 available</p>"

        # Append additional table 2 if it exists
        if os.path.exists(additional_table_path2):
            with open(additional_table_path2, 'r', encoding='utf-8') as table_file2:
                table_content2 = table_file2.read()
        else:
            table_content2 = "<p>No additional table 2 available</p>"

        # Merge the contents into a new file
        merged_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Boxscore {game_folder}</title>
        </head>
        <body>
            {index_content}
            <h2>Additional Table 1</h2>
            {table_content1}
            <h2>Additional Table 2</h2>
            {table_content2}
        </body>
        </html>
        """

        # Write the merged content to a new file with the game's name
        new_file_path = os.path.join(boxscores_dir, f'{game_folder}.html')
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(merged_content)

        print(f"Created {new_file_path}")
