# function: get_response_list_requester
# parameter:
#           code: int
# return: response - message
# description: response message by code
from rest_framework import status


def get_response_list_requester(code):
    response = {
        'code': 200,
        'message': 'Execute successfully',
        'status_code': status.HTTP_200_OK
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Successfully'
        if code == 1:
            response['message'] = 'Value was wrong'

    return response
