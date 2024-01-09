import asyncio
from playwright.async_api import async_playwright

async def check_video_availability(url):
    async with async_playwright() as p:
        # Iniciar el navegador
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Ir a la URL del video
        await page.goto(url)

        # Comprobar si hay mensajes de error que indiquen que el video no está disponible
        unavailable_message = await page.query_selector(".promo-title.style-scope.ytd-background-promo-renderer")
        if unavailable_message:
            error_text = await unavailable_message.text_content()
            print(f"El video no está disponible: {error_text.strip()}")
        else:
            print("El video está disponible.")

        # Cerrar el navegador
        await browser.close()

# URL del video de YouTube
video_urlbueno = "https://www.youtube.com/watch?v=iwXV_xgf1zI"
video_urlmalo = "https://www.youtube.com/watch?v=iwsXVaa_xgf"
asyncio.run(check_video_availability(video_urlmalo))
