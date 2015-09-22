#cebu trends. created march 30 2015 by nikki sigurdson
#works with twitter
# fyi Cebu is a city in the Phillipines
from twitter_setup import api
cebu_id =23424934
cebutrends = api.trends.place( _id = "Canada")[0]

myx = api.uriparts
num = len(cebutrends['trends'])
print(cebutrends['trends'])
#print(len(cebutrends) , (num))
for dictionary in cebutrends['locations']:
   # print (type(cebutrends), type(dictionary))
   None

