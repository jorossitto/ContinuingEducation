import requests

page = 'http://facebook.com'

result = requests.get(page)

print(result.status_code)
