from ParseManager.parse_manager import ParseManager
from PresentationManager.placemark_generator import MarkersTour
from PresentationManager.polygon_generator import polygon_generator

__author__ = 'Marc'


if __name__ == '__main__':

    url = "https://data.lab.fiware.org/dataset/76f7abda-2b8b-4af2-94a5-287f4822afec/resource/1b9ecca2-80a2-43fe-b7b2-a91b697be020/download/plantago0415.csv"
    parse_manager = ParseManager(url)

    parse_manager.parse()

    print parse_manager.get_type_file()

    print len(parse_manager.get_header())

    data_set = parse_manager.get_data_by_location(5,0,"Spain")

    print data_set

    polygon_manager = polygon_generator(data_set[0], "test_polygon", "Green", 5000,0.5,"75")

    polygon_manager.dome_generator()


    #markersTour = MarkersTour(data_set[0], "test", "https://www.sideshowtoy.com/wp-content/uploads/2013/06/1000761-product-silob.png")
    #markersTour.makeFile()