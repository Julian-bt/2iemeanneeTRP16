from PySide2.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()

        self.setWindowTitle("IHM") #titre fenetre
        #self.setMinimumSize(100,50)

        self.barre=QProgressBar()
        self.barre.setValue(0)
        self.layout.addWidget(self.barre)

        self.slider=QSlider()
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.sliderClicked)

        self.setLayout(self.layout)

    def sliderClicked(self):
        val=self.slider.value()
        self.barre.setValue(val)



if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
