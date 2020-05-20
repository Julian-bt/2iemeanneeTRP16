from PySide2.QtWidgets import *
from random import *
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.liste=["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]


        self.setWindowTitle("Cycle ISEN") #titre fenetre
        self.setMinimumSize(500,300)

        self.layout = QVBoxLayout()

        self.label=QLabel("CSI")
        self.layout.addWidget(self.label)

        self.button1 = QPushButton("Changer le cycle")
        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.buttonClicked)


        self.setLayout(self.layout)

    def buttonClicked(self):
        choix=choice(self.liste)
        self.label.setText(choix)






if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()

