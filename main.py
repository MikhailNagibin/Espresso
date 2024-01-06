from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
import sqlite3


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(800, 600)
        con = sqlite3.connect('cofee.sqlite')
        cur = con.cursor()
        data = list(cur.execute("""select sort, degree_of_roasting, type, description_of_taste, price, packaging_volume
                                from main"""))
        self.add.setHorizontalHeaderLabels(['sort', 'degree_of_roasting', 'type',
                                                    'description_of_taste', 'price', 'packaging_volume'])
        if data:
            self.add.setColumnCount(len(data[0]))
            self.add.setRowCount(0)
            for i, row in enumerate(data):
                self.add.setRowCount(
                    self.add.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.add.setItem(
                        i, j, QTableWidgetItem(str(elem)))

            self.add.resizeColumnsToContents()
        self.pushButton.clicked.connect(self.new)

    def new(self):
        self.close()
        self.add = Insert()
        self.add.show()


class Insert(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setFixedSize(800, 600)
        self.pushButton.clicked.connect(self.add)

    def add(self):
        sort = self.lineEdit_4.text()
        degree = self.lineEdit.text()
        type = self.lineEdit_2.text()
        price = self.lineEdit_3.text()
        des = self.lineEdit_5.text()
        v = self.lineEdit_6.text()
        con = sqlite3.connect('cofee.sqlite')
        cur = con.cursor()
        cur.execute(f"insert into main(sort, degree_of_roasting, type, description_of_taste, price, packaging_volume)"
                    f"values(?, ?, ?, ?, ?, ?)", (sort, degree, type, des, price, v))
        con.commit()
        con.close()
        self.close()
        self.m = Main()
        self.m.show()


"""        cur.execute(f"insert into main(name_of_race, year, count_of_flags, count_of_of_starts, duration_of_starts)" 
               f"values(?, ?, ?, ?, ?)", (name, year, flags, starts, minuts))"""

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
