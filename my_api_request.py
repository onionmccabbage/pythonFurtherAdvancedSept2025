# we need the requests library
# NB you may need to pip install requests
import requests

# make requests
def req():
    '''make a call to an external API'''
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json() # this particular API returns JSON
    return users[5]['name']

u = req()
print(u)

