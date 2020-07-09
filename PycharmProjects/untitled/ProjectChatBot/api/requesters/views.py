# File: requester.views.py
# Description:
# Author             Date                       Change Description
# bcdai            8/7/2020                     Create new function
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from . import contains, models


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_requester(request):
    print(request.META)
    try:
        response = contains.get_response_list_requester(None)
        data_output = models.login()
        code_output = data_output['code']
        contains.get_response_list_requester(code_output)

    except Exception as e:
        print("requesters.views -> get_requester -> ex", e)

    return Response(response)
