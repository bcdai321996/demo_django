import jwt

from ProjectChatBot import settings
from datetime import datetime
from utils import global_config

jwt_toket_memory_authen = []


def create_token(userid, username, password, menu_access, ip_request, browser_request):
    time_now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    payload = {
        'userid': userid,
        'username': username,
        'password': password,
        'time': time_now_str,
        'ip': ip_request,
        'browser': browser_request,
        'menu_access': menu_access
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode("utf-8")

    for obj_old in reversed(jwt_toket_memory_authen):
        if obj_old['username'] == username:
            time_old_str = obj_old['time']
            time_old_fr = datetime.strftime(time_old_str, "%d-%m-%Y %H:%M:%S")
            time_now_fr = datetime.strftime(time_now_str, "%d-%m-%Y %H:%M:%S")

            duration_time = time_now_fr - time_old_fr

            duration_minutes = duration_time.seconds / 60

            if duration_minutes > 30:
                jwt_toket_memory_authen.remove(obj_old)

    user_memory_jwt = {
        'userid': userid,
        'username': username,
        'password': password,
        'token': token,
        'time': time_now_str,
        'ip': ip_request,
        'browser': browser_request,
        'menu_access': menu_access
    }

    jwt_toket_memory_authen.append(user_memory_jwt)

    return token
