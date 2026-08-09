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

    elementos = page.get_by_text(
        "残",
        exact=False
    )

    print(
        "\nElementos encontrados:",
        elementos.count()
    )

    # Inspeccionar la primera celda
    if elementos.count() > 0:

        primero = elementos.nth(0)

        print("\n--- HTML DE LA PRIMERA CELDA ---")

        print(
            primero.evaluate(
                "(element) => element.outerHTML"
            )
        )

        print("\n--- PADRE DE LA CELDA ---")

        print(
            primero.evaluate(
                "(element) => element.parentElement.outerHTML"
            )
        )

    browser.close()
