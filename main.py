from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
import sqlite3


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('cofee.sqlite')
        cur = con.cursor()
        data = list(cur.execute("""select sort, degree_of_roasting, type, description_of_taste, price, packaging_volume
                                from main"""))
        print(data)
        self.tableWidget.setHorizontalHeaderLabels(['sort', 'degree_of_roasting', 'type',
                                                    'description_of_taste', 'price', 'packaging_volume'])
        if data:
            self.tableWidget.setColumnCount(len(data[0]))
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(data):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))

            self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
