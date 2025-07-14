x, op, z = input("Expression: ").split()

x = float(x)
z = float(z)

match op:
    case '+': answer = x + z
    case '-': answer = x - z
    case '*': answer = x * z
    case '/': answer = x / z

print(f"Answer: {answer:.2f}")