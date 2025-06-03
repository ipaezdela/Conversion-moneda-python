# PASO 1 Definir el valor actual del euro y dolar con respecto al peso mexicano

tipo_cambio_eur_a_mex = 23.70 # En un caso realista, habria que consumir informacion actualizada de una BDD o API
tipo_cambio_usd_a_mex = 20.75 # En un caso realista, habria que consumir informacion actualizada de una BDD o API


# PASO 2 Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)

tipo_conversion = input("Ingrese la moneda origen para la conversion (EUD/USD): ") # puede ser ingresado en Mayus o Minus, porque el upper en paso 4 convierte a mayuscular


# PASO 3 SOlicitar al usuario el monto a convertir

monto_a_convertir = float(input("ingrese el monto a convertir: ")) #castea el dato ingresado del input de STR a FLOAT

# PASO 4 Realizar la conversion utilizando el tipo de cambio correspondiente
# PASO 5 Mostrar el resultado de la conversion al usuario

if tipo_conversion.upper() == "EUR": #convierte a mayusculas por si hay discrepancia en el dato ingresado por el usuario
    resultado = monto_a_convertir * tipo_cambio_eur_a_mex
    print("El resultado de la conversion de EUR a MXN es: ", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mex
    print("El resultado de la conversion de USD a MXN es: ", resultado)
else: 
    print("Actualmente este tipo de conversion no esta disponible")




