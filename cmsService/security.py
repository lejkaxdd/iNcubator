
from datetime import datetime, timedelta

def get_cookie_expiration(cookies):
    print(cookies)
    expires = None
    for cookie in cookies:
        if cookie.name == 'token':
            expires = cookie.expires
            return expires
    
    return None
