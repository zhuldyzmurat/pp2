#ex1
import math
degrees = float(input())
radian = degrees * math.pi / 180
print(radian)

#ex2
import math

base1 = float(input())
base2 = float(input())
height = float(input())
area = height * (base1 + base2) * 0.5
print(area)
#ex3
import math

n = int(input())
s = float(input())

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(area)
#ex4
import math
a = int(input())
b = int(input())
area = a * b
print(area)