"""In Memory Database
APIs
1. get
2. put
3. dict
4.
5.
"""
import logging

class Database:

    def __init__(self):
        logging.debug('Initialized In Memory Database!!')
        self.__db__ = {}

    def dict(self) ->{}:
        return self.__db__

    def get(self, key: str):
        if key in self.__db__:
            return self.__db__[key]
        return None

    def put(self, key: str, value):
        self.__db__[key] = value

    def clear(self, prefix: str):
        clone_db = {}
        for key, value in self.__db__.items():
            if not key.startswith(prefix):
                clone_db[key] = value
        self.__db__ = clone_db

    def reset(self):
        self.__db__ = {}

db = Database()
