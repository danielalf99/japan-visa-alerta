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

    # Obtener todos los elementos que contienen "残"
    elementos = page.get_by_text(
        "残",
        exact=False
    )

    cantidad = elementos.count()

    print("\nElementos de disponibilidad encontrados:", cantidad)

    for i in range(cantidad):

        elemento = elementos.nth(i)

        try:
            texto = elemento.inner_text()

            print(
                f"{i}: {texto}"
            )

        except Exception as error:
            print(
                f"{i}: ERROR - {error}"
            )

    browser.close()
