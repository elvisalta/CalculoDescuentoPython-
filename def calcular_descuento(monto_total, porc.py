def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el descuento aplicando un porcentaje al monto total."""
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 100  
monto2 = 200  
porcentaje_personalizado = 15  

# Cálculo de descuentos
descuento1 = calcular_descuento(monto1)  
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)  

# Cálculo del monto final
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f"Compra 1 - Monto total: ${monto1}, Descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")
print(f"Compra 2 - Monto total: ${monto2}, Descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")
