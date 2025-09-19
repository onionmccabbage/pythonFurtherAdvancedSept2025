# a service to access https://swapi.info/api
import requests

class SwapiService():
    def __init__(self):
        pass
    def getSwapi(category, id):
        url = f"https://swapi.info/api/{category}/{id}"
        print(url)
        response = requests.get(url)
        return response.json()

if __name__ == "__main__":
    swapi = SwapiService()
    p = swapi.getSwapi('people', 1)
    print(p)