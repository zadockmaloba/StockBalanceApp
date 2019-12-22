import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*


class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        global layout
        layout=QGridLayout()
        self.setLayout(layout)
        self.initUI()

    def initUI(self):
        self.setGeometry(60,100,1020,600)
        self.setWindowTitle('Stockbalance APP: Main Menu')
        self.menu_setup()
        self.menubar()
        self.show()

    def menubar(self):
        menu_bar=QMenuBar(self)
    def menu_setup(self):
        menubtns=[[0,0,0],
                  [0,0,0]]
        menubtn_text=[['Check Balances','Manage Tables', 'Create Table'],
                      ['Stock Analysis','.','Quit']]
        for i in range(2):
            for j in range(3):
                menubtns[i][j]=QPushButton(self)
                menubtns[i][j].setText(menubtn_text[i][j])
                menubtns[i][j].resize(20,20)
                layout.addWidget(menubtns[i][j], i, j)

    def menubtn_checkbalnace():
        pass
    def menubtn_managetables():
        pass
    def menubtn_createtable():
        pass
    def menubtn_stockanalysis():
        pass
    def menubtn_quit():
        quit()

class checkBalanceWindow(QWidget):
    def __init__(self):
        pass
class manageTablesWindow(QWidget):
    def __init__(self):
        pass
class createTableWindow(QWidget):
    def __init__(self):
        pass
class stockAnalysisWindow(QWidget):
    def __init__(self):
        pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyle('Fusion')
    ex=mainwindow()
    sys.exit(app.exec_())
