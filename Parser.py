__author__ = 'hellfish90'

from abc import abstractmethod
from chardet.universaldetector import UniversalDetector


class Parser(object):
    def __init__(self, filename):
        self.filename = filename
        self.set_encoding()

    @abstractmethod
    def get_header(self):
        raise NotImplementedError("Please Implement this method")



    @abstractmethod
    def get_set_of_data_with_coordinates(self, data_point, latitude_point, longitude_point):
        raise NotImplementedError("Please Implement this method")

    # Return two sets of data:
    # The first is a set of dictionaries of the lat, lng and data with the data_point, location_point.
    #   *location_extra is a extra variable for help the search of the location
    # The second set contains the rows that can't get coordinates

    # Example:
    # data_set = get_set_of_data_with_location(0,1,"Barcelona")
    # data = data_set[0]
    # data['lat']
    # data['lng']
    # data['data']
    #
    # bad_rows = data_set[1]
    # bad_row = bad_rows[0]
    @abstractmethod
    def get_set_of_data_with_location(self, data_point, location_point, location_extra=" "):
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Please Implement this method")

    def set_encoding(self):
        file = open(self.filename, 'rb')

        detector = UniversalDetector()
        for line in file.readlines():
            detector.feed(line)
        detector.close()
        file.close()
        self.encoding = detector.result['encoding']