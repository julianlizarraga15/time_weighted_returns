import requests
from config import URL, ENDPOINT_TOKENS


def get_bearer_token(refresh_token, username, password, refresh=False):
    if not refresh:
        payload = {
            'username':username,
            'password':password,
            'grant_type':'password'
        }
    else:
        payload = {
            'refresh_token':refresh_token,
            'grant_type':'refresh_token'
        }
    r = requests.post(URL+ENDPOINT_TOKENS, data=payload)
    if r.status_code == 200:
        r = r.json()
        tokens = {
            'access_token':r['access_token'],
            'refresh_token':r['refresh_token']
        }
        return tokens
    else:
        print('Failed. Status code:', r.status_code)