from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self,clic):
        QWidget.__init__(self)
        self.click=clic
        self.layout = QVBoxLayout()
        self.setWindowTitle("IHM") #titre fenetre

        self.button1 = QPushButton("Changer mon texte!")
        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.buttonClicked)

        self.texte=QTextEdit('le nombre de flic va etre affiche ici')
        self.layout.addWidget(self.texte)

        self.setLayout(self.layout)

    def buttonClicked(self):
        self.click+=1
        self.button1.setText("click "+str(self.click))
        self.texte.setText("click "+str(self.click))
        #print("click",self.click)


if __name__ == "__main__":
   app = QApplication([])
   win = Window(0)
   win.show()
   app.exec_()



