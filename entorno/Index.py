#index.py
import flet
from video_checker.video_checker_factory import VideoCheckerFactory

from view.ui import VideoCheckerUI


def main(page):

    app_ui = VideoCheckerUI(page)
    app_ui.create_ui()

flet.app(target=main)
