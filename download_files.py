# download_files.py

import os
from datetime import datetime, timedelta
from sharepoint_auth import authenticate
import config

def download_modified_files():
    ctx = authenticate()
    if ctx is None:
        print("Failure attempt to download : not able to authenticate")
        return

    folder = ctx.web.get_folder_by_server_relative_url(config.sharepoint_folder_url)
    files = folder.files
    ctx.load(files)
    ctx.execute_query()

    for file in files:
        file_name = file.properties["Name"]
        file_time = file.properties["TimeLastModified"]
        file_time = datetime.strptime(file_time, '%Y-%m-%dT%H:%M:%SZ')

        # Generate a new file name with the current date and time
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        new_file_name = f"{os.path.splitext(file_name)[0]}_{current_time}{os.path.splitext(file_name)[1]}"
        local_path = os.path.join(config.local_folder_path, new_file_name)

        with open(local_path, "wb") as local_file:
            file.download(local_file)
            ctx.execute_query()
        print(f"Downloaded: {new_file_name}")