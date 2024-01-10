from video_checker.video_checker_interface import VideoCheckerInterface
import asyncio
from playwright.async_api import async_playwright
from url_checker.url_checker import URLChecker
from save.save import ExcelRecorder


class NetflixVideoChecker(VideoCheckerInterface):
    def __init__(self):
        self.excel_recorder = ExcelRecorder()

    async def check_video_availability(self, url):
       
        url_checker = URLChecker()
        
        # Comprobar si la URL es una URL de Netflix válida
        if not url_checker.is_netflix_url(url):
            print("La URL no corresponde a un video de Netflix válido.")
            return "La URL no corresponde a un video de Netflix válido."

        async with async_playwright() as p:
            # Iniciar el navegador
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # Ir a la URL del video
            await page.goto(url)

            # Buscar el contenedor del video
            # Buscar el título del video usando data-testid
            video_title = await page.query_selector('[data-testid="Title"]')



            if video_title:
                # Si se encuentra el título, se asume que el video está disponible
                title_text = await video_title.text_content()
                if title_text.strip():
                    print(f"El video está disponible: {title_text}")
                    self.excel_recorder.add_video_info(url, title_text)
                    return f"El video está disponible: {title_text}"
                else:
                    print("No se encontró el título del video, puede que no esté disponible.")
                    return "No se encontró el título del video, puede que no esté disponible."

            # Cerrar el navegador
            await browser.close()
