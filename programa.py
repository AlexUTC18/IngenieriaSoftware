def Menu():
    """Funcion que Muestra el Menu"""
    print """************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir"""
def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese un Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print "Resultado de la Suma es:", x+y
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print "Resultado de la Resta es:",x-y
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print "Resultado de La Multiplicacion es:",x*y
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print "Resultado de La Division es:", x/y
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print "No se Permite la Division Entre 0"
              opc = int(input("Selecione Opcion\n"))
               print "Gracias por usar este programa"
               print "Gracias por usar este programa"
               print "Este es un nuevo cambio, viernes 26 de marzo 2021 a las 11:12"
            
Calculadora()
