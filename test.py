import requests
import datetime

token = 'YPsw8x8JH5Dg1VerQGs2wBHf'

def create_twitter_post():

    ...

def get_bip_post():

    headers = {
        'Authorization': 'Bearer ' + token,
    }

    url = 'https://app.circle.so/api/v1/posts?community_id=45511&space_id=535766'

    result = requests.get(url, headers=headers)


    for i in result.json():
        if datetime.datetime.strptime(i['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ').date() == datetime.date.today():
            ...
        
get_bip_post()