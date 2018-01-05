# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:44:56 2016

Decorator for logging method calls providing the input/output and timing info
Cavet: the current implementation is NOT optimized for performance. Opening/Closing the file for each call will be slow.

@author: jgarrison
"""
import os
import functools
from StopWatch import Stopwatch
from datetime import datetime
import repr      #reprlib is for Python3.*
import logging


class StopWatchLogger:
    def __init__(self, outputFolder='logs', loggerName = None):
        self.outputFolder = outputFolder
        self.loggerName = loggerName
        self.r = repr.Repr()
        self.r.maxlist = 4       # max elements displayed for lists
        self.r.maxstring = 30    # max characters displayed for strings
        
        if not os.path.exists(self.outputFolder):
            os.makedirs(self.outputFolder)

        if(self.loggerName is None):
            self.dir_path = os.path.realpath(os.curdir)
        else:
            self.logger = logging.getLogger(self.loggerName)

    def __call__(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            
            if(self.loggerName is None):
                dateEscapedString = "{0}".format(datetime.utcnow()).replace(' ', '_').replace('-','_').replace(':','_')
                outputfilename = os.path.join(self.dir_path, self.outputFolder, "{0}_{1}.log".format(f.__name__, dateEscapedString))            
            
                with open(outputfilename, 'w', encoding="utf8") as fOut:
                    fOut.write("{0}: BEGIN: call of {1}{2}\n".format(datetime.utcnow(), f.__name__, self.r.repr(args)))
                    methodProcessingTime = Stopwatch()
                    methodProcessingTime.start()
                    x = f(*args, **kwargs)
                    fOut.write("{0}: END  : call of {1}{2} elapsed time {2}\n".format(datetime.utcnow(), f.__name__, self.r.repr(args), methodProcessingTime.time_elapsed))
                    methodProcessingTime.stop()
            else:                
                self.logger.info("BEGIN: call of {0}{1}".format(f.__name__, self.r.repr(args)))
                methodProcessingTime = Stopwatch()
                methodProcessingTime.start()
                x = f(*args, **kwargs)
                self.logger.info("END  : call of {0}{1} elapsed time {2}".format(f.__name__, self.r.repr(args), methodProcessingTime.time_elapsed))
                methodProcessingTime.stop()                
            return x
        return wrap
