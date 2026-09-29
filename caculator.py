A = int(input("Enter First Number: "))
B = int(input("Enter Second Number: "))

addition = A + B
subtraction = A - B

print("Addition =", addition)
print("Subtraction =", subtraction)

multiplication = A * B
print("Multiplication =", multiplication)

if B != 0:
    division = A / B
    print("Division =", division)
else:
    print("Division is not possible by zero")
