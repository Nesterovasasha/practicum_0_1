distance_in_centimeteres = float(input("Введите расстояние в сантиметрах: "))

distance_in_inches = distance_in_centimeteres / 2.54
distance_in_feet = distance_in_inches / 12
distance_in_yards = distance_in_feet / 3
distance_in_miles = distance_in_yards / 1760

print("Расстояние в ярдах:", distance_in_yards)
print("Расстояние в милях:", distance_in_miles)
print("Расстояние в футах:", distance_in_feet)
print("Расстояние в дюймах:", distance_in_inches)
