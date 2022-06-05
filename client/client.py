import http.client

conn = http.client.HTTPSConnection("localhost", 8081)
payload = "{\r\n\t\"ime\": \"Luka\",\r\n\t\"prezime\": \"Isailovic\",\r\n\t\"smer\": \"rm\",\r\n\t\"predmeti\": [\r\n\t\t{\r\n\t\t\t\"ime\": \"pds\",\r\n\t\t\t\"espb\": 5\r\n\t\t}\r\n\t]\r\n}"
headers = {}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))