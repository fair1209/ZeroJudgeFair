
import math
a, b, c = map(int, input().split())
d = b * b - 4 * a * c


if d > 0:
    x1 = (-b + math.isqrt(d)) // (2 * a)
    x2 = (-b - math.isqrt(d)) // (2 * a)
    print(f"Two different roots x1={x1} , x2={x2}")

elif d == 0:
    x = -b // (2 * a)
    print(f"Two same roots x={x}")
else:
    print("No real root")