def determinarPrecio(escrito,oral):
    nivel = determinarNivel(escrito,oral)
    precio = 0
    if nivel == 3:
        precio = 400
    elif nivel == 2:
        precio = 250
    elif nivel == 1:
        precio = 150
    return precio

def determinarNivel(escrito,oral):
    nivel = 0
    if escrito > 95 and oral > 75:
        nivel = 3
    elif escrito > 95 and oral <= 75:
        nivel = 2
    elif escrito <= 95:
        nivel = 1
    return nivel

def ejercicio2():
    #datos prueba (entrada)
    escrito = 97
    oral = 75
    
    #pregunta A
    nivel = determinarNivel(escrito,oral)
    print("El nivel es",nivel)
    
    #pregunta B
    precio = determinarPrecio(escrito,oral)
    print("El precio a pagar es",precio)
    
ejercicio2()