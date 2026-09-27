#Que reciba dos parámetros (nombre y edad), que muestre el mensaje dependiendo de la Edad:
#1. Edad entre 0 a 2 muestre mensaje: nombre + “ es un infante”
#2. Edad entre 3 a 10 muestre mensaje: nombre + “ es niño”
#3. Edad entre 11 a 13 muestre mensaje: nombre + “ es puber”
#4. Edad entre 14 a 18 muestre mensaje: nombre + “ es adolescente”
#5. Edad entre 19 a 59 muestre mensaje: nombre + “ es adulto”
#6. Edad mayor a 60 muestre mensaje: nombre + “ es anciano”

def main():
    #datos de entrada
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    
    #secuencia de pasos
    etapa = ""
    if edad>=0 and edad<=2:
        etapa = " es un infante"
    elif edad>=3 and edad<=10:
        etapa = " es niño"
    elif edad>=11 and edad<=13:
        etapa = " es puber"
    elif edad>=14 and edad<=18:
        etapa = " es adolescente"
    elif edad>=19 and edad<=59:
        etapa = " es adulto”"
    elif edad>=60:
        etapa = " es anciano"

    #datos de salida
    print(nombre + etapa)

main()
