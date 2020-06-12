###/// Sum of the Numbers for 100 to 200
# for x in range(100, 200):
#     y = x + (x + 1)
#     x =+ 1
#     print(y)

###/// List operations
# l1 = [6, 4, 2]
# l1.append(12)
# l1.append(8)
# l1.append(4)
# l1.pop(1)
# l1.insert(1, 3)
# print(l1)


# lust = [25, 58, 24, 16, 95, 75, 36, 24, 15, 69]
# lust2 = []
# lust3 = []
# print(max(lust))
# print(min(lust))
# for item in lust:
#     if item % 2 == 0:
#         lust2.append(item)
#     else:
#         lust3.append(item)
# print(lust2, lust3)

country_codes = {"Ankara": "AN", "İstanbul": "İST", "İzmır": "İZ", "Eskişehir": "ESK", "Konya": "KON"}
print(country_codes.keys(), country_codes.values())

###/// List slicing: [start:stop:step]
pizzas = ["Hawai", "Pepperoni", "Fromaggi", "Napolitana", "Diavoli"]
pizzas2 = pizzas[1:5:1]
print(pizzas2)