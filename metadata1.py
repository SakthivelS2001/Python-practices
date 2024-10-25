import os
import shutil
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TPE1, TALB, TIT2, TDRC

def list_mp3_files(directory):
    """
    List all MP3 files in the specified directory.
    
    Parameters:
    directory (str): The path to the directory.
    
    Returns:
    list: List of MP3 file names.
    """
    mp3_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    return mp3_files

def get_mp3_metadata(file_path):
    """
    Extract metadata from an MP3 file.
    
    Parameters:
    file_path (str): The path to the MP3 file.
    
    Returns:
    dict: A dictionary containing metadata such as artist, album, title, and duration.
    """
    audio = MP3(file_path, ID3=ID3)
    
    metadata = {
        "Artist": audio.get('TPE1'),
        "Album": audio.get('TALB'),
        "Title": audio.get('TIT2'),
        "Year": audio.get('TDRC'),
        "Duration": audio.info.length
    }
    return metadata

def move_files(files, source, destination, user_date):
    """
    Move files from source to destination directory and create a subdirectory with user-specified date.
    
    Parameters:
    files (list): List of file names.
    source (str): The source directory path.
    destination (str): The destination directory path.
    user_date (str): A string representing the user-specified date for the subdirectory.
    """
    # Create a new folder with the specified date within the destination directory
    dated_folder = os.path.join(destination, user_date)
    if not os.path.exists(dated_folder):
        os.makedirs(dated_folder)
    
    for file in files:
        shutil.move(os.path.join(source, file), os.path.join(dated_folder, file))
        print(f"Moved {file} to {dated_folder}")

def main():
    """
    Main function to execute the program logic.
    """
    # Specify the source directory
    source_directory = input("Enter the path of the source folder: ").strip()

    # Ensure the directory exists
    if not os.path.isdir(source_directory):
        print(f"The directory {source_directory} does not exist.")
        return

    # List all MP3 files in the directory
    mp3_files = list_mp3_files(source_directory)
    
    if not mp3_files:
        print("No MP3 files found in the specified folder.")
        return

    print("\nMP3 Files Found:")
    for file in mp3_files:
        print(file)

    # Extract metadata for each MP3 file
    print("\nMetadata for MP3 Files:")
    for mp3_file in mp3_files:
        file_path = os.path.join(source_directory, mp3_file)
        metadata = get_mp3_metadata(file_path)
        print(f"\nFile: {mp3_file}")
        print(f" - Artist: {metadata['Artist']}")
        print(f" - Album: {metadata['Album']}")
        print(f" - Title: {metadata['Title']}")
        print(f" - Year: {metadata['Year']}")
        print(f" - Duration: {metadata['Duration']} seconds")

    # Get user input for the destination folder
    destination_directory = input("\nEnter the path of the destination folder: ").strip()

    # Ensure the destination directory exists or create it
    if not os.path.isdir(destination_directory):
        print(f"The destination directory {destination_directory} does not exist. Creating it now.")
        os.makedirs(destination_directory)

    # Get user input for the date to use for the subdirectory
    user_date = input("Enter a date for the subdirectory (e.g., 2024-08-06): ").strip()

    # Move MP3 files to the destination directory within a date folder
    move_files(mp3_files, source_directory, destination_directory, user_date)

if __name__ == "__main__":
    main()
