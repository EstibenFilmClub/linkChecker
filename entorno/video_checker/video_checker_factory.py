from video_checker.youtube_video_checker import YouTubeVideoChecker
from video_checker.netflix_video_checker import NetflixVideoChecker

class VideoCheckerFactory:
    @staticmethod
    def get_video_checker(url):
        if "youtube" in url:
            return YouTubeVideoChecker()
        elif "netflix" in url:
            return NetflixVideoChecker()
        else:
            raise ValueError("Plataforma no soportada")