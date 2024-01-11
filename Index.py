# index.py
from src.view.ui import VideoCheckerUI

import flet


def main(page):

    app_ui = VideoCheckerUI(page)
    app_ui.create_ui()


flet.app(target=main)
