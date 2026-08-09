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

    # Buscar una celda cualquiera del calendario
    celda = page.locator("p.c_cal_time_cell").first

    print("\n--- ESTRUCTURA DEL CALENDARIO ---")

    print(
        celda.evaluate(
            "(element) => element.parentElement.parentElement.outerHTML"
        )
    )

    browser.close()
