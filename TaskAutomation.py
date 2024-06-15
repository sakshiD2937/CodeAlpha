import os
import shutil
import time
from datetime import datetime, timedelta

# Function to organize files by extension
def organize_files(directory):
    file_type_mapping = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.tar.gz']
    }

    # Create folders if they don't exist
    for folder in file_type_mapping:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to appropriate folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_type_mapping.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            # Optionally, handle files with extensions not in the mapping
            if not moved:
                other_folder = os.path.join(directory, 'Others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))

# Function to delete old files
def delete_old_files(directory, days_old):
    cutoff_time = time.time() - (days_old * 86400)  # Convert days to seconds
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.getatime(file_path) < cutoff_time:
                print(f"Deleting old file: {file_path}")
                os.remove(file_path)

# Main function to get user input and perform tasks
def main():
    directory = input("Enter the path to the directory you want to organize and maintain: ")
    days_old = int(input("Enter the number of days after which files should be deleted: "))

    if os.path.isdir(directory):
        organize_files(directory)
        delete_old_files(directory, days_old)
        print(f"Organized files and deleted files not accessed in the last {days_old} days.")
    else:
        print("Invalid directory path. Please try again.")

if __name__ == "__main__":
    main()
