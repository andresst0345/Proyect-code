num1 = float (input("Ingrese el primer número = "))
num2 = float (input("Ingrese el segundo número = "))

print("Opciones de operaciones:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = int(input("Seleccione una operación (1, 2, 3, 4): "))

if operacion == 1:
  resultado = num1 + num2
  print("El resultado de la suma es:", resultado)
elif operacion == 2:
  resultado = num1 - num2
  print("El resultado de la resta es:", resultado)
elif operacion == 3:
  resultado = num1 * num2
  print("El resultado de la multiplicación es:", resultado)
elif operacion == 4:
  resultado = num1 / num2
  print("El resultado de la división es:", resultado)
else:
  print("Opción inválida. Por favor seleccione una opción válida (1, 2, 3, 4).")

