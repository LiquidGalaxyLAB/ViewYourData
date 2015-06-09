import Coordinates
from Parser import Parser
import csv

__author__ = 'hellfish90'

# sudo apt-get install python3-magic


class CsvParser(Parser):

    def get_header(self):

        self.csv_file = open(self.filename, 'rb')
        dialect = csv.Sniffer().sniff(self.csv_file.read(1024))
        self.csv_Reader = csv.reader(self.csv_file, dialect)
        self.csv_file.seek(0)
        headers = self.csv_Reader.next()

        u_headers = []

        for item in headers:
            u_head = item.decode(self.encoding)
            u_headers.append(u_head)

        return u_headers

    def get_set_of_data_with_coordinates(self, data_point, latitude_point, longitude_point):

        data_set = []
        self.csv_file.seek(0)
        self.csv_Reader.next()

        lose_rows = []

        for row in self.csv_Reader:
            lat = row[latitude_point].decode(self.encoding)
            lng = row[longitude_point].decode(self.encoding)
            data = row[data_point].decode(self.encoding)

            data_row = {'data': data}

            if Coordinates.correct_coordinates(lat, lng):
                data_row['lat'] = lat
                data_row['lng'] = lng
                data_set.append(data_row)
            else:
                lose_rows.append(row)

        return data_set, lose_rows

    def get_set_of_data_with_location(self, data_point, location_point, location_extra):

        data_set = []
        self.csv_file.seek(0)
        self.csv_Reader.next()

        lose_rows = []

        for row in self.csv_Reader:
            loc = row[location_point].decode(self.encoding)
            data = row[data_point].decode(self.encoding)

            data_row = {'data': data}
            coordinates = Coordinates.get_coordinates_by_location([loc, location_extra])

            if coordinates is not None:
                data_row.update(coordinates)
                data_set.append(data_row)
            else:
                lose_rows.append(row)

        return data_set, lose_rows

    def get_data(self):

        data = []
        print "encoding:", self.encoding
        self.csv_file.seek(0)
        for row in self.csv_Reader:
            data.append(row[0].decode(self.encoding))

        return data

    def close_file(self):
        self.csv_file.close()