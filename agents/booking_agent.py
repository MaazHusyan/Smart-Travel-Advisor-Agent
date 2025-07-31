from tools.mock_tools import get_flights, suggest_hotels

def get_booking_info(destination):
    flights = get_flights(destination)
    hotels = suggest_hotels(destination)

    return f"""{flights}{hotels}
"""