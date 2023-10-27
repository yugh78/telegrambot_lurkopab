import requests
import json
import vk_api


def get_data2(app_id: str):
    session = vk_api.VkApi(token=app_id)
    vk = session.get_api()
    posts = vk.wall.get(v=5.154, domain='lurkopub_alive', count=10, filter='all')
    return posts['items']


def get_data(app_id: str):
    url = 'https://api.vk.com/method/wall.get'
    r = requests.post(url,
                      params={'v': 5.154, 'domain': 'lurkopub_alive', 'count': 10, 'filter': 'all'},
                      headers={'Authorization': f"Bearer {app_id}"})
    res = json.loads(r.text)

    # fl = filter(lambda item: item['inner_type'] == 'wall_wallpost', res['response']['items'])
    return res['response']['items']


def sort_collection(coll):
    result = []
    for x in coll:
        if is_right_item(x):
            result.append(x)
    return result


def is_right_item(item):
    return item['inner_type'] == 'wall_wallpost' and '#паста' in item['description']
