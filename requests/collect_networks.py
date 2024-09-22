import requests
import json

BASE_URL = 'https://api.meraki.com/api/v1'
headers = { 'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0' }
RESOURCE = '/organizations'

call_response = requests.get(BASE_URL + RESOURCE, headers=headers)
if call_response.status_code != 200:
    print(f'Failed to get organizations')
    exit(1)
organizations = json.loads(call_response.text)

for organization in organizations:
    RESOURCE = '/organizations/{id}/networks'.format(id=organization['id'])
    call_response = requests.get(BASE_URL + RESOURCE, headers=headers)
    if call_response.status_code != 200:
        print('Failed to get networks for organization {organization}'.format(organization=organization["name"]))
        continue
    networks = json.loads(call_response.text)

    if len(networks) > 0:
        print('Printing networks for organization {name}:'.format(name=organization['name']))

        for network in networks:
            print('\tID: {id}, Name: {name}, TimeZone: {timezone}'.format(id=network['id'],
                                                                  name=network['name'],
                                                                  timezone=network['timeZone']))
    else:
        print('There are no networks assigned to organization {name}'.format(name=organization['name']))
