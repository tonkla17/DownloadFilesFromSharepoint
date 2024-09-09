
import os
from datetime import datetime, timedelta
import config
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential


def authenticate():
    try:
        user_credentials = UserCredential(config.username, config.password)
        ctx = ClientContext(config.site_url).with_credentials(user_credentials)
        return ctx
    except Exception as e:
        print(f"Authentication failed: {e}")
        return None

# Example usage
ctx = authenticate()
if ctx:
    print("Authentication successful")
    try:
        # Perform a test operation: Get the title of the SharePoint site
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()
        print(f"Site Title: {web.properties['Title']}")
    except Exception as e:
        print(f"Failed to retrieve site title: {e}")
else:
    print("Authentication failed")

def download_modified_files():
    ctx = authenticate()
    if ctx is None:
        print("Error downloading, can't authenticate")
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
        
# Example usage
download_modified_files()
