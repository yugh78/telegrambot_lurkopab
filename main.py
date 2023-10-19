import requests
import json
import aiosqlite
# Замените 'APP_ID' на ваш собственный APP_ID
APP_ID = ' '
url = 'https://api.vk.com/method/wall.get'
r = requests.post(url,
                  params={'v':5.154,'domain':'lurkopub_alive','count':10,'filter':'all'},
                  headers= {'Authorization':f"Bearer {APP_ID}"})
res = json.loads(r.text)
print(res)
#fl = filter(lambda item: item['inner_type'] == 'wall_wallpost', res['response']['items'])
#print(*fl)











