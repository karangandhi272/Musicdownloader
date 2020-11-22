from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget,QFileDialog
import sys
from selenium import webdriver 
import os 
from  pytube import YouTube
from moviepy.editor import *


def window():

    app = QApplication(sys.argv)
    win = Create()
    win.show()
    sys.exit(app.exec_())

class Create(QMainWindow):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.length = 400
        self.width = 200
        self.setFixedSize(self.length,self.width)
        self.setWindowTitle("Pypass")
        self.UI()

    def UI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Downloader")
        self.label.resize(self.length,40)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.userinput = QtWidgets.QLineEdit(self)
        self.userinput.move(60,60)
        self.userinput.resize(280,20)

        self.directory = QtWidgets.QPushButton(self)
        self.directory.move(60,100)
        self.directory.resize(280,30)
        self.directory.setText("Pick Directory")
        self.directory.clicked.connect(self.directorypick)
    

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Enter") 
        self.b2.clicked.connect(self.enter)
        self.b2.resize(80, 25)



       
        self.b2.move(310, 170)

    def directorypick(self):
        self.file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def enter(self):
        song = self.userinput.text()
        d = self.file
        print(d)

        driver = webdriver.Chrome()
        driver.get(f"https://www.youtube.com/results?search_query={song}+lyrics")
        s = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a').get_attribute('href')

        video = YouTube(s)
        song = video.title
        video = video.streams.first()
        video.download(f'{d}/', filename=song)



        videoclip = VideoFileClip(f'{d}/{song}.mp4')
        audioclip = videoclip.audio

        audioclip.write_audiofile(f'{d}/{song}.mp3')
        audioclip.close()
        videoclip.close()

        os.remove(f'{d}/{song}.mp4')








if "__main__" == __name__:
    window()


