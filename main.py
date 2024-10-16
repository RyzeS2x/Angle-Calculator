import math

a = int(input('Digite o valor do angulo: '))

r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)

print(f'O seno e o cosseno do angulo de {a}°, e de:')
print(f'sin({a}°) = {s:.3f}')
print(f'cos({a}°) = {c:.3f}')
print(f'tan({a}°) = {t:.3f}')
