import re

#palindromos

#frase ="¿Son mulas, o cívicos alumnos?"
frase = "Dábale arroz a la zorra el abad"

#frase = input("dime la frase: ")
def es_palindromo(frase):
    #quitar acentos, espacios y signos de puntuación
    frase = re.sub(r'[áÁ]', 'a', frase)
    frase = re.sub(r'[éÉ]', 'e', frase)
    frase = re.sub(r'[íÍ]', 'i', frase)
    frase = re.sub(r'[óÓ]', 'o', frase)
    frase = re.sub(r'[úÚ]', 'u', frase)
    frase = ''.join(frase.split())
    frase = re.sub(r'[^a-z0-9A-Z]', '', frase)
    frase = frase.lower()
    print(frase)
    print(frase[::-1])
    
    if frase == frase[::-1]:
        print("es un palindromo")
    else:
        print("no es un palindromo")

es_palindromo(frase)
    
list = [3, 7, 6, 5, 4, 6, 7, 8]

# Replace 3 with 0
list.index(3)
list[0] = 0
print(list)





    


        