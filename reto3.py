edad_float = input("Dime tu edad")
edad = float(edad_float)

if edad >= 0 and edad < 14:
    print("Niño")
elif edad >=14 and edad <=28:
    print("Adolescente")
elif edad >=28 and edad <=60:
    print("Adulto")
elif edad > 60:
    print("Adulto mayor")
else:
    print("edad invalidad")