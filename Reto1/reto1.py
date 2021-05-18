def calcularTotalBoletas(cantidad_adultos, cantidad_menores):
    valor_total_adultos = cantidad_adultos * 12000
    valor_total_menores = cantidad_menores * 10000
    cantidad_total_boletas = cantidad_adultos + cantidad_menores
    if cantidad_total_boletas == 2:
        valor_total_adultos *= 0.9 
        valor_total_menores *= 0.9
    elif cantidad_total_boletas == 3:
        valor_total_adultos *= 0.85 
        valor_total_menores *= 0.85
    elif cantidad_total_boletas == 4:
        valor_total_adultos *= 0.8 
        valor_total_menores *= 0.8
    valor_total = valor_total_adultos + valor_total_menores
    return ("El valor a pagar por adultos es: "
            + str(valor_total_adultos) +" y por menores es: "
            + str(valor_total_menores) +" para un total a pagar de: "
            + str(valor_total))

print(calcularTotalBoletas(1,2))