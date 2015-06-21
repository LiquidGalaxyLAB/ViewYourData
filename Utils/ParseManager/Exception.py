__author__ = 'hellfish90'


class NoParserImplemented(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)