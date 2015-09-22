
# twitter_trending.py
from twitter_setup import api

# "WOE": yahoos where on earth id
cebu_id = 2346740 #1199079

q = api.search.trends.place( _id = 1 )[0]
print(can_trends)

results = api.search.tweets(q = '#linog', count = 100)
for tweet in results['statuses']:
    print ("\n" , tweet)


#using geocoder
from pygeocoder import Geocoder
address = Geocoder.geocode("")
#print (address.formal_address)

import pygmaps
coord = address.cordinates
mymap = pygmaps.maps(coord[0], coord[1], '16' )
mymap.addpoint(coord[0] , coord[1] , '#0000ff' )
mymap.draw('mymap.html')

import webbrowser as wb
wb.open_new_tab('mymap.html')
