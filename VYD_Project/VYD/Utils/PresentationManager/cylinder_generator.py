__author__ = 'Marc'
import simplekml
from polycircles import polycircles


class CylinderGenerator(object):
    def __init__(self, data_set, kml_name, color, altitude, multiplier, radius):
        self.data_set = data_set
        self.kml_name = kml_name
        self.color = color
        self.altitude = altitude
        self.multiplier = multiplier
        self.radius = radius

    def generate(self):


        kml = simplekml.Kml(open=1)

        polygon_circle = []

        for data in self.data_set:
            shape_polycircle = kml.newmultigeometry(name=data['data'])

            print int(data['data'])

            polycircle = polycircles.Polycircle(latitude=data['coordinates']['lat'],
                                                longitude=data['coordinates']['lng'],
                                                radius=self.radius,
                                                number_of_vertices=100
                                                )

            latloncircle = polycircle.to_lon_lat()
            latlonaltcircle = []

            for element in latloncircle:
                tup = (element[0], element[1], (int(data['data']) * self.multiplier) + 10,)
                latlonaltcircle.append(tup)

            for element in latloncircle:
                tup = (element[0], element[1], int(data['data']) * self.multiplier,)
                latlonaltcircle.append(tup)
                tup = (element[0], element[1], 0,)
                latlonaltcircle.append(tup)

            for element in latloncircle:
                tup = (element[0], element[1], 0,)
                latlonaltcircle.append(tup)
                tup = (element[0], element[1], int(data['data']) * self.multiplier,)
                latlonaltcircle.append(tup)

            for element in latloncircle:
                tup = (element[0], element[1], 0,)
                latlonaltcircle.append(tup)

                latlonaltcircle.append(tup)

            print latlonaltcircle

            pol = shape_polycircle.newpolygon()
            pol.outerboundaryis = latlonaltcircle

            pol.altitudemode = simplekml.AltitudeMode.relativetoground
            pol.extrude = 5
            pol.style.polystyle.color = simplekml.Color.changealphaint(230, self.set_color(self.color))
            pol.style.linestyle.color = simplekml.Color.changealphaint(230, self.set_color(self.color))
            pol.style.linestyle.width = 5000

            polygon_circle.append(polycircle)

            latlonaltcircle = []

            for element in latloncircle:
                tup = (element[0], element[1], (int(data['data']) * self.multiplier) + 10,)
                latlonaltcircle.append(tup)
            pol = shape_polycircle.newpolygon()
            pol.outerboundaryis = latlonaltcircle

            pol.altitudemode = simplekml.AltitudeMode.relativetoground
            pol.extrude = 5
            pol.style.polystyle.color = simplekml.Color.changealphaint(230, self.set_color(self.color))
            pol.style.linestyle.color = simplekml.Color.changealphaint(230, self.set_color(self.color))
            pol.style.linestyle.width = 5000

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