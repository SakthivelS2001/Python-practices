import os
import shutil

def move_mp3_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # List all files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file is an MP3
        if filename.endswith('.mp3'):
            # Construct full file path
            file_path = os.path.join(source_folder, filename)
            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved: {filename}")

# Example usage
source_folder = '/home/sakthivel/Documents/Practice/task'
destination_folder = '/home/sakthivel/Documents/Practice/mp3'
move_mp3_files(source_folder, destination_folder)

