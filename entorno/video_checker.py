# video_checker.py
import asyncio
from playwright.async_api import async_playwright
from url_checker import URLChecker
class VideoChecker:
    async def check_video_availability(self, url):

        url_checker = URLChecker()
        
        # Comprobar si la URL es una URL de YouTube válida
        if not url_checker.is_youtube_url(url):
            return "La URL no corresponde a un video de YouTube válido." 
            
            
        async with async_playwright() as p:
            # Iniciar el navegador
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # Ir a la URL del video
            await page.goto(url)
            specific_selector = ".html5-video-container .video-stream.html5-main-video"
            # Comprobar si hay mensajes de error que indiquen que el video no está disponible
            unavailable_message = await page.query_selector(".promo-title.style-scope.ytd-background-promo-renderer")
            enable_message = await page.query_selector(specific_selector)
            if unavailable_message:
                error_text = await unavailable_message.text_content()
                print("El video no está disponible")
                return "El video no está disponible" 
            elif enable_message:
                print("El video está disponible.")
                return "El video está disponible." 
            else:
                print("Programa no soportado, contacta con soporte")
                return "Programa no soportado, contacta con soporte" 

            # Cerrar el navegador
            await browser.close()
