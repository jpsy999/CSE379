import csv
import time
import math
import base64
import numpy as np
from random import randint
import http.client
import pandas as pd
import urllib.request, urllib.parse, urllib.error

location_count = 1

def get_params():
    """ Function to retrieve and send parameters associated with geographical location. 
        Args:
            None
        Returns:
            Call to set_location function 
    """
    global location_count

    # Anchorage, AK
    if location_count == 1:
        location_count += 1
        print("Anchorage, AK is ")
        return set_location('true', 'en-us', '61.2181, 149.9003', 'latitudelongitude')
    # Mojave Desert, CA
    elif location_count == 2:
        location_count += 1
        print("Mojave Desert, CA is ")
        return set_location('true', 'en-us', '35.0110, 115.4734', 'latitudelongitude')
    # Jacksonville, FL
    elif location_count == 3:
        location_count += 1
        print("Jacksonville, FL is ")
        return set_location('true', 'en-us', '30.3322, 81.6557', 'latitudelongitude')
    # Honolulu, HI
    elif location_count == 4:
        location_count += 1
        print("Honolulu, HI is ")
        return set_location('true', 'en-us', '21.3069, 157.8583', 'latitudelongitude')
    # Ann Arbor, MI
    elif location_count == 5:
        location_count += 1
        print("Ann Arbor, MI is ")
        return set_location('true', 'en-us', '42.2808, 83.7430', 'latitudelongitude')
    # Bethlehem, PA
    elif location_count == 6:
        location_count += 1
        print("Bethlehem, PA is ")
        return set_location('true', 'en-us', '40.6259, 75.3705', 'latitudelongitude')
    # Seattle, WA
    elif location_count == 7:
        location_count += 1
        print("Seattle, WA is ")
        return set_location('true', 'en-us', '47.6062, 122.3321', 'latitudelongitude')
    # Bismarck, ND
    elif location_count == 8:
        location_count += 1
        print("Bismarck, ND is ")
        return set_location('true', 'en-us', '46.8083, 100.7837', 'latitudelongitude')
    # Rapid City, SD
    elif location_count == 9:
        location_count += 1
        print("Rapid City, SD is ")
        return set_location('true', 'en-us', '44.0805, 103.2310', 'latitudelongitude')
    # Mobile, AL
    elif location_count == 10:
        location_count = 1
        print("Mobile, AL is ")
        return set_location('true', 'en-us', '30.6954, 88.0399', 'latitudelongitude')


def set_location(verbose, culture, location, loc_type):
    """ Function to set and encode parameters associated with geographical location. 
        Args:
            verbose (bool) : EarthNetworks parameter - always true
            culture (String) : EarthNetworks parameter - specifies language to en-us
            location (String) : Latitutde and longitude coordinates
            loc_type (String) : EarthNetworks parameter - specifies input to be latitude and longitude
        Returns:
            (Dictionary) : urlencoded parameters for API call 
    """
    params = urllib.parse.urlencode({
        'verbose': verbose,
        'cultureInfo': culture,
        'location': location,
        'locationtype': loc_type,
    })
    return params


def validate(entry):
    """ Function to validate that dataframe entry is a number 
        Args:
            entry : value from dataframe being validated
        Returns:
            (String) : if entry is valid, returns it, else returns an empty string
    """
    if (entry != entry):
        return ""
    return entry


def categorize(event):
    """ Function to count the occurrences of keywords in the textual description of forecasts
        Args:
            event (Series) : detailedDescription from EarthNetworks API
        Returns:
            Call to find_greatest_value function
    """
    condition, severity, direction = "", "", ""
    sunny, rain, hail, thunder, snow, hurricane, spout, sandstorm = 0, 0, 0, 0, 0, 0, 0, 0
    precip_chance = ""
    int_precip_chance = 0

    for description in event:
        # print(description,'\n')
        if (len(description) == 5):
            weather = description[0].split(" ")
            index = description[3].split(" ")
        elif (len(description) == 6):
            weather = description[0].split(" ")
            index = description[4].split(" ")
            length = len(precip_chance)
            precip_chance = description[1][length-3:length-1]
            # print(precip_chance)
            if (precip_chance != ""):
                int_precip_chance = int(precip_chance)
        
        for word in weather:
            # print(word)
            if (word == "cloudy" or word == "sunny" or word == "clear" or word == '"Cloudy'):
                sunny += 1
            if (word == "rain"):
                rain += 1
            if (word == "hail"):
                hail += 1
            if (word == "thunderstorms" or word == "thunder" or word == "lightning" or word == "thunderstorm" or word == "storm"):
                thunder += 1
            if (word == "snow" or word == "blizzard" or word == "flurries" or word == "blizzards"):
                snow += 1
            if (word == "hurricane"):
                hurricane += 1
            if (word == "spout" or word == "waterspout" or word == "Waterspout"):
                spout += 1
            if (word == "sandstorm" or word == "Sandstorm"):
                sandstorm += 1
        for word in index: 
            if (word.isdigit()):
                severity = word
            direction = word
        
    return find_greatest_value(sunny, rain, hail, thunder, snow, hurricane, spout, sandstorm, int_precip_chance)


def find_greatest_value(sunny, rain, hail, thunder, snow, hurricane, spout, sandstorm, precip_chance):
    """ Function to determine that categorization of weather event based on the occurrence counts generated 
        by the categorize function. 
        Args: 
            sunny (int) : generated count of keywords relating to forecast of clear skies
            rain (int) : generated count of keywords relating to forecast of rain
            hail (int) : generated count of keywords relating to forecast of hail
            thunder (int) : generated count of keywords relating to forecast of thunderstorms
            snow (int) : generated count of keywords relating to forecast of snow
            hurricane (int) : generated count of keywords relating to forecast of hurricane
            spout (int) : generated count of keywords relating to forecast of waterspout
            sandstorm (int) : generated count of keywords relating to forecast of sandstorm
            precip_chance (int) : precipitation chance included in detailed description of forecast
        Returns:
            (string) : associated Minecraft command
    """
    max_weather = max(sunny, rain, hail, thunder, snow, hurricane)
    if (sandstorm > 1): 
        return "/weather2 storm create sandstorm"
    if (sunny == max_weather):
        if (precip_chance >= 30):
            if (hurricane > 1):
                return "/weather2 storm create f1"
            if (spout > 1): 
                return "/weather2 storm create spout"
            if (thunder > 1 and snow > 1):
                return "/weather thunder"
            if (snow > 1):
                return "/weather rain"
            return "/weather rain"
        return "/weather clear"
    if (rain == max_weather):
        return "/weather rain"
    if (hail == max_weather):
        return "/weather2 storm create hail"
    if (thunder == max_weather):
        return "/weather thunder"
    if (snow == max_weather):
        return "/weather rain"
    if (hurricane == max_weather):
        return "/weather2 storm create f1"
    if (spout == max_weather):
        return "/weather2 storm create spout"
    if (sandstorm == max_weather): 
        return "/weather2 storm create sandstorm"


if __name__ == "__main__":
    """ Main function to handle collection, parsing and cleaning of data gathered from EarthNetworks API 
        Call. 
    """

    # Enterprise Pro subscrition ID

    # Request headers
    headers = {
        # Need to add subscription key
        'Ocp-Apim-Subscription-Key': '',
    }
    
    starttime = time.time()

    while(True):
        try:
            conn = http.client.HTTPSConnection('earthnetworks.azure-api.net')
            conn.request("GET", "/data/forecasts/v1/daily?%s" % get_params(), "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        data_str = data.decode()

        # file = open("/Users/faithkomlo/Documents/Lehigh/Senior/forecast.csv", "w")
        # w = csv.writer(file)
        
        data_str = data_str.split(",")
        data_str = [item.replace('\r\n', '') for item in data_str]
        data_str = [item.replace('  ', '') for item in data_str]
        data_str = [item.replace('{', '') for item in data_str]
        data_str = [item.replace('}', '') for item in data_str]
        data_str = [item.replace('"dailyForecastPeriods":', '') for item in data_str]

        data_str = [category.split(':') for category in data_str]

        col = []
        row = []
        count = 0
        for entry in data_str:
            if (count < 16):
                col.append(entry[0])
            row.append(entry[1])
            count += 1

        chunks = [row[x:x+16] for x in range(0, len(row), 16)]

        df = pd.DataFrame()
        for chunk in chunks:
            df = df.append([chunk], ignore_index=True)
        df.columns = col
        df = df[:19]

        # df.to_csv("/Users/faithkomlo/Documents/Lehigh/Senior/data.csv") 
        event = df['"detailedDescription"']
        event = event.apply(validate)
        event = [info.split('.') for info in event]

        categorized_event = categorize(event);
        print(categorized_event)
        text_file = open("categorized_event.txt", "w")
        text_file.write(categorized_event)
        text_file.close()

        time.sleep(60.0 - ((time.time() - starttime) % 60))
