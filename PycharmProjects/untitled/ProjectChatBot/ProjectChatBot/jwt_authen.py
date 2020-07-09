# File: ProjectChatBot.jwt_authen
# Description:
# Author             Date                       Change Description
# Bcdai            9/7/2020                     Create new function

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
            time_old_fr = datetime.strptime(time_old_str, "%d-%m-%Y %H:%M:%S")
            time_now_fr = datetime.strptime(time_now_str, "%d-%m-%Y %H:%M:%S")

            duration_time = time_now_fr - time_old_fr

            duration_minutes = duration_time.seconds / 60

            if duration_minutes > 1:
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


def vertify_token(token):
    flag_check_done = False
    try:
        decode = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

        userid = decode['userid']
        username = decode['username']
        password = decode['password']
        ip_request = decode['ip']
        browser_request = decode['browser']

        for obj_old in jwt_toket_memory_authen:
            if obj_old['username'] == username and obj_old['password'] == password and obj_old['ip'] == ip_request and \
                    obj_old['browser'] == browser_request:
                time_old_str = obj_old['time']
                time_now_str = datetime.now().strptime('%d-%m-%y %H-%M-%S')
                old_time_fr = datetime.strptime(time_old_str, '%d-%m-%y %H-%M-%S')
                now_time_fr = datetime.strptime(time_now_str, '%d-%m-%y %H-%M-%S')

                duration_time = now_time_fr - old_time_fr

                duration_minutes = duration_time.seconds / 60
                if duration_minutes > 30:
                    jwt_toket_memory_authen.remove(obj_old)
                    flag_check_done = False

                else:
                    obj_old['time'] = datetime.now().strptime("%d-%m-%Y %H:%M:%S")
                    global_config.GLB_USER_ID = userid
                    global_config.GLB_USER_NAME = username

                    flag_check_done = True
                    break

    except Exception as e:
        print("jwt_authen-> vertify_token-> ex", e)

    return flag_check_done


def remove_token(token):
    flag_check_delete_done = False
    try:
        for obj_old in jwt_toket_memory_authen:
            if obj_old['token'] == token:
                jwt_toket_memory_authen.remove(obj_old)
                flag_check_delete_done = True
                break

    except Exception as e:
        print("jwt_authen -> remove_token -> ex", e)

    return flag_check_delete_done
