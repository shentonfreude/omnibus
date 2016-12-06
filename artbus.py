from __future__ import print_function
from datetime import datetime
import urllib

from google.transit import gtfs_realtime_pb2
# import gtfs  # ERROR reading gtfs: 'ascii' codec can't encode character u'\ufeff' in position 0: ordinal not in range(128)
import pygtfs

# gtfs2db overwrite ./google_transit.zip artbus.sqlite

ROUTES = './google_transit.zip'
REALTIME = 'http://realtime.commuterpage.com/rtt/public/utility/gtfsrealtime.aspx/tripupdate'

# pygtfs is DB backed which we don't want, but it works
# sched has:
# 'agencies',
# 'agencies_by_id',
# 'db_connection',
# 'db_filename',
# 'drop_feed',
# 'engine',
# 'fare_rules',
# 'fares',
# 'fares_by_id',
# 'feed_infos',
# 'feeds',
# 'feeds_by_id',
# 'frequencies',
# 'routes',
# 'routes_by_id',
# 'service_exceptions',
# 'service_exceptions_by_id',
# 'services',
# 'services_by_id',
# 'session',
# 'shapes',
# 'stop_times',
# 'stops',
# 'stops_by_id',
# 'transfers',
# 'translations',
# 'trips',
# 'trips_by_id']

# Routes

# sched = pygtfs.Schedule(':memory:')
# pygtfs.append_feed(sched, '/Users/chris/Downloads/google_transit.zip')
sched = pygtfs.Schedule('artbus.sqlite')

# >>> sched.agencies
# [<Agency 1: Arlington Transit>]
# >>> sched.stops
# # Long list like <Stop 83: Ballston Metro G, Fairfax Dr, EB @ N Stafford, NS>,
# >>> sched.routes
# [<Route 41: 41>, <Route 42: 42>, ... <Route 92: 92>]
# >>> sched.routes_by_id('55')
# [<Route 55: 55>]
# Stops like: <Stop 98: N George Mason Drive, SB @ Patrick Henry Drive, NS>,

# r52 = sched.routes_by_id('52')[0] = [<Trip 4371>, ...]


# Realtime entity like:
# trip {
#   trip_id: "4371"
# }
# stop_time_update {
#   stop_sequence: 4
#   departure {
#     time: 1480977581
#   }
# }
# stop_time_update {
#   stop_sequence: 5
#   arrival {
#     time: 1480977606
#   }
# }

# https://developers.google.com/transit/images/gtfs-feed-diagram.png

# t.trip_headsign = u'East Falls Church Metro'
# t.stop_times[4].stop_id = '114'
# sched.stops_by_id('114')[0] = <Stop 114: Washington Blvd, WB @ N Utah Street, NS>
# sched.stops_by_id('115')[0] = <Stop 115: Washington Blvd, WB @ N Vermont Street, NS>

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen(REALTIME)
feed.ParseFromString(response.read())
for entity in feed.entity:
    if entity.HasField('trip_update'):
        #print(entity.trip_update)
        trip_id = entity.trip_update.trip.trip_id  # 4371
        trip = sched.trips_by_id(trip_id)[0]
        stop_times = trip.stop_times
        route_id = sched.trips_by_id('4364')[0].route.route_id

        update = entity.trip_update.stop_time_update
        # should just use comprehension
        for event in update:
            arrival_time = datetime.fromtimestamp(event.departure.time).ctime()
            departure_time = datetime.fromtimestamp(event.departure.time).ctime()
            stop_sequence = event.stop_sequence
            stop_id = stop_times[stop_sequence].stop_id  # off by one? 1- or 0-based?
            stop_name = sched.stops_by_id(stop_id)[0]
            print('route={} arr={} dep={} name={}'.format(route_id, arrival_time, departure_time, stop_name))
