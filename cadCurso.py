import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit, QVBoxLayout, QPushButton

con = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="1234.abcd",
    database="CURSOS"
)
cursor = con.cursor()

class cadCur(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Cadastro de Cursos")

        labelNomeC = QLabel("Nome do Curso:")
        self.editNomeC = QLineEdit()

        labelCarga = QLabel("Carga Horária do Curso:")
        self.editCarga = QLineEdit()

        psbCad = QPushButton("Cadastrar")

        self.labelMsg = QLabel("|")
        
        layout = QVBoxLayout()
        layout.addWidget(labelNomeC)
        layout.addWidget(self.editNomeC)

        layout.addWidget(labelCarga)
        layout.addWidget(self.editCarga)

        layout.addWidget(psbCad)
        psbCad.clicked.connect(self.cadCurso)

        layout.addWidget(self.labelMsg)

        self.setLayout(layout)

    def cadCurso(self):
        cursor.execute("insert into TBCURSOS(NOMEcurso,CARGAhoraria)values(%s,%s)",
                       (self.editNomeC.text(),self.editCarga.text()))
        con.commit()
        self.labelMsg.setText("O curso e sua carga horária foram cadastrados")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = cadCur()
    tela.show()
    sys.exit(app.exec_())