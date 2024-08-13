from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QUrl
from url_bar import UrlBar

class Tab(QWidget):
    def __init__(self, main_window, url):
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.url_bar = UrlBar(self)
        self.web_view = QWebEngineView()

        self.web_view.setUrl(QUrl(url))
        self.web_view.urlChanged.connect(self.update_url)
        self.web_view.loadFinished.connect(self.record_history)

        self.layout.addWidget(self.url_bar)
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def record_history(self):
        url = self.web_view.url().toString()
        self.main_window.history.add_url(url)

    def navigate_to_url(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.web_view.setUrl(QUrl(url))
