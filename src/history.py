from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget
import json
import os

class History(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("History")
        self.layout = QVBoxLayout()
        self.history_list = QListWidget()
        self.layout.addWidget(self.history_list)
        self.setLayout(self.layout)

        # Save history in the home directory
        self.history_file = os.path.join(os.path.expanduser("~"), 'browser_history.json')
        self.load_history()

    def add_url(self, url):
        self.history_list.addItem(url)
        self.save_history()

    def save_history(self):
        history = [self.history_list.item(i).text() for i in range(self.history_list.count())]
        with open(self.history_file, 'w') as file:
            json.dump(history, file)

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                history = json.load(file)
                for url in history:
                    self.history_list.addItem(url)

    def get_urls(self):
        return [self.history_list.item(i).text() for i in range(self.history_list.count())]

    def show_history(self):
        history_html = "<html><body><h1>Browsing History</h1><ul>"
        for url in self.get_urls():
            history_html += f"<li><a href='{url}'>{url}</a></li>"
        history_html += "</ul></body></html>"
        return history_html
