import pymysql.cursors

from ProjectChatBot import settings


def get_connection():
    connection = None

    try:
        connection = pymysql.connect(
            host=settings.MSQL_CHATBOT_HOST,
            port=int(settings.MSQL_CHATBOT_POST),
            db=settings.MSQL_CHATBOT_DB,
            user=settings.MSQL_CHATBOT_USER,
            password=settings.MSQL_CHATBOT_PASS,
            cursorclass=pymysql.cursors.DictCursor
        )

    except Exception as e:
        print("utils.common_connetion -> get_connection -> ex", e)
    print("Connect successfully!!")
    return connection
