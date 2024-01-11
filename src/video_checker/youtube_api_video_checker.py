from decouple import config

from src.save.save import ExcelRecorder

from .video_checker_interface import VideoCheckerInterface
from src.url_checker.url_checker import URLChecker
from src.url_checker.url_extract_id import YouTubeURLParser

import requests

# video_checker.py


class YouTubeApiVideoChecker(VideoCheckerInterface):

    def __init__(self):
        self.excel_recorder = ExcelRecorder()
        self.api_key = config('YOUTUBE_API')

    async def check_video_availability(self, url):

        url_checker = URLChecker()

        # Comprobar si la URL es una URL de YouTube válida
        if not url_checker.is_youtube_url(url):
            print("La URL no corresponde a un video de YouTube válido.")
            return "La URL no corresponde a un video de YouTube válido."
        url_parser = YouTubeURLParser(url)
        video_id = url_parser.extract_video_id()

        base_url = "https://www.googleapis.com/youtube/v3/videos"
        params = {
            "key": self.api_key,
            "id": video_id,
            "part": "snippet, status",
        }

        response = requests.get(base_url, params=params)
        print("respuesta: ", response)
        if response.status_code == 200:
            data = response.json()
            if "items" in data and len(data["items"]) > 0:
                video_status = data["items"][0]["status"]["uploadStatus"]
                if video_status == "processed":
                    self.print_video_available()
                    print("data: ", data)

                    return "El video está disponible en YouTube."

                else:
                    self.print_video_processing()
            else:
                self.print_video_not_found()
        elif response.status_code == 404:
            self.print_video_not_found()
        else:
            self.print_default_message(response.status_code)

        return False

    def print_video_available(self):
        print("El video está disponible en YouTube.")

    def print_video_processing(self):
        print("El video no está disponible en YouTube o aún no se ha procesado.")

    def print_video_not_found(self):
        print("El video no se encontró en YouTube.")

    def print_default_message(self, status_code):
        print(f"Ocurrio un problema la la API de YouTube: {status_code}.")
