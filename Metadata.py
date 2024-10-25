import os
import shutil
from datetime import datetime

def get_mp3_date(file_path):
    try:
        audio = MP3(file_path)
        if audio.tags is not None:
            return datetime.fromtimestamp(audio.info.pprint())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def move_files_by_date(source_folder, destination_folder, user_date):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                file_date = get_mp3_date(file_path)
                
                if file_date and file_date.date() == user_date:
                    shutil.move(file_path, os.path.join(destination_folder, file))
                    print(f"Moved: {file}")

if __name__ == "__main__":
    source_folder = "/home/sakthivel/Documents/Practice/task"
    destination_folder = "/home/sakthivel/Documents/Practice/mp3"
    user_date = datetime.strptime("2024-08-06", "%Y-%m-%d").date()


    move_files_by_date(source_folder, destination_folder, user_date)

