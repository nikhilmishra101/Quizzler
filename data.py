import requests

parameters = {
    "amount":10,
    "type":"boolean",
    "category":18,
}

url = "https://opentdb.com/api.php"
response = requests.get(url=url,params=parameters)
response.raise_for_status()

question_data = response.json()["results"]