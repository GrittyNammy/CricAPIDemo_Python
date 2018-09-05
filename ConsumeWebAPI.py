import json
import requests
import random

api_token = '-- API Key goes here --'
api_url_base  = 'http://cricapi.com/api/'

def get_new_matches_info():
        api_url =  '{0}matches'.format(api_url_base)  + '/?rnd=' + str(random.randint(0,64255))
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

def get_old_matches_info():
        api_url =  '{0}cricket'.format(api_url_base)  + '/?rnd=' + str(random.randint(0,64255))
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

def get_matchScore(unique_id):
        api_url =  '{0}cricketScore'.format(api_url_base)+'/?rnd=' + str(random.randint(0,64255))   + '/?unique_id=' + unique_id
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

def get_matchCalendar():
        api_url =  '{0}matchCalendar'.format(api_url_base)  + '/?rnd=' + str(random.randint(0,64255))
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

def get_playerStats(unique_id):
        api_url =  '{0}playerStats'.format(api_url_base) + '/?rnd=' + str(random.randint(0,64255)) + '&pid=' + unique_id
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

def get_fantasySummary(unique_id):
        api_url =  '{0}fantasySummary'.format(api_url_base) + '/?rnd=' + str(random.randint(0,64255)) + '&unique_id=' + unique_id
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

def get_fantasySquad(unique_id):
        api_url =  '{0}fantasySquad'.format(api_url_base) + '/?rnd=' + str(random.randint(0,64255)) + '&unique_id=' + unique_id
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

def Search_PlayerbyName(name):
        api_url =  '{0}playerFinder'.format(api_url_base) + '/?rnd=' + str(random.randint(0,64255)) + '&name=' + name
        headers = {'Content-Type': 'application/json',
           'apikey': '{0}'.format(api_token)}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

# matches_info = get_old_matches_info()
# matches_info = get_matchScore('1119552')
# matches_info = get_matchCalendar()
# player_info = get_playerStats('253802')
matches_info = Search_PlayerbyName('kohli')
# player_info = Search_PlayerbyName('virat')

if matches_info is not None:
    print("Here's your info: ")
    # for k, v in matches_info['data'][0].items():
    #     print('{0}:{1}'.format(k, v))
    print(matches_info)

else:
    print('[!] Request Failed')