import requests
import redis
import json

TIME_OUT = 1 * 60 * 60

r = redis.Redis(host='127.0.0.1', port=6379)


def get(url):
    cache = r.get(url)

    if cache:
        return json.loads(cache.decode(encoding="utf-8"))
    else:
        rs = requests.get(url)
        if rs.status_code == 200:
            r.set(url, rs.text, TIME_OUT)
            return rs.json()
        else:
            return None


# 获取设备列表
def get_devices():
    return get('https://api.ipsw.me/v4/devices')


# 获取发布历史
def get_releases():
    return get('https://api.ipsw.me/v4/releases')


def get_firmware(firmware):
    return get('https://api.ipsw.me/v4/device/{}?type=ipsw'.format(firmware))


# print(get_devices())

def get_itunes(platform):
    return get('https://api.ipsw.me/v4/itunes/{}'.format(platform))


def get_model(model):
    return get('https://api.ipsw.me/v4/model/{}'.format(model))
