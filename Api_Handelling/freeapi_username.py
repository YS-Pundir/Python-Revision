import requests
def fetch_random_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    object=response.json()

    if object ["success"] and "data" in object:
        user_data=object["data"]
        user_name=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return user_name,country
    else :
        raise Exception("Failed to fetch user data")
def main():
    try:
        username,address=fetch_random_user_freeapi()
        print(f"User Name {username} , address {address}")
    except Exception as e :
        print(str(e))
if __name__=="__main__":
    main()

    