from VYD_Project.VYD.Utils import ParseManager
from VYD_Project.VYD.Utils.ParseManager.Exception import NoParserImplemented

__author__ = 'hellfish90'


import unittest


class TestFileManager(unittest.TestCase):

    url = [
        ["biblioteche.csv",
         "csv",
         [u'id', u'est', u'nord', u'denominazione', u'indirizzo', u'comune', u'provincia', u'id_rete_biblio', u'cod_rete_biblio', u'desc_rete_biblio'],
         "http://mappe.regione.toscana.it/db-webgis/biblio/example_postgis.jsp?format=csv"],

        ["FiereCongressiOrganizzati.csv",
         "csv",
         [u'anno', u'fiere_organizzate', u'congressi_organizzati', u'totale_eventi_organizzati'],
         "http://opendata.comune.fi.it//materiali/cultura_turismo/FiereCongressiOrganizzati.csv"],

        ["Festivals.csv",
         "csv",
         [u'Trcid', u'Title', u'Shortdescription', u'Longdescription', u'Calendarsummary', u'TitleEN', u'ShortdescriptionEN', u'LongdescriptionEN', u'CalendarsummaryEN', u'Types', u'Ids', u'Locatienaam', u'City', u'Adres', u'Zipcode', u'Latitude', u'Longitude', u'Urls', u'Media', u'Thumbnail', u'Datepattern_startdate', u'Datepattern_enddate', u'Singledates', u'Type1', u'Lastupdated', u''],
         "http://www.amsterdamopendata.nl/files/Festivals.csv"],

        ["eventi.json",
         "json",
         [],
         "http://wwwext.comune.fi.it/opendata/files/eventi.json"],

        ["wifiopenbaar.json",
         "json",
         [],
         "https://data.lab.fiware.org/vi/dataset/399d5818-2d02-42af-845b-fb6e1749151d/resource/f06376ac-a5f2-456f-8a26-56e1da5d5b2b/download/wifiopenbaar.json"],

        ["index.xml",
         "xml",
         [],
         "http://www301.regione.toscana.it/bancadati/farmacie/index.xml"],

        ["paas.xml",
         "xml",
         [],
         "http://mappe.regione.toscana.it/db-webgis/paas/example.jsp?format=xml"],

        ["Prezzari.xml",
         "xml",
         [],
         "http://www301.regione.toscana.it/bancadati/PrezzarioLavoriPubblici/Prezzari.xml"],

        ["fiwareaccelerators20150610.xlsx",
         "xlsx",
         [],
         "https://data.lab.fiware.org/vi/dataset/7e0dfb28-cfa2-453b-b624-c5bb6bedd010/resource/53cefac5-3590-4e95-8358-43c8882c3add/download/fiwareaccelerators20150610.xlsx"],

        ["edificiosmunicipales.xls",
         "xls",
         [],
         "http://datosabiertos.malaga.eu/dataset/52f114a6-a7f3-4f5e-bc7e-ca6a6bc72e0c/resource/d20c4c69-f197-4b57-b849-ee496509dcde/download/edificiosmunicipales.xls"],

        ["forze-lavoro-nel-comune-di-firenze-occupati-per-titolo-di-studio-e-per-quartiere-anno-2013.xls",
         "xls",
         [],
         "http://ckan.comune.fi.it/storage/f/2014-12-03T10%3A04%3A58.332Z/forze-lavoro-nel-comune-di-firenze-occupati-per-titolo-di-studio-e-per-quartiere-anno-2013.xls"],

    ]

    def test_get_header(self):

        headers = []
        test_headers = []

        for data in self.url:
            headers.append(data[2])
            parse_manager = ParseManager(data[3])
            try:
                parse_manager.parse()
                test_headers.append(parse_manager.get_header())
            except NoParserImplemented:
                test_headers.append([])

        self.assertEqual(headers, test_headers)

    def test_get_data_by_location(self):
        pass

    def test_get_data_by_coordinates(self):
        pass



if __name__ == '__main__':
    unittest.main()