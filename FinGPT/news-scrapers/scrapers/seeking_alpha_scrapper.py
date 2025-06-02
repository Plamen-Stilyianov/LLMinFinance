import http.client

conn = http.client.HTTPSConnection("seeking-alpha.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "4a161bd443msh5c25c1725a5d493p1f40a1jsn677a2f136b03",
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com"
}

conn.request("GET", "/market/get-earnings-calendar?with_rating=false&currency=USD", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))