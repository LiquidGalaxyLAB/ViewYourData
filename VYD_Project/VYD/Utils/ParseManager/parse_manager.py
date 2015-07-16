from download.downloadmanager import DownloadDataSetManager
from parser.csv_parser import CsvParser
from exception import NoParserImplemented

__author__ = 'hellfish90'

class ParseManager(object):
    file_type = None
    file_path = None
    file_name = None
    url = None
    parser = None
    downloadManager = None
    parseManager = None
    data = None

    extra_location = None
    location_name = None
    coor_lat = None
    coor_lng = None
    data_loc = None
    type_loc = None

    @staticmethod
    def getParseManager(url, new = False):

        if new == True:
            ParseManager.parseManager = None

        if ParseManager.parseManager != None:
            return ParseManager.parseManager
        else:
            ParseManager.parseManager=ParseManager(url)
            return ParseManager.parseManager

    def __init__(self, url):
        self.url = url
        self.downloadManager = DownloadDataSetManager()
        self.downloadManager.set_url(self.url)

    def parse(self):
        self.downloadManager.download()
        self.file_type = self.downloadManager.get_type()
        self.file_path = self.downloadManager.get_file_path()
        self.file_name = self.downloadManager.get_file_name()
        self.downloadManager.get_file_path()

        if self.file_type == "csv":
            self.parser = CsvParser(self.file_path)
        else:
            raise NoParserImplemented("No parser implemented for this type of file " + self.file_name)

    def get_data_by_location(self, data_position, location_name_point, location_extra_name):
        self.Parse = self.parser.get_set_by_data_and_location(data_position, location_name_point, location_extra_name)
        return self.data

    def get_data_by_coordinates(self, pos_latitude, pos_longitude, data_positions):
        self.data = self.parser.get_set_by_data_and_coordinates(data_positions, pos_latitude, pos_longitude)
        return self.data

    def get_type_file(self):
        return self.file_type

    def get_file_name(self):
        return self.file_name

    def get_header(self):
        return self.parser.get_data_types()


if __name__ == '__main__':
    parse_manager = ParseManager("http://mappe.regione.toscana.it/db-webgis/biblio/example_postgis.jsp?format=csv")

    parse_manager.parse()

    print parse_manager.get_type_file()

    print len(parse_manager.get_header())

    print parse_manager.get_data_by_location(1,5,"")