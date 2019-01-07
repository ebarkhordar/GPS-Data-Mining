class TaxiData:
    def __init__(self, trip_id, call_type, origin_call, origin_stand, taxi_id, timestamp, day_type, missing_data,
                 polyline):
        self.trip_id = trip_id
        self.call_type = call_type
        self.origin_call = origin_call
        self.origin_stand = origin_stand
        self.taxi_id = taxi_id
        self.timestamp = timestamp
        self.day_type = day_type
        self.missing_data = missing_data
        self.polyline = polyline

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Location:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
