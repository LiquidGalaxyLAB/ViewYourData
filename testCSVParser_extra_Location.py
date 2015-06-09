from CsvParser import CsvParser


__author__ = 'hellfish90'

if __name__ == '__main__':

    filename = "test_data2.csv"
    parser = CsvParser(filename)
    header = parser.get_header()

    #print Coordinates.get_coordinates_by_location(["C/Diputacio"])

    data_set = parser.get_set_of_data_with_location(0, 7, "Lleida")

    for item in header:
        print item,

    print ""

    for data in data_set:
        print data['lat'], data['lng'], data['data']
    parser.close_file()