import requests
import os, sys, json
from zipfile import ZipFile

vc4_server = os.getenv('VC4_SERVER_URL')
vc4_api_key = os.getenv('VC4_API_KEY')

program_id = sys.argv[1]
file_path = sys.argv[2]
with ZipFile('index.zip','w') as zip:
    zip.write(file_path)

headers = {
    'accept': 'application/json',
    'Authorization': vc4_api_key
}

form_data = {
    'ProgramId': program_id,
    'StartNow': 'true'
}

program_file = {
    'CwsFile': open('index.zip', 'rb')
}

deploy = requests.put(f'{vc4_server}/VirtualControl/config/api/ProgramLibrary', headers=headers, files=program_file, data=form_data)
status_info = (deploy.json()['Actions'][0]['Results'][0]['StatusInfo']
if status_info == 'SUCCESS':
    print('Deployment succeeded')
    sys.exit(0)
else:
    print('Deployment failed, Reason: ' + status_info)
    sys.exit(1)