a = 3 
valorMinimo = 0
valorMaximo = 5

rango = (a >= valorMinimo and a <= valorMaximo)

if(rango):
    print("Esta dentro del rango")
else:
    print("No esta dentro del rango")
    
vacaciones = True
disposicion = True
diaDescanso = False

if((vacaciones and disposicion) | diaDescanso):
    print("Vayase de paseo")
else:
    print("Quedese en casa")
    
if not(vacaciones or diaDescanso):
    print("No salgas")
else:
    print("Ok puedes salir")