import simplelog
import unittest

SL = simplelog.sl

class TestSimpleLog(unittest.TestCase):
    def setUp(self):
        global SL
        self.sl = simplelog.sl

    def test_disable(self):
        """
        Remove all handlers from simplelog
        """
        self.sl.disable()
        self.assertTrue(self.sl.handlers == [])

    def test_set_level(self):
        SL.debug("hello")
        # Should show up
        SL.setLevel(20)
        SL.debug("foo")
        # Should not show up
        SL.disable()
        SL.debug("foo")
        # Should not show up
        SL.enable()
        SL.debug("foo")
        # None
        SL.info("foo")
        # "foo"


@simplelog.dump_func()
def func1(arg1, arg2):
    """
    nul op func
    """
    return

class TestDecorators(unittest.TestCase):
    def setUp(self):
        self.sl = simplelog.sl

    def test_dump_func(self):
        return

