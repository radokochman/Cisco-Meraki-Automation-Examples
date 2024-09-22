import requests
import json

BASE_URL = 'https://api.meraki.com/api/v1'
headers = {'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'}
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

    for network in networks:
        RESOURCE = '/networks/{id}/devices'.format(id=network['id'])
        call_response = requests.get(BASE_URL + RESOURCE, headers=headers)
        if call_response.status_code != 200:
            print('Failed to get devices for {network}'.format(network=network["name"]))
            continue
        devices = json.loads(call_response.text)

        if len(devices) > 0:
            print('Devices assigned to network {network}'.format(network=network['name']))

            for device in devices:
                if 'name' in device:
                    print('\tName: {name}, Model: {model}, Serial: {serial}'.format(name=device['name'],
                                                                                    model=device['model'],
                                                                                    serial=device['serial']))
                else:
                    print('\tModel: {model}, Serial: {serial}'.format(model=device['model'],
                                                                      serial=device['serial']))
        else:
            print('There are no devices assigned to the network {network}'.format(network=network['name']))
