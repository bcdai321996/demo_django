# function: get_response_list_requester
# parameter:
#           code: int
# return: response - message
# description: response message by code
from rest_framework import status


def get_response_authen_reqquester(code):
    response = {
        'code': 200,
        'message': 'Execute successfully',
        'status_code': status.HTTP_200_OK
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Login Successfully'
        if code == 1:
            response['message'] = 'Password does not exist'

        if code == 2:
            response['message'] = 'User name does not exist '

    return response

<<<<<<< HEAD
# Logout requester
def get_response_logout_requester(code):
=======

def get_response_logout(code):
>>>>>>> parent of b3781a8... refacter code
    response = {
        'code': 200,
        'message': 'Execute successfully',
        'status_code': status.HTTP_200_OK
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Logout Successfully'
        if code == 777:
            response['message'] = 'Token does not exist'

    return response
