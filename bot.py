import requests
import re
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

# Texto de la página
texto = response.text

# Buscar cantidades de cupos
patron = r"残\s*(\d+)\s*件"

resultados = re.findall(patron, texto)

print("\n--- CUPOS DETECTADOS ---")

if not resultados:
    print("No se encontraron cupos en el HTML.")
else:
    for cupo in resultados:
        print("Cupos encontrados:", cupo)

# Hora de Colombia
ahora = datetime.now(ZoneInfo("America/Bogota"))

print("\n--- HORA DEL BOT ---")
print(ahora.strftime("%Y-%m-%d %H:%M:%S"))

# ¿Hay algún cupo?
hay_cupo = any(int(cupo) > 0 for cupo in resultados)

print("\n--- RESULTADO ---")

if hay_cupo:
    print("🚨 HAY CUPOS DISPONIBLES")
else:
    print("❌ No hay cupos disponibles")
