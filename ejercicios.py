#coding=utf-8
import os
import random

try:
    horaIngresada = 0
    horas = input("ingrese su hora respectiva:\n.")
    if "." in horas:
        horaIngresada = float(horas)
    else:
        horaIngresada = int(horas)

    

    minutos = horaIngresada*60
    print("su hora seleccionada son",minutos,"minutos!")
except ValueError as Ve:
    print(Ve)
else:
    print("su codigo va bien")
finally:
    print("fin de codigo")
