import requests

url = "https://text-to-speach-api.p.rapidapi.com/supported-languages"

headers = {
	"X-RapidAPI-Key": "ebb0a6b275msh3d9a45cdfcd4585p1c7bd5jsnedebc1b3a195",
	"X-RapidAPI-Host": "text-to-speach-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())