# Copyright: This module has been placed under the public license

"""
This is the SimpleLog Documentation Package.

Package Structure:
==================

Modules:
-------
__init__.py
    Contains the SimpleLog class

Subpackages:
-----------
None yet
"""

__docformat__ = 'reStructuredText'

__version__ = '0.22'

__version_details__ = 'alpha release'

__all__ = ["SimpeLog", "sl", "decorators"]

__author__ = "Kevin S Lin <kevinslin8@gmail.com>"

import inspect
import logging
import logging.config
import logging.handlers
import os
import warnings

#from decorators import dump_func, enable
#DEPRECIATED
SIMPLE_FORMAT = "[%(levelname)s]: %(asctime)s: %(message)s"
SIMPLE_FORMATTER = logging.Formatter(fmt = SIMPLE_FORMAT, datefmt = "%H:%m.%S")

#Singleton instance
env = {}

def _initialize():
    global env
    if (env):
        pass
    else:
        env['LOG_LEVEL'] = logging.DEBUG
        env['LOG_FILE'] = '/tmp/simplelog.log'
        env['LOG_FORMAT'] = "[%(levelname)s]: %(asctime)s: %(message)s"
        env['LOG_FORMATTER'] = logging.Formatter(fmt = SIMPLE_FORMAT,
                                    datefmt = "%H:%m.%S")



_initialize()
# Configure Logger
logger = logging.getLogger("simplelog")
logger.setLevel(env['LOG_LEVEL'])
handler_file = logging.FileHandler(filename = env['LOG_FILE'])

handler_file.setFormatter(env['LOG_FORMATTER'])

logger.addHandler(handler_file)

def log(msg, level = None):
    """
    Log the output. Nothing more, nothing less
    """
    global logger
    if (level == None):
        level = env['LOG_LEVEL']
    logger.log(level, msg)

#BOND

######################################################################
class SimpleLog(logging.Logger):
    """
    Simplelog, because you have better things to do then worry about logging.

    """
    def __init__(self, name="simplelog", level=logging.NOTSET,
                    path = None, verbose = False, quiet = False,
                    force = False):
        """
        @param:
        name - name of log, default is simplelog
        level - log level
        fname - filepath, defaults to <cwd>/simplelog.log
        path - default is current directory, 'tmp' puts log in /tmp folder
        verbose - if true, prints very detailed messages in dump
        quiet - print message to standard out?
        force - remove old folder if it exists
        @return:
        simple log logger object
        """
        super(SimpleLog, self).__init__(name, level)
        warnings.simplefilter("ignore")
        warnings.warn("this class is depreciated", DeprecationWarning)


        # Default is simplelog in current directory
        if (path == None):
            path = os.path.join(os.getcwd(), "simplelog.log")
        elif(path == "tmp"):
            path = "/tmp/simplelog.log"
        try:
            if (force): os.remove("path")
        except OSError:
            pass

        #State
        self.DIVIDER = "=========="
        self.path = path
        self.quiet = quiet
        self.sl_debug = logging.getLogger('alog')

        #Handlers
        if not quiet:
            self.sh = logging.StreamHandler()
            self.sh.setFormatter(SIMPLE_FORMATTER)

        fh = logging.FileHandler(filename=path)
        fh.setFormatter(SIMPLE_FORMATTER)

        self.setLevel(level)
        self.addHandler(self.sh)
        self.addHandler(fh) #TODO: don't have this here

        #TODO: make this work
        self.sl_debug.setLevel(logging.DEBUG)
        self.sl_debug.addHandler(fh)

    def setLevel(self, level):
        """
        Set level for simplelog and its handlers
        """
        super(SimpleLog, self).setLevel(level)
        for hndl in self.handlers:
            hndl.setLevel(level)

    def disable(self):
        """
        Dispale simplelog
        """
        self.handlers = [] #could this result in a memory leak?
        assert(self.handlers == [])

    def enable(self):
        """
        Enable simplelog
        """
        self.__init__(path = self.path, quiet = self.quiet,
                    level = self.level)

    def quiet(self):
        """
        Remove the stream handler
        """
        self.quiet = True
        self.removeHandler(self.sh)

    def log(self, level, msg, *args, **kwargs):
        super(SimpleLog, self).log(level, msg, *args, **kwargs)
        self.sl_debug.log(level, msg, *args, **kwargs)

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

SL = sl = SimpleLog(path="/tmp/simplelog.log", force = True)

if __name__ == "__main__":
    print(sl)



