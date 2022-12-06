from pymongo import MongoClient


def get_db_handle():

    client = MongoClient(
        host='localhost',
        port=27017,
    )
    return client['AviFest']