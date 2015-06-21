__author__ = 'hellfish90'

import wget

import os

class DownloadDataSetManager(object):

    global dump
    file_type = None
    file_name = None
    tmp_path = "/tmp/VYD/data_set/"
    extList = ["xml", "json", "csv", "gtfs", "xls", "xlsx"]
    bar_thermometer = 0

    def __init__(self, url):
        self.url = url

    def get_type(self):
        return self.file_type

    def get_file_name(self):
        return self.file_name

    def get_file_path(self):
        return self.tmp_path + self.file_name

    def download_file(self):
        self.download_wget()

    def download(self):
        self.__clean_temp_files()
        wget.download(self.url, out=self.tmp_path, bar=self.bar_thermometer)
        self.file_name = os.listdir(self.tmp_path)[0]
        self.file_type = self.__get_file_type()
        print self.file_name
    def __get_file_type(self):

        split_name = self.file_name.split(".")
        ext = split_name[len(split_name)-1]

        if ext in self.extList:
            return ext
        else:
            return None

    def __clean_temp_files(self):
        for file in os.listdir(self.tmp_path):
            os.remove(self.tmp_path+file)

if __name__ == '__main__':

    fi = DownloadDataSetManager("http://mappe.regione.toscana.it/db-webgis/paas/example.jsp?format=xml")
    fi.download()
    print "________________"
    print fi.get_file_name()
    print fi.get_file_path()
    print fi.get_type()