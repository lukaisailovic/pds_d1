import requests
from requests.structures import CaseInsensitiveDict
import os

url = os.getenv("SERVER_URL","http://localhost:8081/users")

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
	"ime": "Luka",
	"prezime": "Isailovic",
	"smer": "rm",
	"predmeti": [
		{
			"ime": "pds",
			"espb": 5
		}
	]
}
"""

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)