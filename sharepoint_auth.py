from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
import config

def authenticate():
    try:
        # Authen via Graph api
        # client_credentials = ClientCredential(config.client_id, config.client_secret)
        # ctx = ClientContext(config.site_url).with_credentials(client_credentials)
        
        #Authen via username + password
        ctx = ClientContext(config.site_url).with_user_credentials(config.username, config.password)
        return ctx
    except Exception as e:
        print(f"Authentication failed: {e}")
        return None
