
Simplelog Class Methods:
========================
log(msg, level = None)
  Log message to /tmp/simplelog. Level defaults to env['LOG_LEVEL']

Usage:
======
from simplelog import log

log('Simplelog is running')


######################################################
Simplelog()
    Creates a logger that prints the log files in the current directory.

quiet()
    Stops the logger from printing to standard out

enable()
    Restarts the logger with original path.

SL
    Singleton instance of the simplelog. The log files are stored in /tmp/simplelog.log. Default behavior is to rewrite the log everytime

Decorators:
-----------
enable()
    If simplelog is disabled, enables it for function. Otherwise,
does nothing.

disable()
    If simplelog is enabled, disable it for function. Otherwise does
nothing.

dump_func(level = None, func_name_only = False, pretty = True)

Usage:
=========
import simplelog

SL = simplelog.SL

def foo(bar):
  ...
  x = acc
  SL.debug("value of x: " %s str(x))

# Disabling and Enabling the simplelogger

def bar(foo):
  SL.disable()
  SL.debug("old debug message")
  SL.debug("more debug messsages")
  SL.enable()
