import math
def find_angle(AB: float, BC: float) -> int:
    MC = math.sqrt(AB**2 + BC**2) / 2
    BM = math.sqrt(MC**2 + BC**2 - 2 * MC * BC * math.cos(math.atan(AB / BC)))
    return round(math.acos((BM**2 + BC**2 - MC**2)/(2 * BM * BC)) * 180/math.pi)

print(str(find_angle(float(input()), float(input()))) + u'\N{DEGREE SIGN}')
