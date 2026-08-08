¿from playwright.sync_api import sync_playwright

URL = "https://embjpcol.rsvsys.jp/reservations/calendar"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/150.0.0.0 Safari/537.36"
        )
    )

    print("Abriendo calendario...")

    page.goto(
        URL,
        wait_until="networkidle",
        timeout=60000
    )

    print("Página cargada")

    # Esperar a que el calendario aparezca
    page.wait_for_timeout(5000)

    texto = page.locator("body").inner_text()

    print("\n--- CALENDARIO ---")
    print(texto[:10000])

    browser.close()
