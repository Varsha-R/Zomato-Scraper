import requests
from bs4 import BeautifulSoup
import re
import pandas
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
page_no = 1
restaurant_reviews =[]

for page in range(0, 813):
    print(page_no)
    response = requests.get("https://www.zomato.com/bangalore/restaurants?page={0}".format(page_no), headers=headers)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    search_list = soup.find_all("div", {'id': 'orig-search-list'})
    list_content = search_list[0].find_all("div", {'class': 'content'})
    for i in range(0,15):
        res_name = list_content[i].find("a", {'data-result-type': 'ResCard_Name'})
        ratings = list_content[i].find("div", {'data-variation': 'mini inverted'})
        if ratings is None:
            continue
        res_url = res_name.get('href')
        response_url = requests.get(res_url, headers=headers)
        content_url = response_url.content
        soup_url = BeautifulSoup(content_url, "html.parser")
        merch_name = soup_url.find_all("div", {'class': 'header nowrap ui left'})
        merch_ratings = soup_url.find_all("div", {'class': re.compile(r'ttupper fs12px left bold zdhl2 tooltip*')})
        try:
            popular = soup_url.find_all("a", {'data-sort': 'reviews-top'})
            num_reviews = int(popular[0].find('span').string)
        except:
            continue
        if(num_reviews > 10):
            for j in range(0, 10):
                name = merch_name[j].find('a')
                ratings = merch_ratings[j].get('aria-label').split()[1]
                dataframe ={}
                dataframe["rest_name"] = res_name.string.replace('\n', ' ')
                dataframe["cust_name"] = name.string.replace('\n', ' ')
                dataframe["cust_rating"] = ratings
                restaurant_reviews.append(dataframe)
        else:
            for j in range(0, num_reviews):
                name = merch_name[j].find('a')
                ratings = merch_ratings[j].get('aria-label').split()[1]
                dataframe ={}
                dataframe["rest_name"] = res_name.string.replace('\n', ' ')
                dataframe["cust_name"] = name.string.replace('\n', ' ')
                dataframe["cust_rating"] = ratings
                restaurant_reviews.append(dataframe)
    page_no+=1
    
df = pandas.DataFrame(restaurant_reviews)
df.to_csv("zomato_reviews.csv", index=False)
