import flet
from video_checker.video_checker_factory import VideoCheckerFactory
import asyncio
class VideoCheckerUI:

    def __init__(self, page):
        self.page = page
        self.factory = VideoCheckerFactory()
    
    def create_ui(self):
        self.url_input = flet.TextField(label="Ingresa la URL del video de YouTube", width=300)
        self.submit_button = flet.ElevatedButton(text="Comprobar")
        self.result_label = flet.Text("")

        self.submit_button.on_click = self.on_submit_click

        self.page.add(self.url_input, self.submit_button, self.result_label)

    async def check_video(self, url):
        self.result_label.value = "Espere..."
        self.page.update()

        try:
            video_checker = self.factory.get_video_checker(url)
            result = await video_checker.check_video_availability(url)
        except ValueError as e:
            result = str(e)
        self.result_label.value = result
        self.page.update()

    def on_submit_click(self, e):
        asyncio.run(self.check_video(self.url_input.value))