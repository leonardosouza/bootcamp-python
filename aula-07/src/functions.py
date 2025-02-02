def soma(n1: float = 0, n2: float = 0) -> float:
    """
    soma dois numeros
    """
    return n1 + n2


a = 1.5
b = 2
print(f"{a} + {b} = {soma(n1=a, n2=b)}")

c = 4
d = 8
print(f"{c} + {d} = {soma(c, d)}")


print(f"{soma()}")
