from distutils.core import setup
#TODO: add long description

PACKAGE = "simplelog"
NAME = "simplelog"
DESCRIPTION = "Simple logging interface for python"
AUTHOR = "Kevin S  Lin"
AUTHOR_EMAIL = "kevinslin8@gmail.com"
URL = ""
VERSION = __import__(PACKAGE).__version__


#with open("README.rst") as fh:
        #long_description = fh.read()

setup(name = 'simplelog',
      version = VERSION,              
      description = 'Simple interface for logging in python',
      long_description = '',
      author = 'Kevin S Lin',
      author_email = 'kevinslin8@gmail.com',
      url = 'kevinslin.com',
      packages = ['simplelog']
      )   
