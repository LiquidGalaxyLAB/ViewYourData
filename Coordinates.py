from time import sleep

__author__ = 'hellfish90'
import requests


def get_coordinates_by_location(location_data):

    query = ''

    if len(location_data) > 1:
        for data in location_data:
            query += data + '+'
    else:
        query = location_data[0]

    #print "query:" + query

    url = 'http://maps.google.com/maps/api/geocode/json?address='+query+'&sensor=false'

    r = requests.get(url)
    #print r.status_code
    #print r.encoding
    #print r.text

    json = r.json()

    if json["status"] == 'OK':
        lat = json["results"][0]["geometry"]["location"]["lat"]
        lng = json["results"][0]["geometry"]["location"]["lng"]

        if correct_coordinates(lat, lng):

            coordinates = {'lat': lat, 'lng': lng}
            #sleep(0.1)
            return coordinates
        else:
            return None
    else:
        #print json["status"]
        return None


def correct_coordinates(lat, lng):
    return is_number(lat) and is_number(lng)


def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False

    return True