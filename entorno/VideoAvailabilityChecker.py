import asyncio
from playwright.async_api import async_playwright

class VideoAvailabilityChecker:
    def __init__(self):
        self.browser = None
        self.page = None

    async def start_browser(self):
        async with async_playwright() as p:
            self.browser = await p.chromium.launch()
            self.page = await self.browser.new_page()

    async def check_video_availability(self, url):
        await self.page.goto(url)
        unavailable_message = await self.page.query_selector(".promo-title.style-scope.ytd-background-promo-renderer")
        if unavailable_message:
            error_text = await unavailable_message.text_content()
            print(f"El video no está disponible: {error_text.strip()}")
        else:
            print("El video está disponible.")

    async def close_browser(self):
        await self.browser.close()
