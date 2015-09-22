# this code maps friends. i want to map ppl who tweet "#linog".
# i need to find the location data for users  who tweet using
# the tag linog

# there was anearthquake in the phillipines last night.
# i want to map out the location of the people talking about this
# earthquake. 

# this code is from the end of the slide chpater 14 in class. 
#CBCNewsfriends.py

from twitter_setup import api
#from pygeocoder import Geocoder
import pygmaps, time

mymap = pygmaps.maps(56.95, -98.31 , "10" )
uniqueid = 0 

for hit_loop in (0,100):
    try:
        results = api.search.tweets(q = "#NHLbracketchallenge" , count = 100 )
        num2 = len(results['statuses'])
        for u in range (0, num2):
            if ( (results['statuses'][u]['coordinates']) ) != None :
                if ( results['statuses'][u]['coordinates']['coordinates'][0] != 0.0):
                    uniqueid += 1 # note: its only counting valid coords found. needs to be fixed
            #coord is a list type
                    coord = results['statuses'][u]['coordinates']['coordinates']
                    print (coord)
                    num2 += 100
                    mymap.addpoint(coord[1],coord[0])
        print (results)
    except:
        continue
    

print ("total number of hits: ", num2 )
print ("total number of unique coord IDs found: ", uniqueid )

mymap.draw("mymap1.html")

import webbrowser as wb
wb.open_new_tab('mymap1.html')
