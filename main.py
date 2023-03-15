num1 = int(input("Ingrese el primer número: "))
num2 = int(input('Ingrese el segundo numero:'))
suma = num1 + num2
resta = num1 - num2

if num2 != 0:
    div = num1 / num2

else:
    print("El segundo número no puede ser cero para calcular la división; 'div'")


print("El resultado de la suma es:", suma)
print("El resultado de la suma es:", resta)
print("El resultado de la suma es:", div)