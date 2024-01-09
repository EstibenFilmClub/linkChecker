from video_checker.video_checker_interface import VideoCheckerInterface

# video_checker.py
import asyncio
from playwright.async_api import async_playwright
from url_checker.url_checker import URLChecker

class YouTubeVideoChecker(VideoCheckerInterface):
    async def check_video_availability(self, url):
        url_checker = URLChecker()
        
        # Comprobar si la URL es una URL de YouTube válida
        if not url_checker.is_youtube_url(url):
            print("La URL no corresponde a un video de YouTube válido.")
            return "La URL no corresponde a un video de YouTube válido."

        async with async_playwright() as p:
            # Iniciar el navegador
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # Ir a la URL del video
            await page.goto(url)

            

            # Buscar el contenedor del video
            video_container = await page.query_selector(".html5-video-container")

            if video_container:
                # Buscar el elemento video dentro del contenedor
                video_element = await video_container.query_selector("video")

                if video_element:
                    # Obtener el atributo src del video
                    src = await video_element.get_attribute("src")

                    if src:
                        print("El video está disponible.")
                        return "El video está disponible."
                    else:
                        unavailable_message = await page.query_selector(".promo-title.style-scope.ytd-background-promo-renderer")
                        error_text = await unavailable_message.text_content()
                        print(f"No se encontró el video. "+ error_text)
                        return f"No se encontró el video. {error_text}"
            else:
                print("No se encontró el contenedor del video contacta con soporte.")
                return "No se encontró el contenedor del video contacta con soporte."

            # Cerrar el navegador
            await browser.close()