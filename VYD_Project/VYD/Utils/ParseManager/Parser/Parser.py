__author__ = 'hellfish90'

from abc import abstractmethod
from chardet.universaldetector import UniversalDetector


class Parser(object):
    def __init__(self, filename):
        self.filename = filename
        self.encoding = self.get_encoding()
        self.file = None



    def open_file(self):
        self.file = open(self.filename, 'rb')

    def close_file(self):
        self.file.close()


    # Return a set of the data types
    @abstractmethod
    def get_data_types(self):
        raise NotImplementedError("Please Implement this method")

    # Return two sets of data:
    # The first is a set of dictionaries of the lat, lng and data by the data_point, coordinates.
    #   *location_extra is a extra variable for help the search of the location
    # The second set contains the rows that can't get coordinates

    # Example:
    # data_set = get_set_of_data_with_location(0,1,"Barcelona")
    # data = data_set[0]
    # data['coordinates']['lat']
    # data['coordinates']['lng']
    # data['data']
    #
    # bad_rows = data_set[1]
    # bad_row = bad_rows[0]

    @abstractmethod
    def get_set_by_data_and_coordinates(self, data_point, latitude_point, longitude_point):
        raise NotImplementedError("Please Implement this method")

    # Return two sets of data:
    # The first is a set of dictionaries of the lat, lng and data by the data_point, location_point.
    #   *location_extra is a extra variable for help the search of the location
    # The second set contains the rows that can't get coordinates

    # Example:
    # data_set = get_set_of_data_with_location(0,1,"Barcelona")
    # data = data_set[0]
    # data['coordinates']['lat']
    # data['coordinates']['lng']
    # data['data']
    #
    # bad_rows = data_set[1]
    # bad_row = bad_rows[0]

    @abstractmethod
    def get_set_by_data_and_location(self, data_point, location_point, location_extra=""):
        raise NotImplementedError("Please Implement this method")

    # Load the encoding of the file

    def get_encoding(self):
        file = open(self.filename, 'rb')

        detector = UniversalDetector()
        for line in file.readlines():
            detector.feed(line)
        detector.close()
        file.close()
        return detector.result['encoding']