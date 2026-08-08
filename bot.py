import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo

URL = "https://embjpcol.rsvsys.jp/reservations/calendar"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    )
}

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)

print("Estado:", response.status_code)

if response.status_code != 200:
    raise Exception("No se pudo acceder al calendario")

soup = BeautifulSoup(response.text, "html.parser")

texto = soup.get_text(" ", strip=True)

print("\n--- COMPROBACIÓN DE DISPONIBILIDAD ---")

if "Cupos disponibles" in texto:
    print("🚨 HAY ALGUNA FECHA CON DISPONIBILIDAD")
else:
    print("❌ No se detectó disponibilidad")

print("\n--- ESTADO DEL CALENDARIO ---")

print("Cupos disponibles:",
      texto.count("Cupos disponibles"))

print("Completos:",
      texto.count("Completos"))

print("\n--- HORA COLOMBIA ---")

ahora = datetime.now(ZoneInfo("America/Bogota"))

print(ahora.strftime("%Y-%m-%d %H:%M:%S"))
