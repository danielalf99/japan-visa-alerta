import requests
from bs4 import BeautifulSoup

URL = "https://embjpcol.rsvsys.jp/reservations/calendar"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)

print("Estado de la página:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

texto = soup.get_text(" ", strip=True)

print(texto[:5000])
