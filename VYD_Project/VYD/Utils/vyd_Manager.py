from ParseManager.parse_manager import ParseManager
from PresentationManager.placemark_generator import MarkersTour
from PresentationManager.polygon_generator import polygon_generator
from PresentationManager.cylinder_generator import CylinderGenerator
from PresentationManager.circle_generator import CircleGenerator
from PresentationManager.dome_generator import DomeGenerator

__author__ = 'Marc'


if __name__ == '__main__':

    url = "https://data.lab.fiware.org/dataset/76f7abda-2b8b-4af2-94a5-287f4822afec/resource/1b9ecca2-80a2-43fe-b7b2-a91b697be020/download/plantago0415.csv"
    parse_manager = ParseManager(url)

    parse_manager.parse()

    print parse_manager.get_type_file()

    print len(parse_manager.get_header())

    data_set = parse_manager.get_data_by_location(5,0,"Spain")

    print data_set
    """
    polygon_manager = polygon_generator(data_set[0], "test_polygon", "Red", 8000,5000,"75")

    polygon_manager.cylinder_generator()

    """

    """
    Test Cylinder
    """
    """
    cylinder_generator = CylinderGenerator(data_set[0], "test_polygon", "Red", 8000,5000, 8000)
    cylinder_generator.generate()
    """


    """
    Test circle
    """
    """
    circle_generator = CircleGenerator(data_set[0], "test_polygon_circle", "Red", 8000,5000, 8000)
    circle_generator.generate()
    """

    """
    Test markers
    """
    """
    marker_generator = MarkersTour(data_set[0], "test_marker", "http://lalocal.tianat.cat/wp-content/uploads/2014/03/N%C3%BAvol_Kinton-300x162.png")
    marker_generator.makeFile()

    """


    """
    Test dome
    """

    dome_generator = DomeGenerator(data_set[0], "test_polygon_dome", "Red", 100,0.5, 75)
    dome_generator.generate()



    #markersTour = MarkersTour(data_set[0], "test", "https://www.sideshowtoy.com/wp-content/uploads/2013/06/1000761-product-silob.png")
    #markersTour.makeFile()