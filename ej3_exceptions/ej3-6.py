import mysql.connector
from mysql.connector import Error

cnx = mysql.connector.connect(user='bdi', password='pepe1234', host='127.0.0.1', database='empresa')
cursor = cnx.cursor()
try:
    add_medico = ("INSERT INTO MEDICOS "
                 "(dni, nombre)"
                 "VALUES (%s, %s)")

    data_medico = (33457892, 'Ricchiardo Rinoldi')

    cursor.execute(add_medico, data_medico)
    cnx.commit()
except mysql.connector.errors.IntegrityError:
    print("whoops! hubo un problema inesperado!")
cursor.close()
cnx.close()