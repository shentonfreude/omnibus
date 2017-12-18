from google.transit import gtfs_realtime_pb2
import urllib

ART = 'http://realtime.commuterpage.com/rtt/public/utility/gtfsrealtime.aspx/tripupdate'
feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen(ART)
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print entity.trip_update
