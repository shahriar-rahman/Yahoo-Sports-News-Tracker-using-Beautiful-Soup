import requests
from bs4 import BeautifulSoup
import pandas as pd


class YahooNews:
    def __init__(self):
        # Get Request
        url = 'https://sports.yahoo.com/'
        req = requests.get(url)
        self.soup = BeautifulSoup(req.text, 'lxml')

        # Initialize Data frame
        self.data_frame = pd.DataFrame(columns=['Header', 'Link'])

    def get_data(self):
        # Extract the first batch of data through inspection
        selector = self.soup.findAll('li', attrs={'class': 'js-stream-content'})

        for header in selector:
            print(header.text)
            print(header.find('a')['href'])
            link = header.find('a')['href']
            header = header.text

            # Store inside the initialized Data Frame
            self.data_frame = self.data_frame._append({'Header': header, 'Link': link}, ignore_index=True)

        print(self.data_frame)
        self.store()

    # Store in dataframe
    def store(self):
        try:
            self.data_frame.to_csv('../data/yahoo_news.csv', sep=',')
            self.data_frame.to_json('../data/yahoo_news.json')

        except Exception as exc:
            print("! ", exc)

        else:
            print("Save Successful!")


if __name__ == "__main__":
    web = YahooNews()
    web.get_data()
