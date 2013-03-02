import unittest

from simplelog import *
from simplelog.decorators import quiet
#TODO: wipe simplelog, make some logs and check the output


def foo():
    return 'foo'

class TestSimpleLog(unittest.TestCase):
    def setUp(self):
        SL.setLevel(DEBUG)

    def test(self):
        # Make sure nothing is throwing an exception
        debug("debug foo")
        info("info foo")
        warning("warn foo")
        error("error foo")
        critical("crit foo")
        self.assertTrue(True);

class TestDecorators(unittest.TestCase):
    def setUp(self):
        pass

    def test_quiet(self):
        log('this is visible')

    @quiet()
    def test_no_quiet(self):
        log('this is not visible')


    def test_dump_func(self):
        return

if __name__ == '__main__':
    unittest.main()
