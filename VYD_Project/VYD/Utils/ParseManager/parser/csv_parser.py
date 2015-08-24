import csv

import coordinates
import parser


__author__ = 'hellfish90'

# sudo apt-get install python3-magic


class CsvParser(parser.Parser):
    def get_data_types(self):

        self.csv_file = open(self.filename, 'rb')
        dialect = csv.Sniffer().sniff(self.csv_file.read(1024))

        print "Delimiter: ' " + str(dialect.delimiter) + " ' "
        self.csv_Reader = csv.reader(self.csv_file, dialect)
        self.csv_file.seek(0)

        u_headers = []

        # Search the header
        while len(u_headers) < 1:
            headers = self.csv_Reader.next()

            for item in headers:
                u_head = item.decode(self.encoding)
                u_headers.append(u_head)

        return u_headers

    def get_set_by_data_and_coordinates(self, data_point, latitude_point, longitude_point):

        data_set = []
        self.csv_file.seek(0)
        self.csv_Reader.next()

        lose_rows = []

        for row in self.csv_Reader:
            if len(row) != 0:

                lat = float(row[latitude_point].decode(self.encoding))
                lng = float(row[longitude_point].decode(self.encoding))

                print lat
                print lng
                data = row[data_point].decode(self.encoding)

                data_row = {'data': data}

                if coordinates.correct_coordinates(lat, lng):
                    coordinate = {'lat': lat, 'lng': lng}
                    data_row['coordinates'] = coordinate
                    data_set.append(data_row)
                else:
                    lose_rows.append(row)

        return [data_set, lose_rows]

    def get_set_by_data_and_location(self, data_point, location_point, location_extra=""):

        data_set = []
        self.csv_file.seek(0)
        self.csv_Reader.next()

        lose_rows = []

        for row in self.csv_Reader:

            if len(row) != 0:
                if location_point != -1:
                    loc = row[location_point].decode(self.encoding)
                else:
                    loc = ""
                data = row[data_point].decode(self.encoding)

                data_row = {'data': data}
                coor = coordinates.get_coordinates_by_location([loc, location_extra])

                if coor is not None:
                    data_row['coordinates'] = coor
                    data_set.append(data_row)
                else:
                    lose_rows.append(row)

        return [data_set, lose_rows]

    def get_data(self):

        data = []
        print "encoding:", self.encoding
        self.csv_file.seek(0)
        for row in self.csv_Reader:
            data.append(row)

        return data

    def close_file(self):
        self.csv_file.close()