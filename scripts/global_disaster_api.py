from gdacs.api import GDACSAPIReader

def get_disaster_data():
    client = GDACSAPIReader()

    events = client.latest_events()

    if events:
        return events
    else:
        print("No data available")