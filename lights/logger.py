from pymongo import Connection
from datetime import datetime

__author__ = 'jeffgarrison'


class MongoLogger:
    def __init__(self, host, port):
        self.conn = Connection(host, port)
	self.db = self.conn.log
        self.log = self.db.log

    def write(self, message):
        self.log.insert({'message': message, 'date_time_utc': datetime.utcnow()})
