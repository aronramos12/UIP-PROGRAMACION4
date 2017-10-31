def generar_secuencia():
    impar = 1

    while True:
       yield impar
       impar = impar + 2

if __name__ == "__main__":
    generador = generar_secuencia()
#   print(next(generador))

    numeros = generar_secuencia()
    for n in numeros:
        print(n)
        if n >20:
             break