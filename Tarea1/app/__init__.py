import sqlite3

db = sqlite3.connect('data/tarea1')

cursor = db.cursor()

print("""MI BIBLIOTECA
1. AGREGAR
2. QUITAR
3. LISTAR
4. CONSULTAR
5. SALIR""")
opc = (int(input("Opcion: ")))

if (opc==1):
    print("USTED VA AGREGAR UN DATO")
    autor = input("Autor: ")
    titulo = input("Titulo: ")
    fecha = input("Fecha: ")

    cursor.execute('''INSERT INTO libros(autor, titulo, fecha)
     VALUES(?,?,?)''', (autor, titulo, fecha))

    db.commit()
    db.close()

elif(opc==2):
    print("USTED HA DECIDIDO ELIMINAR  UN DATO")
    # BORRAR DATOS
    cursor.execute('''SELECT id, autor, titulo, fecha FROM libros''')
    resultado = cursor.fetchall()
    for fila in resultado:
         print("{0} : {1}".format(fila[0], fila[1]), fila[2], fila[3])

    id = input("ID de usuario a eliminar: ")
    for fila in resultado:
        if int(id) == int(fila[0]):
            cursor.execute('''DELETE FROM libros WHERE id = ?''',
                           (id,))
            db.commit()


elif(opc==3):
    print("USTED HA DECIDIDO VER LA LISTA")
    # PARA VER LOS DATOS
    cursor.execute('''SELECT id, autor, titulo, fecha FROM libros''')
    resultado = cursor.fetchall()
    for fila in resultado:
      print("{0} : {1}".format(fila[0], fila[1]),fila[2],fila[3])

    db.commit()
    db.close()
elif(opc==4):
    print("USTED HA DECIDIDO HACER UNA CONSULTA")

    cursor.execute('''SELECT titulo FROM libros''')
elif(opc==5):
    print("USTED HA DECIDIDO SALIR")



else:
    print("OPCION NO VALIDA")
#cursor.execute(''' CREATE TABLE libros(id INTEGER PRIMARY KEY, autor TEXT, titulo TEXT, fecha DATE)''')

#db.commit()
#db.close()
#PARA INSERTAR DATOS




