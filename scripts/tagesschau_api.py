from get_data_func import get_data

def get_german_news():
    api_url = "https://www.tagesschau.de/api2u/homepage/"
    news_data = get_data(api_url)

    if news_data:
        return news_data
    else:
        print("No data retrieved")

#print(get_german_news())