from CsvParser import CsvParser


__author__ = 'hellfish90'

if __name__ == '__main__':

    filename = "test_data2.csv"
    parser = CsvParser(filename)
    header = parser.get_data_types()

    data_set = parser.get_set_by_data_and_location(0, 7, "Lleida")

    for item in header:
        print item,

    print ""

    for data in data_set[0]:
        print data['lat'], data['lng'], data['data']

    print "Missed Rows: ", len(data_set[1])

    parser.close_file()