import requests
import json

BASE_URL = 'https://api.meraki.com/api/v1'
headers = { 'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0' }
RESOURCE = '/organizations'

call_response = requests.get(BASE_URL + RESOURCE, headers=headers)
if call_response.status_code != 200:
    print(f'Failed to get organizations')
    exit(1)
parsed_response = json.loads(call_response.text)

for organization in parsed_response:
    print('ID: {id}, Name: {name}'.format(id=organization['id'], name=organization['name']))
