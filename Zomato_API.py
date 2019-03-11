import requests
import csv

with open("output_restaurant.csv", "a", newline='') as fp:
    wr = csv.writer(fp, dialect='excel')
    url = "https://developers.zomato.com/api/v2.1/search?entity_id=4&entity_type=city&q=Bangalore&start=80"
    header = {"Accept": "application/json", "user-key": "API_KEY", "User-agent": "curl/7.43.0"}
    resp = requests.get(url, headers=header).json()
    for i in range(0, 20):
        rest = resp['restaurants'][i]
        res_id = rest['restaurant']['id']
        name = rest['restaurant']['name']
        locality = rest['restaurant']['location']['locality']
        cuisines = rest['restaurant']['cuisines']
        average_cost_for_two = rest['restaurant']['average_cost_for_two']
        rating = rest['restaurant']['user_rating']['aggregate_rating']
        votes = rest['restaurant']['user_rating']['votes']
        list_ = [res_id, name, locality, cuisines, average_cost_for_two, rating, votes]
        wr.writerow(list_)
