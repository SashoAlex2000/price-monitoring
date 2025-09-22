import requests

print('Helloooo!')

response: requests.Response = requests.get('https://quotes.toscrape.com/')

print(response)
print(type(response))
print(response.status_code)
print(response.content)

