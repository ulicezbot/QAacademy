nombre= input ("ingrese su nombre")
apellido= input ("ingrese su apellido")
edad= input ("ingrese su nombre ")
edad= int(edad)
if edad <18:
    condicionedad= ("es menor")
elif edad <65:
    condicionedad= (" mayor")
elif edad< 120:
   condicionedad=("es jubilado")
else:
   condicionedad=(" esta muerto")
print("Su nombre es: "+nombre+" y su apeliido es: "+apellido+" y por su edad usted es un: "+condicionedad)
