__author__ = 'Marc'

import simplekml
import os


class DomeGenerator(object):
    def __init__(self, data_set, kml_name, color, altitude, multiplier, opacity=None):
        self.data_set = data_set
        self.kml_name = kml_name
        self.color = color
        self.altitude = altitude
        self.multiplier = multiplier
        self.opacity = opacity

    def generate(self):
        kml = simplekml.Kml(open=1)

        for data in self.data_set:
            print round(data['data'])

            location = simplekml.Location(longitude=data['coordinates']['lng'], latitude=data['coordinates']['lat'],
                                          altitude=self.altitude)
            netlink = kml.newnetworklink(name=self.kml_name)
            netlink.link.href = self.getFileRoute(self.color, self.opacity)
            netlink.link.viewrefreshmode = simplekml.ViewRefreshMode.onregion

            value = self.multiplier * round(data['data'])
            s_scale = simplekml.Scale(x=value, y=value, z=value)

            dome = kml.newmodel(altitudemode=simplekml.AltitudeMode.clamptoground, link=netlink, location=location)
            dome.scale = s_scale

        kml.save("/tmp/kml/" + self.kml_name + ".kml")
        input_file = open("/tmp/kml/" + self.kml_name + ".kml", "r")
        output_file = open("kmls_management/static/" + self.kml_name, "w")

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