clientes=int(input("ingrese un numero de clientes: "))
for i in range (clientes):

  print(i+1)
  edad= input("ingrese su edad: ")
  edad=int(edad)
  if edad <0:
      print ("usted no nacio")
  elif edad <18:
    print ("usted es menor de edad")
  elif edad <65:
    print ("usted es mayor de edad")
  elif edad< 120:
    print ("usted es jubilado")
  else:
    print ("isted esta muerto")
    break
