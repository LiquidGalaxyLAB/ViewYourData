__author__ = 'Marc'

from pykml.factory import nsmap
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
from pykml.parser import Schema
from lxml import etree
import os

class MarkersTour(object):

    data_set = None
    range = 50000
    tilt = 70
    kml_name = None

    def __init__(self, data_set, kml_name, icon):
        self.data_set = data_set
        self.kml_name = kml_name
        self.icon = icon;

    def makeFile(self):


        # define a variable for the Google Extensions namespace URL string
        gxns = '{' + nsmap['gx'] + '}'

        stylename = "sn_shaded_dot"
        # start with a base KML tour and playlist
        tour_doc = KML.kml(
            KML.Document(
              GX.Tour(
                KML.name("Play me!"),
                GX.Playlist(),
              ),
              KML.Folder(
                KML.name('Features'),
                id='features',
              ),
              KML.Style(
                KML.IconStyle(
                    KML.scale(1.2),
                    KML.Icon(
                        KML.href(self.icon)
                    ),
                ),
                id=stylename,
               )
            )
        )
        for data in self.data_set:
            #import ipdb; ipdb.set_trace()
            # fly to a space viewpoint
            tour_doc.Document[gxns+"Tour"].Playlist.append(
              GX.FlyTo(
                GX.duration(5),
                GX.flyToMode("smooth"),
                KML.LookAt(
                  KML.longitude(float(data['coordinates']['lng'])),
                  KML.latitude(float(data['coordinates']['lat'])),
                  KML.altitude(0),
                  KML.heading(0),
                  KML.tilt(0),
                  KML.range(10000000.0),
                  KML.altitudeMode("relativeToGround"),
                )
              ),
            )
            # fly to the data
            tour_doc.Document[gxns+"Tour"].Playlist.append(
              GX.FlyTo(
                GX.duration(5),
                GX.flyToMode("bounce"),
                KML.LookAt(
                  KML.longitude(float(data['coordinates']['lng'])),
                  KML.latitude(float(data['coordinates']['lat'])),
                  KML.altitude(0),
                  KML.heading(0),
                  KML.tilt(data['data']),
                  KML.name(data['data']),
                  KML.range(self.range),
                  KML.altitudeMode("relativeToGround"),
                )
              ),
            )
            # spin around the data
            for aspect in range(0,360,10):
                tour_doc.Document[gxns+"Tour"].Playlist.append(
                  GX.FlyTo(
                    GX.duration(0.25),
                    GX.flyToMode("smooth"),
                    KML.LookAt(
                      KML.longitude(float(data['coordinates']['lng'])),
                      KML.latitude(float(data['coordinates']['lat'])),
                      KML.altitude(0),
                      KML.heading(aspect),
                      KML.tilt(data['data']),
                      KML.name(data['data']),
                      KML.range(self.range),
                      KML.altitudeMode("relativeToGround"),
                    )
                  )
                )
            tour_doc.Document[gxns+"Tour"].Playlist.append(GX.Wait(GX.duration(1.0)))

        #    tour_doc.Document[gxns+"Tour"].Playlist.append(
        #        GX.TourControl(GX.playMode("pause"))
        #    )

            # add a placemark for the data
            tour_doc.Document.Folder.append(
              KML.Placemark(
                KML.name("?"),
                KML.description(
                    "<h1>"+data['data']+"</h1>"
                ),
                KML.styleUrl('#{0}'.format(stylename)),
                KML.Point(
                  KML.extrude(1),
                  KML.altitudeMode("relativeToGround"),
                  KML.coordinates("{lon},{lat},{alt}".format(
                          lon=float(data['coordinates']['lng']),
                          lat=float(data['coordinates']['lat']),
                          alt=50,
                      )
                  )
                ),
                id=data['data'].replace(' ','_')
              )
            )
            # show the placemark balloon
            tour_doc.Document[gxns+"Tour"].Playlist.append(
                GX.AnimatedUpdate(
                  GX.duration(2.0),
                  KML.Update(
                    KML.targetHref(),
                    KML.Change(
                      KML.Placemark(
                        KML.visibility(1),
                        GX.balloonVisibility(1),
                        targetId=data['data'].replace(' ','_')
                      )
                    )
                  )
                )
            )

            tour_doc.Document[gxns+"Tour"].Playlist.append(GX.Wait(GX.duration(2.0)))

            tour_doc.Document[gxns+"Tour"].Playlist.append(
                GX.AnimatedUpdate(
                  GX.duration(2.0),
                  KML.Update(
                    KML.targetHref(),
                    KML.Change(
                      KML.Placemark(
                        GX.balloonVisibility(0),
                        targetId=data['data'].replace(' ','_')
                      )
                    )
                  )
                )
            )
            # fly to a space viewpoint
            tour_doc.Document[gxns+"Tour"].Playlist.append(
              GX.FlyTo(
                GX.duration(5),
                GX.flyToMode("bounce"),
                KML.LookAt(
                  KML.longitude(float(data['coordinates']['lng'])),
                  KML.latitude(float(data['coordinates']['lat'])),
                  KML.altitude(0),
                  KML.heading(0),
                  KML.tilt(0),
                  KML.range(10000000.0),
                  KML.altitudeMode("relativeToGround"),
                )
              ),
            )

        # check that the KML document is valid using the Google Extension XML Schema
        #assert(Schema("kml22gx.xsd").validate(tour_doc))

        #print etree.tostring(tour_doc, pretty_print=True)

        # output a KML file (named based on the Python script)
        outfile = file("kmls_management/static/"+self.kml_name,'w')
        outfile.write(etree.tostring(tour_doc, pretty_print=True))