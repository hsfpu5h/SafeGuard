def determine_required_apis(city=None, state=None, country=None):
    required_apis = []
    if city or state or country:
        required_apis.append("weather_api")
        required_apis.append("news_api")
        required_apis.append("tagesschau_api")
        required_apis.append("neo_api")
        required_apis.append("iqair_api")
        required_apis.append("global_disaster_api")
        required_apis.append("earthquake_api")
    return required_apis
