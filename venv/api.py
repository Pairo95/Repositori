import requests

dades = {"nom": "Ada", "punts": 85}
resposta = requests.post("https://httpbin.org/post", json=dades)
resposta_json = resposta.json()
print("Dades rebudes pel servidor:", resposta_json["json"])
