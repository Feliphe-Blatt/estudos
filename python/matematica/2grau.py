from math import sqrt
print("Equação de 2° grau: ax² + bx + c = 0\n")
a = float(input("Digite um valor para a:"))
b = float(input("Digite um valor para b:"))
c = float(input("Digite um valor para c:"))

Delta = b**2 - (4*a*c)
x1 = (-b + pow(Delta,1/2))/(2*a)
x2 = (-b - pow(Delta,1/2))/(2*a)

print("x1 = %g" %x1)
print(x2)
