# coding=utf-8

__author__ = 'Marc Solé Farré'
import simplekml
from polycircles import polycircles


class CircleGenerator(object):
    def __init__(self, data_set, kml_name, color, altitude, multiplier, opacity=None):
        self.data_set = data_set
        self.kml_name = kml_name
        self.color = color
        self.altitude = altitude
        self.multiplier = multiplier
        self.opacity = opacity

    def generate(self):

        kml = simplekml.Kml(open=1)

        polygon_circle = []

        for data in self.data_set:

            shape_polycircle = kml.newmultigeometry(name=data['data'])

            print int(data['data'])

            polycircle = polycircles.Polycircle(latitude=data['coordinates']['lat'],
                                                longitude=data['coordinates']['lng'],
                                                radius=(int(data['data']) + 1) * self.multiplier,
                                                number_of_vertices=36)

            latloncircle = polycircle.to_lon_lat()
            latlonaltcircle = []

            for element in latloncircle:
                tup = (element[0], element[1], self.altitude,)

                latlonaltcircle.append(tup)

            print latlonaltcircle

            pol = shape_polycircle.newpolygon()
            pol.outerboundaryis = latlonaltcircle

            pol.altitudemode = simplekml.AltitudeMode.relativetoground
            pol.extrude = 5
            pol.style.polystyle.color = simplekml.Color.changealphaint(200, self.set_color(self.color))
            pol.style.linestyle.color = simplekml.Color.changealphaint(230, self.set_color(self.color))

            polygon_circle.append(polycircle)

        kml.save("kmls_management/static/" + self.kml_name)

    def set_color(self, color):
        if color == "Yellow":
            return simplekml.Color.yellow
        if color == "Red":
            return simplekml.Color.red
        if color == "Green":
            return simplekml.Color.green
        if color == "Blue":
            return simplekml.Color.blue