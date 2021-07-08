import math


def triangle_square(a, b):
    return 0.5 * a * b


res = input('a b (separated by space)')
a, b = map(float, res.split())
print('Hypotenuse of right-angled triangle -', math.hypot(a, b))
print('Square of right-angled triangle -', triangle_square(a, b))
