import requests
import os, sys, json
from zipfile import ZipFile

vc4_server = os.getenv('VC4_SERVER_URL')
vc4_api_key = os.getenv('VC4_API_KEY')

file_path = sys.argv[1]
with ZipFile('index.zip','w') as zip:
    zip.write(file_path)

headers = {
    'accept': 'application/json',
    'Authorization': vc4_api_key
}

form_data = {
    'ProgramId': 3,
    'FriendlyName': 'SSProJenkins',
    'Notes': 'Jenkins Deployed This',
    'StartNow': 'true'
}

program_file = {
    'CwsFile': open('index.zip', 'rb')
}

deploy = requests.put(f'{vc4_server}/VirtualControl/config/api/ProgramLibrary', headers=headers, files=program_file, data=form_data)
print(deploy.content)