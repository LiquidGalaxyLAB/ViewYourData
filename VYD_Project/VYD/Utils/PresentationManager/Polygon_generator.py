__author__ = 'Marc'
import simplekml
from polycircles import polycircles
import subprocess
import os


class polygon_generator(object):
    def __init__(self, data_set, kml_name, color, altitude, multiplier, opacity=None):
        self.data_set = data_set
        self.kml_name = kml_name
        self.color = color
        self.altitude = altitude
        self.multiplier = multiplier
        self.opacity = opacity

    def make_polygons_file(self):
        kml = simplekml.Kml()
        pol = kml.newpolygon(name='A Polygon')
        polygon_points = []
        first = None
        truecolor = self.set_color(self.color)

        for data in self.data_set:
            if first == None:
                first = (
                    data['coordinates']['lng'], data['coordinates']['lat'], int(data['data']) * self.altitude + 2000)
            polygon_points.append(
                (data['coordinates']['lng'], data['coordinates']['lat'], int(data['data']) * self.altitude + 2000))

        polygon_points.append(first)
        # pol.outerboundaryis = [(18.333868,-34.038274, 1800), (18.370618,-34.034421,700),
        # (18.350616,-34.051677,1800),(18.333868,-34.038274,600),
        #                       (18.4,-34.038274, 1800), (18.5,-34.034421,700),
        #                       (18.43,-34.051677,1800), (18.51,-34.038274,600)]

        pol.outerboundaryis = polygon_points

        pol.altitudemode = simplekml.AltitudeMode.relativetoground
        pol.extrude = 100
        pol.style.polystyle.color = simplekml.Color.changealphaint(190, truecolor)
        pol.style.linestyle.color = simplekml.Color.changealphaint(230, truecolor)

        kml.save("" + self.kml_name + ".kml")

    def set_color(self, color):
        if color == "Yellow":
            return simplekml.Color.yellow
        if color == "Red":
            return simplekml.Color.red
        if color == "Green":
            return simplekml.Color.green
        if color == "Blue":
            return simplekml.Color.blue


    def make_polygons_bar_char_file(self):
        kml = simplekml.Kml()

        set_pol_data = []
        print self.data_set
        pol = kml.newpolygon(name='Polygon')

        set_pol_data.append(pol)
        polygon_points = []
        first = None
        for data in self.data_set:
            if first == None:
                first = (
                    data['coordinates']['lng'], data['coordinates']['lat'], int(data['data']) * self.altitude + 2000)
            polygon_points.append(
                (data['coordinates']['lng'], data['coordinates']['lat'], int(data['data']) * self.altitude + 2000))
            polygon_points.append((data['coordinates']['lng'], data['coordinates']['lat'], 500))
            polygon_points.append((
                data['coordinates']['lng'], data['coordinates']['lat'] + 0, 05,
                int(data['data']) * self.altitude + 2000))
            polygon_points.append((data['coordinates']['lng'], data['coordinates']['lat'], 500))
            polygon_points.append((
                data['coordinates']['lng'] - 0, 05, data['coordinates']['lat'],
                int(data['data']) * self.altitude + 2000))
            polygon_points.append((data['coordinates']['lng'], data['coordinates']['lat'], 500))
            polygon_points.append((
                data['coordinates']['lng'], data['coordinates']['lat'] - 0, 05,
                int(data['data']) * self.altitude + 2000))
            polygon_points.append((data['coordinates']['lng'], data['coordinates']['lat'], 500))
            polygon_points.append((
                data['coordinates']['lng'] - 0, 05, data['coordinates']['lat'],
                int(data['data']) * self.altitude + 2000))
            polygon_points.append((data['coordinates']['lng'], data['coordinates']['lat'], 500))
            polygon_points.append(
                (data['coordinates']['lng'], data['coordinates']['lat'], int(data['data']) * self.altitude + 2000))
        polygon_points.append(first)

        # pol.outerboundaryis = [(18.333868,-34.038274, 1800), (18.370618,-34.034421,700),
        # (18.350616,-34.051677,1800),(18.333868,-34.038274,600),
        #                       (18.4,-34.038274, 1800), (18.5,-34.034421,700),
        #                       (18.43,-34.051677,1800), (18.51,-34.038274,600)]

        pol.outerboundaryis = polygon_points

        pol.altitudemode = simplekml.AltitudeMode.absolute
        pol.extrude = 5
        pol.style.polystyle.color = simplekml.Color.changealphaint(190, self.color)
        pol.style.linestyle.color = simplekml.Color.changealphaint(230, self.color)

        kml.save("" + self.kml_name + ".kml")

    def dome_generator(self):
        kml = simplekml.Kml(open=1)

        polygon_circle = []

        for data in self.data_set:
            # shape_domes = kml.newmultigeometry(name=data['data'])

            print int(data['data'])

            location = simplekml.Location(longitude=data['coordinates']['lng'], latitude=data['coordinates']['lat'],
                                          altitude=self.altitude)
            netlink = kml.newnetworklink(name=self.kml_name)
            netlink.link.href = self.getFileRoute(self.color, self.opacity)
            netlink.link.viewrefreshmode = simplekml.ViewRefreshMode.onregion

            value = self.multiplier * int(data['data'])
            s_scale = simplekml.Scale(x=value, y=value, z=value)

            dome = kml.newmodel(altitudemode=simplekml.AltitudeMode.clamptoground, link=netlink, location=location)
            dome.scale = s_scale

        kml.save("/tmp/kml/" + self.kml_name + ".kml")
        input_file = open("/tmp/kml/" + self.kml_name + ".kml", "r")
        output_file = open("kmls_management/static/" + self.kml_name + ".kml", "w")

        for line in input_file:
            if not 'NetworkLink' in line:
                output_file.write(line)

        input_file.close()
        output_file.close()

        os.system("rm /tmp/kml/" + self.kml_name + ".kml")

    def getFileRoute(self, color, opacity):

        if color == "Yellow":
            return "/dome/yellow_" + str(opacity) + "_opacity_dome.dae"
        if color == "Red":
            return "/dome/red_" + str(opacity) + "_opacity_dome.dae"
        if color == "Green":
            return "/dome/green_" + str(opacity) + "_opacity_dome.dae"
        if color == "Blue":
            return "/dome/blue_" + str(opacity) + "_opacity_dome.dae"

        print color

        return "/dome/yellow_" + opacity + "_opacity_dome.dae"

    def polycicle_generator(self):

        kml = simplekml.Kml(open=1)

        polygon_circle = []

        for data in self.data_set:

            shape_polycircle = kml.newmultigeometry(name=data['data'])

            print int(data['data'])

            polycircle = polycircles.Polycircle(latitude=data['coordinates']['lat'],
                                                longitude=data['coordinates']['lng'],
                                                radius=(int(data['data']) + 1) * self.multiplier,
                                                number_of_vertices=36
                                                )

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


    def cylinder_generator(self):


        kml = simplekml.Kml(open=1)

        polygon_circle = []

        for data in self.data_set:
            shape_polycircle = kml.newmultigeometry(name=data['data'])

            print int(data['data'])

            polycircle = polycircles.Polycircle(latitude=data['coordinates']['lat'],
                                                longitude=data['coordinates']['lng'],
                                                radius=10000,
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
            pol.style.polystyle.color = simplekml.Color.changealphaint(200, self.set_color(self.color))
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

        kml.save("kmls_management/static/" + self.kml_name + ".kml")


if __name__ == '__main__':
    kml = simplekml.Kml()

    pol = kml.newpolygon(name='A Polygon')
    pol.outerboundaryis = [(18.333868, -34.038274, 1800), (18.370618, -34.034421, 700),
                           (18.350616, -34.051677, 1800), (18.333868, -34.038274, 600),
                           (18.4, -34.038274, 1800), (18.5, -34.034421, 700),
                           (18.43, -34.051677, 1800), (18.51, -34.038274, 600)]

    pol.altitudemode = simplekml.AltitudeMode.absolute
    pol.extrude = 100
    pol.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.green)
    pol.style.linestyle.color = simplekml.Color.changealphaint(15, simplekml.Color.green)
    kml.save("kmls_management/static/Polygon Styling.kml")