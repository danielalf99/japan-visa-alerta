from playwright.sync_api import sync_playwright

URL = "https://embjpcol.rsvsys.jp/reservations/calendar"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    print("Abriendo la página...")

    page.goto(URL, wait_until="networkidle", timeout=60000)

    print("Página cargada.")

    page.wait_for_timeout(5000)

    texto = page.locator("body").inner_text()

    print("----- INFORMACIÓN DEL CALENDARIO -----")
    print(texto[:10000])

    browser.close()
