import sqlite3
import hashlib
#db = sqlite3.connect(':memory:')#base de datos en memoria
#db = sqlite3.connect('data/prueba') #base de datos en un archivo

#cursor = db.cursor()
def cifrar_password(password):
    cifrado=hashlib.sha512(password.encode('utf-8')).hexdigest()
    return cifrado
db = sqlite3.connect('data/prueba')#base de datos en un archivo
db.create_function('cifrar', 1, cifrar_password)
cursor = db.cursor()
cursor.execute('''CREATE TABLE clave(id INTEGER PRIMARY KEY,
                    email TEXT, password TEXT)''')
usuario= input("correo: ")
password= input("password: ")
cursor.execute('''INSERT INTO clave(email, password) VALUES
                    (?,cifrar(?))''',(usuario, password))
db.commit()
#cursor.execute('''SELECT id, nombre FROM usuario''')
#resultado = cursor.fetchall()
#for fila in resultado:
 #   print("{0} : {1}".format(fila[0], fila[1]))

#id = input("ID de usuario a modificar: ")
#for fila in resultado:
#    if int(id)== int (fila[0]):
#        nuevo_nombre = input("Nombre Nuevo: ")
#        cursor.execute('''UPDATE usuario SET nombre = ? WHERE
#                            id= ?''',(nuevo_nombre, id))
#        db.commit()

#cursor.execute('''CREATE TABLE usuario(id INTEGER PRIMARY KEY, nombre TEXT,
#			telefono TEXT, email TEXT UNIQUE,password TEXT)''')
#db.commit()
#cursor.execute('''DROP TABLE usuario''')
#db.commit()

#sqlitebrowser
#nombre = input("Nombre: ")
#telefono = input("Telefono: ")
#email = input("Email: ")
#password = input("Password: ")

#cursor.execute('''INSERT INTO usuario(nombre, telefono, email, password)
#                    VALUES(?,?,?,?)''', (nombre, telefono,email,password))

#cursor.execute('''INSERT INTO usuario(nombre, telefono, email, password)
 #                VALUES(:nombre, :telefono, :email, :password)''',
#                 {'nombre':nombre, 'telefono':telefono, 'email':email, 'password':password})

#db.commit()

#usuarios = [("Juan","2323222","juan2@juan.org","12345"),
 #           ("Maria", "4352122", "maria2@maria.com,""maria123"),
 #           ("Pedro","7773345", "pedro2@juan.org","p3dro")]
#cursor.executemany('''INSERT INTO usuario(nombre, telefono, email,password) VALUES(?,?,?,?)''', usuarios)

#db.commit()

#db.close()