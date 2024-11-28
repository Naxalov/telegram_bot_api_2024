import requests
import os 

TOKEN = os.getenv('TOKEN')
base_url = f'https://api.telegram.org/bot{TOKEN}'
r = requests.get(f'{base_url}/getMe')
print(r.json())