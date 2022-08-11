import vk_api
from credentials import vk_token
import re
import pytz
from datetime import timedelta


def fix_timezone(date):
    if date.tzinfo:
        return date
    date += timedelta(hours=3)
    return date.astimezone(pytz.timezone('Europe/Moscow'))


def fix_timezones(items):
    for i, m in enumerate(items):
        items[i]['article_time'] = fix_timezone(m['article_time'])
    return items

class vkapi:
    def __init__(self):
        self._session = vk_api.VkApi(token=vk_token)
        self._vk = self._session.get_api()

    def get_video(self, oid, vid):
        respond = self._session.method("video.get", {"videos": f"{oid}_{vid}"})
        # print()
        return respond['items'][0]['photo_1280']

    def get_cover(self, oid, vid):
        respond = self._session.method("video.get", {"videos": f"{oid}_{vid}"})
        return respond['items'][0]['photo_800']


def get_embed_html_object(source):
    # тут должно возвращаться видео, но видео не вставляется
    oid = re.search(r'oid=(.+?)&', source, flags=re.DOTALL)[1]
    vid = re.search(r'&id=(.+?)&', source, flags=re.DOTALL)[1]
    my_vk_api = vkapi()
    video = my_vk_api.get_video(oid, vid)
    embed = f'<a href="https://vk.com/video{oid}_{vid}"><img src="{video}"></a>'
    return embed


def get_ebbed_object_cover(source):
    oid = re.search(r'oid=(.+?)&', source, flags=re.DOTALL)[1]
    vid = re.search(r'&id=(.+?)&', source, flags=re.DOTALL)[1]
    my_vk_api = vkapi()
    cover_img = my_vk_api.get_cover(oid, vid)
    return cover_img
