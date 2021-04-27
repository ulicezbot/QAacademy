#programa de prueba
#print("hola mundo")

#edad= 24
edad= input("ingrese su edad: ")
#print (edad)
edad=int(edad)
#if edad >= 18:
#    print ("usted es mayor de edad")
#    if edad ==65:
#        print ("debe chequearse de corona")
#else:
#    print ("usted es menor de edad")
if edad <0:
    print ("usted no nacio")
elif edad <18:
    print ("usted es menor de edad")
elif edad <65:
    print ("usted es mayor de edad")
elif edad< 120:
    print ("usted es jubilado")
else:
    print ("de donde saliste flaco")
a= "hola"
b= " mundo"

print (a+b)
