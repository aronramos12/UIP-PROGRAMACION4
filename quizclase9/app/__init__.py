def corutina_letra():
    for i in range(ord('a'), ord('m')+1):
        yield(chr(i))

if __name__ == "__main__":
    letras = corutina_letra()
    try:
        for i in range(ord('m')):
            print (next(letras))
            if i == 'm':
                 break
    except Exception as e:
        print(e)
