import requests
import re

URL = "https://embjpcol.rsvsys.jp/reservations/calendar"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=headers, timeout=30)

print("Estado:", response.status_code)
print("Tamaño HTML:", len(response.text))

# Buscar scripts utilizados por la página
scripts = re.findall(
    r'<script[^>]+src=["\']([^"\']+)',
    response.text,
    re.IGNORECASE
)

print("\n--- SCRIPTS ---")

for script in scripts:
    print(script)

print("\n--- POSIBLES LLAMADAS AL CALENDARIO ---")

# Buscar palabras relacionadas con la carga del calendario
palabras = [
    "calendar",
    "reservation",
    "schedule",
    "ajax",
    "api",
    "availability",
    "next",
    "prev"
]

html = response.text.lower()

for palabra in palabras:
    cantidad = html.count(palabra)
    print(f"{palabra}: {cantidad}")
