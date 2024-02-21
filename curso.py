import mysql.connector as mc 

conexao = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="1234.abcd",
    database="CURSOS"
    )

print(conexao)


cursor = conexao.cursor()

cursor.execute("describe CURSOS.TBCURSOS")
print(cursor)

# for c in cursor:
#     print (f"ID do curso: {c[0]}")
#     print (f"NOME do curso: {c[1]}")
#     print (f"CARGA HORÁRIA do curso: {c[2]}")
    