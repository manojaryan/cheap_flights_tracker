import requests
from datetime import datetime, timedelta

# Define your search parameters
origin = "DFW"  # Your departure airport code
destination = "BLR"  # Your destination airport code
departure_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")  # Departure date 2 weeks from now
return_date = (datetime.now() + timedelta(days=21)).strftime("%Y-%m-%d")  # Return date 3 weeks from now

# Make the request to the API
url = f"https://api.skypicker.com/flights?flyFrom={origin}&to={destination}&dateFrom={departure_date}&dateTo={return_date}"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the response is not OK
    flights = response.json()["data"]
    # Find the cheapest flight
    cheapest_flight = sorted(flights, key=lambda x: x["price"])[0]
    # Print the details of the cheapest flight
    print(f"The cheapest flight from {origin} to {destination} is ${cheapest_flight['price']} on {cheapest_flight['route'][0]['local_departure']} with {cheapest_flight['route'][0]['airline']}.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching flight information: {e}")
