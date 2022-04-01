import json
import re
import requests
from instaloader import Instaloader, Profile

PROFILE = ['atitbimali','cristiano','leomessi'] #enter usernames here
n = len(PROFILE)
for i in range(0,n):
    response = requests.get('https://www.instagram.com/' + PROFILE[i])
    json_match = re.search(r'window\._sharedData = (.*);</script>', response.text)
    profile_json = json.loads(json_match.group(1))['entry_data']['ProfilePage'][0]['graphql']['user']

    print(profile_json['edge_followed_by']['count'])

