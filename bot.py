import requests
import re

BASE_URL = "https://embjpcol.rsvsys.jp"

URL = BASE_URL + "/reservations/calendar"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    )
}

# 1. Descargar la página
response = requests.get(URL, headers=headers, timeout=30)

print("Estado página:", response.status_code)
print("Tamaño HTML:", len(response.text))

# 2. Descargar el JavaScript del calendario
js_url = BASE_URL + "/assets/js/user/reservations/calendar.js?1763711289"

js_response = requests.get(
    js_url,
    headers=headers,
    timeout=30
)

print("\nEstado JavaScript:", js_response.status_code)
print("Tamaño JavaScript:", len(js_response.text))

# 3. Mostrar líneas relacionadas con las citas/calendario
print("\n--- LÍNEAS IMPORTANTES DEL JAVASCRIPT ---")

keywords = [
    "ajax",
    "calendar",
    "reservation",
    "reserve",
    "next",
    "prev",
    "url",
    "json",
    "get",
    "post"
]

for i, line in enumerate(js_response.text.splitlines(), 1):
    line_lower = line.lower()

    if any(keyword in line_lower for keyword in keywords):
        print(f"{i}: {line[:1000]}")
