import csv
import json
from datetime import datetime
import random
import string


# Open the .dat file
with open('navaids.dat', newline='') as datfile:
    # Skip the header row
    next(datfile)
    # Read the .dat file contents
    data = csv.reader(datfile, delimiter=';')
    # Create WP list
    wpl = []
    # Iterate through each row in the .dat file
    i = 0
    for row in data:
        # Dictionary for each WP
        wpe = {}
        # Extract WP data from each list item
        lat = row[1]
        long = row[2]
        wp_name = row[3]
        # Set key value pairs within dictionary
        wpe["number"] = i+1
        wpe["elevation"] = 0
        wpe["name"] = wp_name
        wpe["wp_type"] = "WP"
        wpe["latitude"] = lat
        wpe["longitude"] = long
        # Append the WP dictionary to the WP list
        wpl.append(wpe)

        i+=1

    # Dictionary for the top level key value pairs that we will export as json
    wp_json = {}
    # Creating the 3 key value pairs at the top level and appending the WP list
    wp_json["waypoints"] = wpl
    wp_json["name"] = "cf2wpe-{0}-{1}".format(datetime.today().strftime('%Y%m%d'), ''.join(random.choice(string.ascii_lowercase) for i in range(4)))
    wp_json["aircraft"] = "harrier"

    # Serializing json  
    with open(wp_json["name"] + ".json", "w") as outfile:
        json.dump(wp_json, outfile)
