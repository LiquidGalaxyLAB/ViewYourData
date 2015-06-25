from Download.downloadmanager import DownloadDataSetManager
from Parser.CsvParser import CsvParser
from Exception import NoParserImplemented

__author__ = 'hellfish90'


class ParseManager(object):

    file_type = None
    file_path = None
    file_name = None
    url = None
    parser = None
    downloadManager = None

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
            raise NoParserImplemented("No parser implemented for this type of file "+self.file_name)


    def get_data_by_location(self, header_position, extra, data_positions):
        pass

    def get_data_by_coordinates(self, pos_latitude, pos_longitude, data_positions):
        pass

    def get_type_file(self):

        return self.file_type


    def get_header(self):
        return self.parser.get_data_types()


if __name__ == '__main__':
    parse_manager = ParseManager("http://www.amsterdamopendata.nl/files/Festivals.csv")

    parse_manager.parse()

    print parse_manager.get_type_file()

    print parse_manager.get_header()