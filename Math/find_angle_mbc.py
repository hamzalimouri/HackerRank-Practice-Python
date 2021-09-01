import math
ab, bc = int(input()), int(input())
degree = round(math.degrees(math.atan2(ab, bc)))
sym = chr(176)
print(f'{degree}{sym}')
