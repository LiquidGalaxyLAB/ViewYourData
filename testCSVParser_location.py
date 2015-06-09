from CsvParser import CsvParser

__author__ = 'hellfish90'

if __name__ == '__main__':

    filename = "test_data.csv"
    parser = CsvParser(filename)
    header = parser.get_header()

    #print Coordinates.get_coordinates_by_location(["C/Diputacio"])

    data_set = parser.get_set_of_data_with_location(1, 1, "")

    for item in header:
        print item,

    print ""

    for data in data_set[0]:
        print data['lat'], data['lng'], data['data']


    print "Losed Rows: ", len(data_set[1])

    parser.close_file()