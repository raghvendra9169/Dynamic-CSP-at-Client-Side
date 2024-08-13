from PyQt5.QtWidgets import QMainWindow, QTabWidget, QAction, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from tab import Tab
from toolbar import Toolbar
from history import History
from cookies_management import CookiesManagement
from bookmarks import Bookmarks
from web_inspection import WebInspector

try:
    from PyQt5.QtWebEngineCore import QWebEngineProfile
except ImportError:
    QWebEngineProfile = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modular Browser")

        self.setWindowIcon(QIcon("images/brow.png"))
        self.setGeometry(100, 100, 1200, 800)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url_bar)

        self.history = History()
        self.bookmarks = Bookmarks()

        if QWebEngineProfile is not None:
            self.cookies_management = CookiesManagement(QWebEngineProfile.defaultProfile())
        else:
            self.cookies_management = None

        self.setCentralWidget(self.tabs)

        self.toolbar = Toolbar(self)
        self.addToolBar(self.toolbar)

        self.add_new_tab("https://www.google.com", "Homepage")

    def add_new_tab(self, url, label):
        new_tab = Tab(self, url)
        self.tabs.addTab(new_tab, label)
        self.tabs.setCurrentWidget(new_tab)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def update_url_bar(self, index):
        current_tab = self.tabs.widget(index)
        if current_tab:
            url = current_tab.web_view.url().toString()
            self.toolbar.url_bar.setText(url)

    def open_history(self):
        history_widget = QWidget()
        history_layout = QVBoxLayout()
        history_widget.setLayout(history_layout)

        for url in self.history.get_urls():
            label = QLabel(url)
            history_layout.addWidget(label)

        self.add_new_tab("about:blank", "History")
        current_tab = self.tabs.currentWidget()
        layout = current_tab.layout()
        layout.addWidget(history_widget)

    def open_bookmarks(self):
        bookmarks_widget = QWidget()
        bookmarks_layout = QVBoxLayout()
        bookmarks_widget.setLayout(bookmarks_layout)

        for bookmark in self.bookmarks.get_bookmarks():
            label = QLabel(bookmark)
            bookmarks_layout.addWidget(label)

        self.add_new_tab("about:blank", "Bookmarks")
        current_tab = self.tabs.currentWidget()
        layout = current_tab.layout()
        layout.addWidget(bookmarks_widget)

    def open_cookies_management(self):
        if self.cookies_management:
            self.cookies_management.show()
        else:
            print("Cookies management is not available in this version.")


