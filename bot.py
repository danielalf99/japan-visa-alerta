from playwright.sync_api import sync_playwright

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

    filas = page.locator("tr")

    print("\n--- CALENDARIO ---")

    for i in range(filas.count()):

        fila = filas.nth(i)

        celdas = fila.locator("td, th")

        if celdas.count() == 0:
            continue

        textos = []

        for j in range(celdas.count()):

            texto = celdas.nth(j).inner_text().strip()

            if texto:
                textos.append(texto.replace("\n", " "))

        if textos:
            print(" | ".join(textos))

    browser.close()
