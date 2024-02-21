import sys
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem,QLabel,QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="1234.abcd",
    database="CURSOS"
)
cursor = cx.cursor()

class AtualizarCurso(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Atualização de dados de cursos já cadastrados.")

        labelID = QLabel("ID do Curso:")
        self.editID = QLineEdit()

        labelNomeC = QLabel("Nome do Curso:")
        self.editNomeC = QLineEdit()

        labelCarga = QLabel("Carga Horária do Curso:")
        self.editCarga = QLineEdit()

        btAtualizacao = QPushButton("Atualizar")

        layout.addWidget(labelID)
        layout.addWidget(self.editID)

        layout.addWidget(labelNomeC)
        layout.addWidget(self.editNomeC)

        layout.addWidget(labelCarga)
        layout.addWidget(self.editCarga)

        layout.addWidget(btAtualizacao)
        btAtualizacao.clicked.connect(self.upCurso)

        tbCursos = QTableWidget(self)
        tbCursos.setColumnCount(4)
        tbCursos.setRowCount(10)

        headerLine=["Id","Nome","Carga Horária"]

        tbCursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from TBCURSOS")
        lintb = 0
        for linha in cursor:
            tbCursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbCursos.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbCursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1

       
        layout.addWidget(tbCursos)
        self.setLayout(layout)

    def upCurso(self):
            if(self.editID.text()==""):
                print("Não é possível realizar uma atualização sem o ID do curso")
            elif(self.editNomeC.text()!="" and self.editCarga.text()==""):
                    cursor.execute("update TBCURSOS set NOMEcurso=%s where CURSOSid=%s",
                                (self.editNomeC.text(), self.editID.text()))
            elif(self.editNomeC.text()=="" and self.editCarga.text()!=""):
                    cursor.execute("update TBCURSOS set CARGAhoraria=%s where CURSOSid=%s",
                                   self.editCarga.text(), self.editID.text())
            else:
                  cursor.execute("update TBCURSOS set NOMEcurso=%s, CARGAhoraria=%s where CURSOSid=%s",
                                 self.editNomeC.text(), self.editCarga.text(),self.editID.text())  
            cx.commit()
            print("Atualizado")

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCurso()
    tela.show()
    sys.exit(app.exec_())

