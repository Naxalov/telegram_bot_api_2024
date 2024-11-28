import requests
import os 

TOKEN = os.getenv('TOKEN')
base_url = f'https://api.telegram.org/bot{TOKEN}'
r = requests.get(f'{base_url}/getUpdates')
result = r.json()['result'][0]
message = result['message']
print(message['text'])