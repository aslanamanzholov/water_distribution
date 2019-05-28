import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
 
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):

        waterText, water = QInputDialog.getInt(self, 'Input Dialog1',
            'Введите общее количество воды(тонна):')
        cityText,city = QInputDialog.getInt(self, 'Input Dialog2', 'Введите лимит для города(тонна):')
        bathhouseText,bathhouse = QInputDialog.getInt(self, 'Input Dialog3', 'Введите лимит для бани(тонна):') 
        
        if waterText:
            result = self.le.setText(str(waterText / (cityText + bathhouseText)))
        # if waterText / (cityText + bathhouseText) == 1.0:
        #      self.le.setText(str(waterText / 2))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


    

