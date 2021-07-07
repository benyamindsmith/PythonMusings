import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):

    def __init__(self): 
        super(MainWindow, self).__init__()
        # Create a browser
        self.browser = QWebEngineView()
        # Set default link upon opening
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        # Make Browser be in full screen mode
        self.showMaximized()

        ######################
        #  Navigation Bar    #
        ######################

        navbar = QToolBar()

        self.addToolBar(navbar)

        # Create a back button
        back_button=QAction('Back',self)
        # Define what happens when it is clicked
        back_button.triggered.connect(self.browser.back)
        # Add it to the navigation bar
        navbar.addAction(back_button)

        # Same thing but with a forward button
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Same thing but with a Refresh button
        refresh_button = QAction('Refresh', self)
        refresh_button.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_button)

        # Same thing but with a Home button
        home_button = QAction('Home', self)
        # Need to construct the navigate_home method
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        ######################
        # Browser Search Bar #
        ######################

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Enable for url to update when back/forward/refresh is pressed
        self.browser.urlChanged.connect(self.update_url)

    # Return home
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    # Navigate to url entered
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())




# The application

app= QApplication(sys.argv)

# Name the Browser
QApplication.setApplicationName("Qt5 Browser")

# Create the window
window= MainWindow()

app.exec()
