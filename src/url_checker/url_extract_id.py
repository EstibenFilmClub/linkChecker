class YouTubeURLParser:
    def __init__(self, url):
        self.url = url

    def extract_video_id(self):
        # Verificar si la URL es válida para YouTube
        if "youtube.com" not in self.url:
            return None

        # Separar el ID del video de la URL
        parts = self.url.split("v=")
        if len(parts) != 2:
            return None

        video_id = parts[1]
        # Eliminar cualquier argumento adicional en la URL
        video_id = video_id.split("&")[0]
        return video_id