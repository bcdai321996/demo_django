import rest_framework


def get_response_common(code, message):
    response = {
        "code": 999,
        "message": "System busy, please try again later !",
        "status_code": rest_framework.status.HTTP_200_OK
    }

    if code is not None:
        response["code"] = code

    if message is not None:
        response["message"] = message

    return response
