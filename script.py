import os

import requests
import json
from dotenv import load_dotenv

def get_real_random(nums, min, max, col,):
    url = 'https://www.random.org/integers/?num={0}&min={1}&max={2}&col={3}&base=10&format=plain&rnd=new'.format(nums, min, max, col)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(e)
        return None

def get_random_from_gaussian_distribution(n, mean, standard_deviation, significant_digits):

    try:
        load_dotenv(".env")
        data = {
            "jsonrpc": "2.0",
            "method": "generateGaussians",
            "params": {
                "apiKey": os.getenv("API_KEY"),
                "n": n,
                "mean": mean,
                "standardDeviation": standard_deviation,
                "significantDigits": significant_digits,
            },
            "id": 0
        }
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(data)
        response = requests.post('https://api.random.org/json-rpc/4/invoke', json=data, headers=headers)

        if response.status_code == 200:
            print(response.json()["result"]["random"]["data"])
        else:
            print(response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print(e)
        return None

def main():

#   nums, min, max, col = input("Enter the number of random numbers, minimum, maximum, and columns separated by commas: ").split(',')

#    posts = get_real_random(nums, min, max, col)
#    if posts:
#        print(posts)#.replace("\n", "\t"))
#    else:
#        print('Failed to get posts')

    get_random_from_gaussian_distribution(
        input("Enter the number of random numbers: "),
        input("Mean: "),
        input("Standard deviation: "),
        input("and the number of Significant digits: "))

if __name__ == '__main__':
    main()