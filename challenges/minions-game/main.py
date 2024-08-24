def minion_game(string):
    if not string.isalpha():
        print("El input no es válido. Debe contener solo letras del abecedario.")
    else:
        string = string.upper()
        palabras_stuart = []
        palabras_kevin = []
        vocales = ["A", "E", "I", "O", "U"]
        if 0 < len(string) and len(string) < 10**6:
            # Kevin
            for i in range(0, len(string)):
                if string[i] in vocales:
                    for x in range(0, len(string) - i):
                        palabras_kevin.append(string[i : len(string) - x])

            # Stuart
            for i in range(0, len(string)):
                if string[i] not in vocales:
                    for x in range(0, len(string) - i):
                        palabras_stuart.append(string[i : len(string) - x])

            unicos_kevin = list(set(palabras_kevin))
            unicos_stuart = list(set(palabras_stuart))
            resultados_kevin = []
            for i in unicos_kevin:
                resultados_kevin.append((i, palabras_kevin.count(i)))
            resultados_stuart = []
            for i in unicos_stuart:
                resultados_stuart.append((i, palabras_stuart.count(i)))
            # print(dict(resultados_kevin))
            # print(dict(resultados_stuart))
            if len(palabras_kevin) > len(palabras_stuart):
                print(f"Kevin {len(palabras_kevin)}")
            elif len(palabras_stuart) > len(palabras_kevin):
                print(f"Stuart {len(palabras_stuart)}")
            else:
                print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
