from video_checker.youtube_video_checker import YouTubeVideoChecker
from video_checker.youtube_api_video_checker import YouTubeApiVideoChecker

from video_checker.netflix_video_checker import NetflixVideoChecker

class VideoCheckerFactory:
    @staticmethod
    def get_video_checker(url, use_api=False):
        if "youtube" in url:
            if use_api:
                return YouTubeApiVideoChecker()
            else:
                return YouTubeVideoChecker()
        elif "netflix" in url:
            return NetflixVideoChecker()
        else:
            raise ValueError("Plataforma no soportada")
