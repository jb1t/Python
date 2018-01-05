import requests
import time
import logging
import logging.config
import sys
sys.path.append('../utils')
from StopWatchLogger import StopWatchLogger

#Setup logging
logging.config.fileConfig('logging_config.ini', defaults={'logfilename':'test.log'})
logger = logging.getLogger('keepalive')
stopwatchLogger = StopWatchLogger(loggerName=logger.name)

sleep_time_in_minutes = 4

@stopwatchLogger
def RequestPage(url):
    print("requesting {0}".format(url))
    r = requests.get(url)
    print("{0} status code".format(r.status_code))

while True:
    RequestPage("http://thefullstacknerd.com")
    RequestPage("http://thefullstacknerd.com/2017/12/31/noise-maker-ring-in-the-new-year/")
    
    print("Sleep for {0} minutes".format(sleep_time_in_minutes))
    time.sleep(sleep_time_in_minutes*60)
