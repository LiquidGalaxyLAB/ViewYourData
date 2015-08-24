__author__ = 'hellfish90'

import unittest

from VYD_Project.VYD.Utils.ParseManager.download.downloadmanager import DownloadDataSetManager


class TestFileManager(unittest.TestCase):
    url = [
        ["biblioteche.csv", "csv", "http://mappe.regione.toscana.it/db-webgis/biblio/example_postgis.jsp?format=csv"],
        ["FiereCongressiOrganizzati.csv", "csv",
         "http://opendata.comune.fi.it//materiali/cultura_turismo/FiereCongressiOrganizzati.csv"],
        ["Festivals.csv", "csv", "http://www.amsterdamopendata.nl/files/Festivals.csv"],
        ["eventi.json", "json", "http://wwwext.comune.fi.it/opendata/files/eventi.json"],
        ["wifiopenbaar.json", "json",
         "https://data.lab.fiware.org/vi/dataset/399d5818-2d02-42af-845b-fb6e1749151d/resource/f06376ac-a5f2-456f-8a26-56e1da5d5b2b/download/wifiopenbaar.json"],
        ["index.xml", "xml", "http://www301.regione.toscana.it/bancadati/farmacie/index.xml"],
        ["paas.xml", "xml", "http://mappe.regione.toscana.it/db-webgis/paas/example.jsp?format=xml"],
        ["Prezzari.xml", "xml", "http://www301.regione.toscana.it/bancadati/PrezzarioLavoriPubblici/Prezzari.xml"],
        ["fiwareaccelerators20150610.xlsx", "xlsx",
         "https://data.lab.fiware.org/vi/dataset/7e0dfb28-cfa2-453b-b624-c5bb6bedd010/resource/53cefac5-3590-4e95-8358-43c8882c3add/download/fiwareaccelerators20150610.xlsx"],
        ["edificiosmunicipales.xls", "xls",
         "http://datosabiertos.malaga.eu/dataset/52f114a6-a7f3-4f5e-bc7e-ca6a6bc72e0c/resource/d20c4c69-f197-4b57-b849-ee496509dcde/download/edificiosmunicipales.xls"],
        ["forze-lavoro-nel-comune-di-firenze-occupati-per-titolo-di-studio-e-per-quartiere-anno-2013.xls", "xls",
         "http://ckan.comune.fi.it/storage/f/2014-12-03T10%3A04%3A58.332Z/forze-lavoro-nel-comune-di-firenze-occupati-per-titolo-di-studio-e-per-quartiere-anno-2013.xls"],
    ]

    def test_file_formats(self):

        formats = []
        test_formats = []

        for data in self.url:
            formats.append(data[1])
            fileMng = DownloadDataSetManager()
            fileMng.set_url(data[2])
            fileMng.download()
            test_formats.append(fileMng.get_type())

        self.assertEqual(formats, test_formats)

    def test_file_name(self):

        names = []
        test_names = []

        for data in self.url:
            names.append(data[0])
            fileMng = DownloadDataSetManager()
            fileMng.set_url(data[2])
            fileMng.download()
            test_names.append(fileMng.get_file_name())

        self.assertEqual(names, test_names)

    def test_file_path(self):

        names = []
        test_names = []

        for data in self.url:
            names.append("/tmp/VYD/data_set/" + data[0])
            fileMng = DownloadDataSetManager()
            fileMng.set_url(data[2])
            fileMng.download()
            test_names.append(fileMng.get_file_path())

        self.assertEqual(names, test_names)


if __name__ == '__main__':
    unittest.main()


