# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:40:48 2016

@author: jgarrison
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 14:35:42 2016

@author: jgarrison
"""

from datetime import datetime as dt, timedelta
import time
import functools

class RateLimit:
    def __init__(self, callsPerPeriod = 6, inTime = timedelta(0,1), maxCallCount = 30000):
        self.callsPerPeriod = callsPerPeriod
        self.inAmountOfTime = inTime
        self.maxCallCount = maxCallCount
        
        self.startTime = None
        self.callCount = 0
        self.totalCallCount = 0    
        
        #print("Calls per second={0}, inAmountOfTime={1}, maxCallCount={2}".format(self.callsPerPeriod, self.inAmountOfTime, self.maxCallCount))
 
    def __call__(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            
            if(self.totalCallCount > self.maxCallCount):
                raise Exception("You've exceed the total number of calls for this API {0}".format(self.maxCallCount))
                
            if(self.startTime is None):
                self.startTime = dt.now()
                
            currentTime = dt.now() - self.startTime
            
            if(self.callCount < self.callsPerPeriod and currentTime <= self.inAmountOfTime):
                #print("IF: CallCount={0}, currentTime={1}".format(self.callCount, currentTime))
                self.callCount = self.callCount + 1            
            elif(self.callCount >= self.callsPerPeriod and currentTime <= self.inAmountOfTime):
                #print("ELIF: CallCount={0}, currentTime={1}".format(self.callCount, currentTime))
                sleepTime = self.inAmountOfTime - currentTime
                #print("ELIF: SleepTime={0} in microseconds={1} and then... {2}".format(sleepTime, sleepTime.microseconds, sleepTime.microseconds/1000000))
                time.sleep(sleepTime.seconds + sleepTime.microseconds/1000000)
                self.callCount = 1
                self.startTime = dt.now()
            else:
                #print("ELSE: CallCount={0}, currentTime={1}".format(self.callCount, currentTime))
                self.callCount = 1
                self.startTime = dt.now()
                
            x = f(*args, **kwargs)
            self.totalCallCount = self.totalCallCount + 1
            
            return x

        return wrap
