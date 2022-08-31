mesDigitado=input("Digite el mes que desea evaluar")
mes=mesDigitado.lower()

if(mes=='enero' or mes=='febrero' or mes=='marzo'):
    print(f'{mes} corresponde a Invierno')
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print(f'{mes} corresponde a Primavera')
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print(f'{mes} corresponde a verano')
elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print(f'{mes} corresponde a otoño')
else:
    print(f'{mes} no corresponde a un mes del año')