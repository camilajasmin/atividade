import sys
import mysql.connector as mycon
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="1234.abcd",
    database="CURSOS"
)

cursor = cx.cursor()

class ExibirCursos(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,300)
        self.setWindowTitle("Cursos Cadastrados")

        tbCursos = QTableWidget(self)
        tbCursos.setColumnCount(3)
        tbCursos.setRowCount(10)

        headerLine=["ID", "Nome do Curso", "Carga Horária"]
        tbCursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from TBCURSOS")
        lintb = 0
        for linha in cursor:
            tbCursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbCursos.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbCursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1

        layout = QVBoxLayout()
        layout.addWidget(tbCursos)
        self.setLayout(layout)

if __name__=="__main__":
        app = QApplication(sys.argv)
        tela = ExibirCursos()
        tela.show()
        sys.exit(app.exec_())