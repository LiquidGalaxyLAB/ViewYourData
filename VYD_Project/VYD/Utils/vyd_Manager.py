from ParseManager.parse_manager import ParseManager
from PresentationManager.placemark_generator import MarkersTour

__author__ = 'Marc'


if __name__ == '__main__':

    parse_manager = ParseManager("https://data.lab.fiware.org/vi/dataset/3c201404-2a1f-4f96-940c-cad892899ea8/resource/6e29f557-7efa-4f5e-8472-914e0a6ec437/download/equipamientos.csv")

    parse_manager.parse()

    print parse_manager.get_type_file()

    print len(parse_manager.get_header())

    data_set = parse_manager.get_data_by_coordinates(1,2,3)



    markersTour = MarkersTour(data_set[0], "test", "https://www.sideshowtoy.com/wp-content/uploads/2013/06/1000761-product-silob.png")
    markersTour.makeFile()