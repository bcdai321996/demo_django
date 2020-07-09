# File: requester.views.py
# Description:
# Author             Date                       Change Description
# bcdai            8/7/2020                     Create new function
# bcdai            9/7/2020                     Create new function login, logout
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from . import contains, models
from ProjectChatBot import jwt_authen


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def login_requester(request):
    print(request.META)
    response = contains.get_response_authen_reqquester(None)
    try:
        data_input = request.data
        obj_login = {
            "user_name": data_input['user_name'],
            "password": data_input['password']
        }
        ip_request = request.META['REMOTE_ADDR']
        browser_request = request.META['HTTP_USER_AGENT']
        menu_access = ""
        token = ""
        data_output = models.login_requester(obj_login)
        code_output = data_output['code']
        if code_output == 0:
            user_id = data_output['user_id']
            token = jwt_authen.create_token(user_id, obj_login['user_name'], obj_login['password'], menu_access,
                                            ip_request, browser_request)
        response = contains.get_response_authen_reqquester(code_output)
        response['token'] = token
        response['code'] = code_output
    except Exception as e:
        print("authen.views -> login -> ex", e)

    return Response(response)


def logout_requester(request):
    print(request.META)
    response = contains.get_response_logout(None)
    try:
        token = request.META['HTTP_AUTHORIZATION']
        check_token = jwt_authen.remove_token(token)
        if check_token:
            response = contains.get_response_logout(0)
        else:
            response = contains.get_response_logout(777)
    except Exception as e:
        print("authen.views -> logout -> ex", e)

    return Response(response)
