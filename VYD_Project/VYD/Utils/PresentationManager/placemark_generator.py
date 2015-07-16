__author__ = 'Marc'


class ParseManager(object):

    file = None

    def __init__(self, file_name, data_set, location_set, icon_url, look_at, line_width=2):
        self.file = open(file_name, 'w')

    def make_kml(self):

        self.file.write('<?xml version="1.0" encoding="UTF-8"?>')
        self.file.write('<kml xmlns="http://www.opengis.net/kml/2.2">')
        self.file.write('<Document>')
        self.file.write('<name>'+self.file_name+'</name>')
        self.file.write('<open>1</open>')
        self.file.write('<Style id="personalized_style">')
        self.file.write('<IconStyle>')
        self.file.write('<Icon>')
        self.file.write('<href>'+self.icon_url+'</href>')
        self.file.write('</Icon>')
        self.file.write('</IconStyle>')
        self.file.write('</Style>')
        self.file.write('<LineStyle>')
        self.file.write('<width>'+self.line_width+'</width>')
        self.file.write('</LineStyle>')
        self.file.write('</Style>')

        self.file.write('<Folder>')
        self.file.write('</Folder>')
        self.file.write('<name>Placemarks '+self.file_name+'</name>')
        self.file.write('<description>A set of placemarks of '+self.file_name+'</description>')

        self.file.write('<LookAt>')
        self.file.write('<longitude>'+self.look_at['longitude']+'</longitude>')
        self.file.write('<latitude>'+self.look_at['latitude']+'</latitude>')
        self.file.write('<altitude>'+self.look_at['altitude']+'</altitude>')
        self.file.write('<heading>'+self.look_at['heading']+'</heading>')
        self.file.write('<tilt>'+self.look_at['tilt']+'</tilt>')
        self.file.write('<range>'+self.look_at['range']+'</range>')
        self.file.write('</LookAt>')

        for counter, location in self.location_set:

            self.file.write('<Placemark>')
            self.file.write('<name>'+self.data_set[counter]+'</name>')
            self.file.write('<description>'+ self.data_set[counter]+' '+counter+'</description>')
            self.file.write('<styleUrl>#personalized_style</styleUrl>')
            self.file.write('<Point>')
            self.file.write('<altitudeMode>relativeToGround</altitudeMode>')
            self.file.write('<coordinates>'+self.location_set[counter]['lat']+','+self.location_set[counter]['lng']+'</coordinates>')
            self.file.write('</Point>')
            self.file.write('</Placemark>')

        self.file.write('</Folder>')
        self.file.write('</Document>')
        self.file.write('</kml>')


