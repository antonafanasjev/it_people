import json

from redis import Redis


__storage = Redis() 

def ad_views_key(ad_id):
    return 'views_{}'.format(ad_id) 

def get_ad_views(ad_id):
    views_info = __storage.get(ad_views_key(ad_id))

    if views_info is None:
        return {}
    
    return json.loads(views_info.decode())

def increase_ad_views(ad_id, user_id):
    user_id = str(user_id)

    views_info = get_ad_views(ad_id)

    views_info[user_id] = int(views_info.get(user_id, 0)) + 1

    __storage.set(ad_views_key(ad_id), json.dumps(views_info))
