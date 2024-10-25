import os
import shutil
from datetime import datetime

def list_files_in_folder(folder_path):
    return os.listdir(folder_path)

def get_file_format():
    return input("Enter the file format (e.g., .mp3, .jpg): ")

def get_creation_date(file_path):
    return datetime.fromtimestamp(os.path.getctime(file_path))

def get_user_date():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    return datetime.strptime(date_str, '%Y-%m-%d')

def move_files_based_on_date(folder_path, file_format, user_date, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for file_name in list_files_in_folder(folder_path):
        if file_name.endswith(file_format):
            file_path = os.path.join(folder_path, file_name)
            creation_date = get_creation_date(file_path)
            if creation_date.date() == user_date.date():
                shutil.move(file_path, os.path.join(destination_folder, file_name))
                print(f"Moved: {file_name}")

def main():
    folder_path = ("/home/sakthivel/Documents/Practice/task")
    destination_folder = ("/home/sakthivel/Documents/Practice/mp3")
    
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    file_format = get_file_format()
    user_date = get_user_date()
    
    move_files_based_on_date(folder_path, file_format, user_date, destination_folder)

if __name__ == "__main__":
    main()
