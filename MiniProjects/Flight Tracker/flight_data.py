class FlightData:
    def __init__(self, price, origin, destination, out_date, return_date, stops):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def get_cheapest_flight(data):

    if data is None or not data['data']:
        return FlightData(None, None, None, None, None, stops=None)

    flight_data = [x for x in data['data']]
    nr_stops = len(flight_data[0]['itineraries'][0]['segments']) - 1
    cheapest_flight = FlightData(price=flight_data[0]['price']['grandTotal'],
                                         origin=flight_data[0]['itineraries'][0]['segments'][0]['departure']['iataCode'],
                                         stops = nr_stops,
                                         destination=flight_data[0]['itineraries'][0]['segments'][nr_stops]['arrival']['iataCode'],
                                         out_date=flight_data[0]['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0],
                                         return_date=flight_data[0]['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0])
    for item in flight_data:
        if item['price']['grandTotal'] < cheapest_flight.price:
            cheapest_flight = FlightData(price=item['price']['grandTotal'],
                                         origin=item['itineraries'][0]['segments'][0]['departure']['iataCode'],
                                         stops=nr_stops,
                                         destination=item['itineraries'][0]['segments'][0]['arrival']['iataCode'],
                                         out_date=item['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0],
                                         return_date=item['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0])

    return cheapest_flight