# File: requester.views.py
# Description:
# Author             Date                       Change Description
# Bcdai            8/7/2020                     Create new function
from utils import response_json_common, common_conection


def login(obj_login):
    connection = None
    cursor = None
    list_requesters = []
    response = response_json_common.get_response_common(None, None)
    try:
        connection = common_conection.get_connection()
        cursor = connection.cursor()
        sql_select = "SELECT * FROM requesters WHERE LCASE(user_name) = LCASE(%s)"
        cursor.execute(sql_select, obj_login['user_name'])
        if cursor.rowcount > 0:
            list_requesters = cursor.fetchall()
            for item in list_requesters:
                if item['password'] == obj_login['password']:
                    response['code'] = 0
                    response['user_id'] = item['id']

                else:
                    response['code'] = 1
        else:
            response['code'] = 2

    except Exception as e:
        print("authen.models ->login -> ex", e)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()

    return response
