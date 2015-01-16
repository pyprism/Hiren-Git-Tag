__author__ = 'prism'

# import github
#
# gh = github.GitHub(client_id='',
#                    client_secret='')
#
# print(gh.authorize_url(state='a-random-string'))
#
# state = gh.get_access_token(b'', b'a-random-string')
# print("access: ", state)
# gh = github.GitHub(access_token=state)
#
# print(gh.users('pyprism').starred())

import requests

bomb = {'client_id': '',
        'client_secret': '',
        'note': 'example'}

r = requests.post('https://api.github.com/authorizations', bomb)

print(r)
#print(r)