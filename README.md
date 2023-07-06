# Yahoo Sports News Tracker using Beautiful Soup
Allows the BeatifulSoup script to scrape all the recent data based on sports events and results from Yahoo and store it inside the memory as a dataset. 
 
<div align="center">
    <img width="70%%" src="img/yahoosports.jpg" alt="yahoo.jpg" >
</div>

## Project Organization
---------------------------------------------------------

    ├── LICENSE          <- MIT License
    ├── README.md        <- The top-level README for developers using this project.
    ├── scraping_data
    │   ├── yahoo_news.csv              <- Data in csv format compatible with pandas dataframe.
    │   └── yahoo_news.json            <- Data in Json format for better utilization.
    │
    ├── img                 <- Contains project image files.
    │   
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         			generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── yahoo_news.py    <- Primary script for parsing and scraping data.
    │
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

## Methods and Modules Required:
* Python 3.11 
* BeautifulSoup4 4.12.2
* pandas 2.0.0
* requests

## Installation (using pip)
In order to *install* bs4 on the local machine, follow these steps:
1. Open pip and type:
```
> pip install beautifulsoup4                                                  
```
2. To install the Pandas Library, type:
```
> pip install pandas                                                          
```

## Future Plans:
Future plans include scraping the entire field of sports news feed of Yahoo and storing it in separate dataframes for a better user conveniences. 
