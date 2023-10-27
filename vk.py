import requests
import json
import vk_api


class VkClient:
    def __init__(self, app_id):
        self.app_id = app_id

    def get_data(self, offset: int):
        session = vk_api.VkApi(token=self.app_id)
        vk = session.get_api()
        posts = vk.wall.get(offset=offset, v=5.154, domain='lurkopub_alive', count=100, filter='all')
        # log('get response ...', posts['items'])
        return posts['items']

    def get_post_count(self):
        session = vk_api.VkApi(token=self.app_id)
        vk = session.get_api()
        posts = vk.wall.get(v=5.154, domain='lurkopub_alive', count=0, filter='all')
        return posts['count']


# def get_data(app_id: str):
#     url = 'https://api.vk.com/method/wall.get'
#     r = requests.post(url,
#                       params={'v': 5.154, 'domain': 'lurkopub_alive', 'count': 10, 'filter': 'all'},
#                       headers={'Authorization': f"Bearer {app_id}"})
#     res = json.loads(r.text)
#
#     # fl = filter(lambda item: item['inner_type'] == 'wall_wallpost', res['response']['items'])
#     return res['response']['items']


def sort_collection(coll):
    result = []
    for x in coll:
        if is_right_item(x):
            result.append(x)
            log('item is right:', x)

    return result


def is_right_item(item):
    return item['inner_type'] == 'wall_wallpost' \
        and '#паста' in item['text']


enable_log = False



def log(msg, *args):
    global enable_log
    if enable_log:
        if msg:
            print(f"\033[32m{msg}\033[0;0m")
        print(json.dumps(args, indent=2))
