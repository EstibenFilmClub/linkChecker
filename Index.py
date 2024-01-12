# index.py
from src.view.ui import VideoCheckerUI

import flet


def main(page):

    print("ejecutnado main.py")
    app_ui = VideoCheckerUI(page)
    app_ui.create_ui()


# flet.app(target=main)flet.app(target=main, host="0.0.0.0", port=8000)ppp
flet.app(target=main, view=flet.WEB_BROWSER, port=8000)
