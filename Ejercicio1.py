def determinarPrecio(escrito,oral):
    nivel = determinarNivel(escrito,oral)
    precio = 0
    if nivel == 3:
        precio = 400
    elif nivel == 2:
        precio = 450
    elif nivel == 1>
        precio = 300
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

    
    #pregunta A
    nivel = determinarNivel(escrito,oral)
    print("El nivel es",nivel)
    
    #pregunta B
    precio = determinarPrecio(escrito,oral)
    print("El precio a pagar es",precio)
    
ejercicio2()