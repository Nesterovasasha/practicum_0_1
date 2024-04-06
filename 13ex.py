import math

blind_zone_radius = float(input("Введите радиус 'слепой зоны': "))
reception_radius = float(input("Введите радиус дальности приема: "))

coverage_area = math.pi * (reception_radius**2 - blind_zone_radius**2)

print(f"Площадь покрываемой территории: {coverage_area}")
