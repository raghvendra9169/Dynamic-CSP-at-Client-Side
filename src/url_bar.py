from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QUrl

class URLBar(QLineEdit):
    def __init__(self, parent=None):
        super(URLBar, self).__init__(parent)
        self.returnPressed.connect(self.navigate_to_url)
    
    def navigate_to_url(self):
        url = QUrl(self.text())
        if url.scheme() == "":
            url.setScheme("http")
        self.parent().tabs.currentWidget().setUrl(url)
    
    def set_url(self, url):
        self.setText(url.toString())
        self.setCursorPosition(0)
