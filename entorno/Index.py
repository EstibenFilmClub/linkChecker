import flet
from video_checker import VideoChecker
import asyncio

def main(page):
    video_checker = VideoChecker()

    # Crear los elementos de la interfaz
    url_input = flet.TextField(label="Ingresa la URL del video de YouTube", width=300)
    submit_button = flet.ElevatedButton(text="Comprobar")
    result_label = flet.Text("")

    async def check_video(url):
        result = await video_checker.check_video_availability(url)
        result_label.value = result
        page.update()

    def on_submit_click(e):
        asyncio.run(check_video(url_input.value))

    submit_button.on_click = on_submit_click

    # Agregar elementos a la página
    page.add(url_input, submit_button, result_label)

flet.app(target=main)
