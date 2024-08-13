from PyQt5.QtWidgets import QToolBar, QAction, QLineEdit, QMenu, QWidget, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from web_inspection import WebInspector  # Ensure this import exists and is correct

class Toolbar(QToolBar):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        # Back button
        self.back_action = QAction(QIcon("images/back.png"), "Back", self)
        self.back_action.triggered.connect(self.go_back)
        self.addAction(self.back_action)

        # Forward button
        self.forward_action = QAction(QIcon("images/forward.png"), "Forward", self)
        self.forward_action.triggered.connect(self.go_forward)
        self.addAction(self.forward_action)

        # Refresh button
        self.refresh_action = QAction(QIcon("images/refresh.png"), "Refresh", self)
        self.refresh_action.triggered.connect(self.refresh_page)
        self.addAction(self.refresh_action)

        # Home button
        self.home_action = QAction(QIcon("images/home.png"), "Home", self)
        self.home_action.triggered.connect(self.go_home)
        self.addAction(self.home_action)

        # Spacer to push next actions to the right
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.addWidget(spacer)

        # New tab button
        self.new_tab_action = QAction(QIcon("images/new_tab.png"), "New Tab", self)
        self.new_tab_action.triggered.connect(self.open_new_tab)
        self.addAction(self.new_tab_action)

        # Dropdown menu
        self.dropdown_action = QAction(QIcon("images/dropdown.png"), "Menu", self)
        self.dropdown_action.triggered.connect(self.show_dropdown_menu)
        self.addAction(self.dropdown_action)

    def go_back(self):
        self.main_window.tabs.currentWidget().web_view.back()

    def go_forward(self):
        self.main_window.tabs.currentWidget().web_view.forward()

    def refresh_page(self):
        self.main_window.tabs.currentWidget().web_view.reload()

    def go_home(self):
        self.main_window.tabs.currentWidget().web_view.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.main_window.tabs.currentWidget().web_view.setUrl(QUrl(url))

    def open_new_tab(self):
        self.main_window.add_new_tab("https://www.google.com", "New Tab")

    def show_dropdown_menu(self):
        menu = QMenu(self)

        history_action = QAction("History", self)
        history_action.triggered.connect(self.main_window.open_history)
        menu.addAction(history_action)

        bookmarks_action = QAction("Bookmarks", self)
        bookmarks_action.triggered.connect(self.main_window.open_bookmarks)
        menu.addAction(bookmarks_action)

        cookies_action = QAction("Cookies Management", self)
        cookies_action.triggered.connect(self.main_window.open_cookies_management)
        menu.addAction(cookies_action)

        web_inspection_action = QAction("Web Inspector", self)
        web_inspection_action.triggered.connect(self.open_web_inspector)
        menu.addAction(web_inspection_action)

        action_position = self.actionGeometry(self.dropdown_action).bottomLeft()
        menu.exec_(self.mapToGlobal(action_position))

    def open_web_inspector(self):
        inspector = WebInspector()  # Ensure this is correctly implemented
        self.main_window.add_new_tab("about:blank", "Web Inspector")
        current_tab = self.main_window.tabs.currentWidget()
        layout = current_tab.layout()
        layout.addWidget(inspector)
