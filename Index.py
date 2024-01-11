#index.py
import flet
from src.view.ui import VideoCheckerUI




def main(page):

    app_ui = VideoCheckerUI(page)
    app_ui.create_ui()

flet.app(target=main)
