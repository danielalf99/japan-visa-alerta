from playwright.sync_api import sync_playwright
import re
from datetime import datetime

URL = "https://embjpcol.rsvsys.jp/reservations/calendar"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    print("Abriendo página...")

    page.goto(
        URL,
        wait_until="networkidle",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    print("Página cargada.")

    # -----------------------------------------
    # OBTENER FECHAS DEL CALENDARIO
    # -----------------------------------------

    encabezado = page.locator("table").first.locator("tr").first

    columnas = encabezado.locator("th, td")

    fechas = []

    for i in range(columnas.count()):

        texto = columnas.nth(i).inner_text().strip()

        if re.match(r"\d{2}/\d{2}", texto):
            fechas.append(texto)

    print("\nFechas detectadas:")

    for fecha in fechas:
        print(fecha)

    # -----------------------------------------
    # RECORRER FILAS
    # -----------------------------------------

    citas = []

    filas = page.locator("table").first.locator("tr")

    for i in range(filas.count()):

        fila = filas.nth(i)

        celdas = fila.locator("th, td")

        if celdas.count() < 2:
            continue

        hora = celdas.nth(0).inner_text().strip()

        if not re.match(r"^\d{2}:\d{2}$", hora):
            continue

        # Las celdas de disponibilidad
        for j in range(1, celdas.count()):

            celda = celdas.nth(j)

            texto = celda.inner_text().strip()

            if "残" not in texto:
                continue

            # Buscar número de cupos
            match = re.search(r"残\s*(\d+)", texto)

            if not match:
                continue

            cupos = int(match.group(1))

            if cupos > 0:

                fecha = (
                    fechas[j - 1]
                    if j - 1 < len(fechas)
                    else "Fecha desconocida"
                )

                citas.append({
                    "fecha": fecha,
                    "hora": hora,
                    "cupos": cupos
                })

    # -----------------------------------------
    # RESULTADO
    # -----------------------------------------

    print("\n==============================")
    print("RESULTADO DE LA REVISIÓN")
    print("==============================")

    if not citas:

        print("❌ No hay citas disponibles.")

    else:

        print(
            f"🚨 SE ENCONTRARON {len(citas)} CITAS"
        )

        for cita in citas:

            print(
                f"\n📅 Fecha: {cita['fecha']}"
                f"\n⏰ Hora: {cita['hora']}"
                f"\n👥 Cupos: {cita['cupos']}"
            )

            if cita["cupos"] >= 3:

                print(
                    "⭐ ¡ESTA CITA SIRVE PARA 3 SOLICITUDES!"
                )

    browser.close()
