# cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus', 'Termez', 'Namangan', 'Andijan']
# three_cities = cities[3:6]
# print(three_cities)
# print(three_cities)
# reversed_cities = cities[::-1]

# print('Fergana' in cities)
# print('Chirchik' in cities)
# print(2 in cities)

# print(cities)
# for city in cities:
#     print(city)


# text = 'my name is Aziz'
# for letter in text:
#     print(letter)

# cities = ('Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus', 'Termez', 'Namangan', 'Andijan')
# for city in cities:
#     print(city)

# print(range(10)
# (0,1,2,3,4,5,6,7,8,9)

# for num in range(10, 20, 2):
#     print(num)

# for num in range(20,10, -2):
#     print(num)

# пршли
# 1. lists-[]
# 2. tuples - ()
# 3. strings - '' , ""
# 4. range()- интегрируемый объект

# 5. ЦИКЛ for нужен для того чтобы прогонять через цикл ИНТЕРИРУЕМЫЕ СУЩНОСТИ

# for i in range(11):
#      print(i * i)

# for i in range(11):
#       print(i * i, i * i * i)

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(i * i, i * i * i)

# for i in range(1000):
#        print(i * i, i * i * i)

# for i in range(0, 1000, 5):
#         print(i * i, i * i * i)

# acc = 0
# for num in range(1, 11):
#     acc = num  + acc
#     print(acc)



# acc = 0
# for num in range(1, 11):
#      acc = num  + acc
# print(acc)

# acc = 1
# for num in range(1, 11):
#       acc = num  * acc
# print(acc)

# acc = 0
# for num in range(0, 21, 2):
#     acc = num  + acc
# print(acc)

cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus', 'Termez', 'Namangan', 'Andijan']

# for i in range(len(cities)):
#     print(cities[i])

acc = ''
cities_len = len(cities)
for i in range(len(cities)):
    acc += cities[i] + ','
    if i != cities_len -1:
        acc += cities[i] + ','
    else: acc += cities[i]
print(acc)