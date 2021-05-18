def despacho_buses(personas_bus: int, personas_estacion: int)->bool:
    
    if(personas_estacion >= 40) :
        totalPersonas = personas_bus + personas_estacion
        if(totalPersonas > 200):
            personas_bus = 200
            personas_estacion = totalPersonas - personas_bus
        else:
            personas_bus = totalPersonas
            personas_estacion = 0
          
    #if(personas_bus > 150 or personas_estacion >= 50) :
    #    return True
    #    
    #return False
         
    return personas_bus > 150 or personas_estacion >= 50

print(despacho_buses(50,200))
print(despacho_buses(170,10))
print(despacho_buses(50,10))
print(despacho_buses(50,50))





