import re

from nintendo import NintendoClient


client = NintendoClient()
login_info = client.get_nso_login_info()
login_url = login_info['login_url']
print(f'Please visit the following URL to log in:\n')
print(login_url)
print('\nright click the "Select this account" button, copy the link address, and paste it below:')

use_account_url = input()
session_token_code = re.search('de=(.*)&st', use_account_url).group(1)

session_token = client.get_session_token(session_token_code, login_info['auth_code_verifier'])

if session_token:
    print('Session token obtained!\n')
    print(f'Your session token is: {session_token}\n')
    print('You can now set it to GitHub Secrets as "NINTENDO_SESSION_TOKEN"')
