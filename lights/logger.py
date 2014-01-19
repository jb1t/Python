from pymongo import Connection
#import pymongo
from datetime import datetime

__author__ = 'jeffgarrison'


class MongoLogger:
    def __init__(self, host, port):
        self.conn = Connection(host, port)
        #self.conn = pymongo.MongoClient(host, port)
        self.db = self.conn.log
        self.log = self.db.log

    def write(self, message, request=None):
        log_entry = {'message': message, 'date_time_utc': datetime.utcnow(), 'request': None}
        if request is not None:
            log_entry['request'] = self.get_request_details(request)
        self.log.insert(log_entry)
        assert isinstance(request, object)
        print request

    @staticmethod
    def get_request_details(request):
        details = {'url': request.url, 'ip': request.remote_addr}
        headers = []
        for key, value in request.headers.iteritems():
            if not key.startswith("_"):
                headers.append({key: value})
        details['headers'] = headers
        return details