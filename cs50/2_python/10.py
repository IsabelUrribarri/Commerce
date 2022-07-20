import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Entrada invalida")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: No puedes dividir por 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")