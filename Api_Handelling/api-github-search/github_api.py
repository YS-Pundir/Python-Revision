import requests

params={
    "q":"Python",
    "sort":"stars",
    "order":"desc",
    "per_page":5
}

url="https://api.github.com/search/repositories"
response=requests.get(url,params=params)

if response.status_code==200:
    data=response.json()

    for dict in data["items"]:
        print(f"Full Name : {dict["full_name"]} \nTotal Stars : {dict["stargazers_count"]}")
        print("-"*60)