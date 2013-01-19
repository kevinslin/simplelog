import logging

# Filters
class NullFilter(logging.Filter):
    """
    Null Filter
    """
    def filter(self, record):
        print("filter")
        return False

class QuietUnlessExceptionFilter(logging.Filter):
    def __init__(self):
        self.records = []

    def filter(self, record):
        print("filtered")
        self.records.append(record)
        return False
