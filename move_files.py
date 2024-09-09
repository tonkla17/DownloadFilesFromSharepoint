# move_files.py

import os
import shutil
import config

def move_files():
    for file_name in os.listdir(config.local_folder_path):
        if file_name.endswith('.xlsx'):
            source_path = os.path.join(config.local_folder_path, file_name)
            destination_path = os.path.join(config.destination_folder_path, file_name)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name} to {config.destination_folder_path}")

