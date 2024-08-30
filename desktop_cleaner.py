import os
import shutil

def organize_desktop():
    # Path to the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # Categories and their corresponding file extensions
    categories = {
        'Pictures': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.svg'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
    }
    
    # Create folders if they don't exist
    for category in categories:
        folder_path = os.path.join(desktop_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
    
    # Move files into their respective folders
    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1]
            for category, extensions in categories.items():
                if file_ext.lower() in extensions:
                    shutil.move(file_path, os.path.join(desktop_path, category, file))
                    print(f"Moved {file} to {category}")
                    break

# Call the function to organize the desktop
organize_desktop()
