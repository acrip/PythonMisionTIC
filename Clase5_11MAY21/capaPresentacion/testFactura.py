from Clase5_11MAY21.libFactura.calcularIva import valorIva
from Clase5_11MAY21.libFactura import calcularIva as iva

valorTotal = iva.valorTotal(10000,20000,30000)

valorConIva = iva.valorIva(valorTotal)

print("El valor total a pagar es: "+valorTotal+" con un iva de "+valorConIva)