flight_number = input("Введите номер рейса:")
airline_name_ru = input("Введите название авиакомпании на русском языке:")
airline_name_en = input("Введите название авиакомпании на английском языке:")
destination_city_ru = input("Введите город прилёта на русском языке:")
destination_city_en = input("Введите город прилёта на английском языке:")

print("Объявление в аэропорту:")
print(f"Заканчивается посадка на рейс {flight_number} виакомпании {airline_name_ru} до {destination_city_ru}.")
print(f"This is the final boarding call for {airline_name_en} flight {flight_number} to {destination_city_en}.")