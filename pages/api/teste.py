import http.client

conn = http.client.HTTPSConnection("api.airtable.com")

headers = {
    'authorization': "Bearer keyejuwdVkKLST1H0",
    'cache-control': "no-cache",
    'postman-token': "a2f47588-1afc-66f6-8028-c0bfefbe43bd"
    }

conn.request("GET", "/v0/appkYesjT7j819rOp/Hospitais", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
