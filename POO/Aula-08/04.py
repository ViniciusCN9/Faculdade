from PIL import Image
from io import BytesIO
import json
import requests

CHAVE_API = "563492ad6f91700001000001499e224f3c9742939dcf077b378025d8"
URL = "https://api.pexels.com/v1/search"

opcao = input("Search: ")

headers = {"Authorization": CHAVE_API}
response = requests.get(f"{URL}?query={opcao}&per_page=1", headers=headers)
response = json.loads(response.content)

if not response['total_results']:
    print('Nenhum resultado encontrado!')
    exit()

imagem_url = response['photos'][0]['src']['original']
imagem = Image.open(BytesIO(requests.get(imagem_url).content))
imagem.show()
