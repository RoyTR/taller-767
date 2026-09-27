def calcularTotalKm(tipoViaje,km,tipoCliente,dia):
    bono1 = calcularBonificacion1(tipoViaje,km) / 100
    bono2 = calcularBonificacion2(tipoCliente) / 100
    bono3 = calcularBonificacion3(dia) / 100
    totalKm = km + km*bono1 + km*bono2 + km*bono3
    return totalKm

def calcularBonificacion3(dia):
    bono = 0
    if dia == "Lunes" or dia == "Martes" or dia == "Miercoles":
        bono = 20
    elif dia == "Jueves" or dia == "Viernes":
        bono = 15
    elif dia == "Sabado" or dia == "Domingo":
        bono = 10
    return bono

def calcularBonificacion2(tipoCliente):
    bono = 0
    if tipoCliente == "Normal":
        bono = 10
    elif tipoCliente == "Preferencial":
        bono = 12
    elif tipoCliente == "VIP":
        bono = 20
    return bono

def calcularBonificacion1(tipoViaje,km):
    bono = 0
    if tipoViaje == "Nacional":
        if km <= 10000:
            bono = 10.61
        elif km > 10000 and km <= 16000:
            bono = 20.52
        elif km > 16000 and km <= 18000:
            bono = 30.43
        elif km > 18000:
            bono = 40.11
    elif tipoViaje == "Internacional":
        if km <= 25000:
            bono = 45.34
        elif km > 25000 and km <= 30000:
            bono = 55.25
        elif km > 30000 and km <= 45000:
            bono = 65.16
        elif km > 45000:
            bono = 75.13
    return bono

def ejercicio4():
    #Datos de prueba (entrada)
    tipoViaje = "Internacional"
    km = 27000
    tipoCliente = "VIP"
    dia = "Martes"
    
    #Pregunta A
    bono1 = calcularBonificacion1(tipoViaje,km)
    print("La primera bonificación es",bono1)
    
    #Pregunta B
    bono2 = calcularBonificacion2(tipoCliente)
    print("La segunda bonificiación es",bono2)
    
    #Pregunta C
    bono3 = calcularBonificacion3(dia)
    print("La tercera bonificación es",bono3)
    
    #Pregunta D
    totalKm = calcularTotalKm(tipoViaje,km,tipoCliente,dia)
    print("El total de kilometros es",totalKm)
    
ejercicio4()