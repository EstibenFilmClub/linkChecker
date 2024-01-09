class VideoCheckerInterface:
    async def check_video_availability(self, url):
        raise NotImplementedError
