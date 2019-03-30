# Zomato-Scraper
Web scraping in Python with Beautiful Soup



**Zomato_API**:

API endpoint provided by Zomato has been used to get details about restaurants in Bangalore. You can get the details of up to 100 restaurants using this endpoint. The details obtained:
* Restaurant ID
* Restaurant Name
* Locality
* Cuisines
* Average cost for two
* Rating
* Votes
This data is stored in a *csv* file. the API Key required for making the call can be obtained [here](https://developers.zomato.com/api). Up to 1000 API calls can be made per day using this key.




**Restaurants_BS4**:

Beautiful Soup has been used to scrape data from [Zomato](https://www.zomato.com/bangalore/restaurants). The data obtained is stored in a *csv* file.
* Restaurant Name
* Locality
* Cuisine
* Rating
* Cost for two
* Votes




**Reviews_BS4**:

Beautiful Soup has been used to scrape the popular top 10 reviews of each restaurant in Bangalore. The data obtained is stored in a *csv* file.
* Restaurant Name
* Customer Name
* Customer Rating
