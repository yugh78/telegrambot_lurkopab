import requests
import json
import vk_api

WALL_DOMAIN = 'lurkopub_alive'

class VkClient:
    def __init__(self, app_id, logger = None):
        self.app_id = app_id
        self.logger = logger

    def get_data(self, offset: int):
        session = vk_api.VkApi(token=self.app_id)
        vk = session.get_api()
        posts = vk.wall.get(offset=offset, v=5.154, domain=WALL_DOMAIN, count=100, filter='all')
        if self.logger is not None: self.logger.log_debug("get response from VK", posts)
        return posts['items']

    def get_post_count(self):
        session = vk_api.VkApi(token=self.app_id)
        vk = session.get_api()
        posts = vk.wall.get(v=5.154, domain=WALL_DOMAIN, count=0, filter='all')
        return posts['count']

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
