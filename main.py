import requests
import os 

TOKEN = os.getenv('TOKEN')
base_url = f'https://api.telegram.org/bot{TOKEN}'

chat_id = 86775091
text = 'hello'

r = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={text}')

print(r.json())