import requests

response = requests.get("https://www.screamingfrog.co.uk/")

print(len(response.text))