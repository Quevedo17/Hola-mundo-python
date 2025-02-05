#programa para identificar si una persona puede
#dependiendo de su edad y nacionalidad


#tabla de verdad
#P  Q  P and Q  P or Q  
#V  V    V       V
#V  F    F       V
#F  V    F       V
#F  F    F       F

print("programa para identificar si una persona puede votar")
edad = int(input("ingrese su edad:\n"))
nacionalidad = input("ingrese su nacionalidad:\n")
if edad >= 18 and nacionalidad.lower() == "Colombiano":
    print("usted puede votar")

elif edad >= 21 and nacionalidad.lower() == "Extranjero":
    print("sos gringo pero mayor de edad asi que si podes votar")
else:
    print("deportadito")

