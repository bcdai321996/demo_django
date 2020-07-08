# File: requester.views.py
# Description:
# Author             Date                       Change Description
# Bcdai            8/7/2020                     Create new function
from utils import response_json_common, common_conection


def get_requester():
    connection = None
    cursor = None
    response = response_json_common.get_response_common(None, None)
    try:
        connection = common_conection.get_connection()
        cursor = connection.cursor()
        sql_select = "SELECT * FROM requesters"
        cursor.execute(sql_select)
        response['list_requester'] = cursor.fetchall()
        response['code'] = 0
    except Exception as e:
        print("requester.models ->get_requester -> ex", e)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()

    return response

