#!/usr/bin/env python2.7
# Copyright: This module has been placed under the public license

"""
Because you have better things to do.
"""

import inspect
import logging
import logging.config
import logging.handlers
import os
from settings import *

__version__ = "0.2.1"


class SimpleLog(logging.Logger):
    """
    Simplelog, because you have better things to do then worry about logging.
    """
    def __init__(self, name=SIMPLELOG, level=logging.NOTSET,
                    path = None,  quiet = False,
                    force = False):
        """
        @param:
        name - name of log, default is simplelog
        level - log level
        fname - filepath, defaults to <cwd>/simplelog.log
        path - default is current directory, 'tmp' puts log in /tmp folder
        quiet - print message to standard out?
        force - remove old folder if it exists
        @return:
        simple log logger object
        """
        super(SimpleLog, self).__init__(name, level)

        # Default is simplelog in current directory
        if (path == None):
            path = os.path.join(os.getcwd(), "simplelog.log")
        elif(path == "tmp"):
            path = "/tmp/simplelog.log"
        # delete path if it exists
        try:
            if (force): os.remove("path")
        except OSError:
            pass

        #State
        self.path = path
        self.quiet = quiet
        #TODO: what?
        #self.sl_debug = logging.getLogger('alog')

        #Handlers
        if not quiet:
            self.sh = logging.StreamHandler()
            self.sh.setFormatter(SIMPLE_FORMATTER)
            self.addHandler(self.sh)

        fh = logging.FileHandler(filename=path)
        fh.setFormatter(SIMPLE_FORMATTER)
        self.addHandler(fh) #TODO: don't have this here
        self.setLevel(level)

        #self.sl_debug.addHandler(fh)

    def setLevel(self, level):
        """
        Set level for simplelog and its handlers

        :param level: debug level to set
        """
        super(SimpleLog, self).setLevel(level)
        for hndl in self.handlers:
            hndl.setLevel(level)

    def setFormatter(self, format):
        """
        Sets format in each handler
        :params format: either a Formatter object or format string
        """
        if not isinstance(format, logging.Formatter):
            format = logging.Formatter(format, FMT_DATETIME)
        for hndl in self.handlers:
            hndl.setFormatter(format)

    def disable(self):
        """
        Disable simplelog by getting rid of all handlers
        """
        self.handlers = [] #could this result in a memory leak?
        assert(self.handlers == [])

    def enable(self):
        """
        Enable simplelog
        """
        self.__init__(path = self.path, quiet = self.quiet,
                    level = self.level)

    #def quiet(self):
        #"""
        #Remove the stream handler
        #"""
        #self.quiet = True
        #self.removeHandler(self.sh)

    def log(self, level, msg, *args, **kwargs):
        super(SimpleLog, self).log(level, msg, *args, **kwargs)
        #self.sl_debug.log(level, msg, *args, **kwargs)

    def dump(self, var_name):
        """
        Prints the content of the string along with the string name
        @param:
        var_name - a string constant
        @return:
        none
        """
        #TODO: this doesn't work [critical, bug]
        try:
            value = locals()[var_name]
        except KeyError:
            value = globals()[var_name]
        self.log(self.level, self.var_name + ":" + str(value))

    @property
    def config():
        return self.config

### Convenience
SL = sl = SimpleLog(path="/tmp/simplelog.log", level = logging.INFO, force = True)

#TODO: support *args
def log(msg, level = None):
    """
    Log the output. Nothing more, nothing less
    """
    level = SL.level
    SL.log(level, msg)

def debug(msg):
    level = logging.DEBUG
    log(msg, level)

def info(msg):
    level = logging.INFO
    log(level, msg)

def error(msg):
    level = logging.ERROR
    log(level, msg)

def warning(msg):
    level = logging.WARNING
    log(msg, level)

def critical(msg):
    level = logging.CRITICAL
    log(msg, level)
