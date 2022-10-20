import requests

url = "https://khalti.com/api/v2/payment/status/"
params = {
  "token": "629A2MNdkYnpzPv8TqsPqj",
  "amount": 1000
}
headers = {
  "Authorization": "Key test_secret_key_4e85bb4e70114300844afa1e59abfb00"
}

response = requests.get(url, params, headers = headers)

print(response.text)