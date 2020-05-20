from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        self.click=0
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.setWindowTitle("IHM") #titre fenetre

        self.button1 = QPushButton("Changer mon texte!")
        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.buttonClicked)

        self.setLayout(self.layout)

    def buttonClicked(self):
        self.close()






if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
