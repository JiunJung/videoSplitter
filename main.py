import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog, QGridLayout
from video_splitter import video_splitter

filename=""
foldername = ""

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #버튼 생성
        selectButton = QPushButton('Video')
        selectButton.clicked.connect(self.showSelectDialog)
        
        saveButton = QPushButton('Select location')
        saveButton.clicked.connect(self.showSaveDialog)
        
        executeButton = QPushButton('Split!')
        executeButton.pressed.connect(self.showOngoing) # 버튼이 눌렸을 때 : "please wait" 표시
        executeButton.released.connect(lambda : self.split(filename,foldername)) # lambda를 통해서 인자전달

        #레이블 생성
        self.label1 = QLabel("",self, objectName='label1') # 선택한 비디오를 보여줌
        self.label2 = QLabel("",self,objectName='label2') # 선택한 저장위치를 보여줌
        self.label3 = QLabel("",self,objectName='label3') # 진행상태를 보여줌.

        #레이아웃
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label1)
        hbox1.addStretch(1)
        hbox1.addWidget(self.label2)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(selectButton)
        hbox2.addStretch(1)
        hbox2.addWidget(saveButton)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addStretch(1)
        hbox3.addWidget(self.label3)
        hbox3.addStretch(1)
        hbox3.addStretch(1)

        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addStretch(1)
        hbox4.addWidget(executeButton)
        hbox4.addStretch(1)
        hbox4.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Video Splitter')
        self.resize(640, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showSelectDialog(self):
        fname = QFileDialog.getOpenFileName(self,'동영상 선택','./','*.mp4')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                global filename
                filename = f.name
                self.label1.setText(filename)

    def showSaveDialog(self):
        global foldername
        folder = QFileDialog.getExistingDirectory(self,"저장 위치")
        foldername = folder
        self.label2.setText(foldername)

    def showOngoing(self):
        self.label3.setText("please wait...")

    def split(self,filename,foldername):
        video_splitter(filename,foldername)
        self.label3.setText("complete!")


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())