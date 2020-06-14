import random
import secrets
import string
import time
import threading


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

# country_codes = {"Ankara": "AN", "İstanbul": "İST", "İzmır": "İZ", "Eskişehir": "ESK", "Konya": "KON"}
# print(country_codes.keys(), country_codes.values())
#
# ###/// List slicing: [start:stop:step]
# pizzas = ["Hawai", "Pepperoni", "Fromaggi", "Napolitana", "Diavoli"]
# pizzas2 = pizzas[1:5:1]
# print(pizzas2)

# print("/"*10, "/"*10, "//"*20,  sep="_"*10)
# print("/"*9, "/"*10, "//"*20, sep="_"*9)
# print("/"*8, "/"*10, "//"*20, sep="_"*8)
# print("/"*7, "/"*10, ""*7, "/"*11, sep="_"*7)
# print("/"*6, "/"*10, ""*7, "/"*11, sep="_"*6)
# print("/"*5, "/"*10, ""*7, "/"*11, sep="_"*5)
# print("/"*4, "/"*10, ""*7, "/"*11, sep="_"*4)
# print("/"*3, "/"*10, ""*7, "/"*11, sep="_"*3)
# print("/"*2, "/"*10, ""*7, "/"*11, sep="_"*2)
# print("/"*1, "/"*10, ""*7, "/"*11, sep="_"*1)
# print(".", "/"*9, ""*7, "/"*11, sep="")

# for x in range(3):
#     print(random.randrange(100, 999, 5))

# silt = []
# for x in range(100):
#     silt.append(random.randrange(1000000000, 9999999999))
# winner = random.sample(silt, 2)
# print(winner)

###/// secrets module

# #Getting systemRandom class instance out of secrets module
# secretsGenerator = secrets.SystemRandom()
#
# #random integer number uisng secrets
# randomNumber = secretsGenerator.randint(0,50)
# print("Secure random number is ", randomNumber)
#
# #random integer number within given range using secrets
# randomNumber = secretsGenerator.randrange(4, 40, 4)
# print("Secure random number within range is ", randomNumber)
#
# #Secure Random choice using secrets
# number_list = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
# secure_choice = secretsGenerator.choice(number_list)
# print ("Secure random choice using secrets is ", secure_choice)
#
# #Secure Random sample uisng secrets
# secure_sample = secretsGenerator.sample(number_list, 3)
# print ("Secure random sample using secrets is ", secure_sample)
#
# #Secure Random uniform using secrets
# secure_float = secretsGenerator.uniform(2.5, 25.5)
# print("Secure random float number using secrets is ", secure_float)


###/// Random exercises
# x = "String"
# y = random.choice(x)
# print(y)
#
# name = 'pynative'
# char = random.choice(name)
# print(char)


# def random_string(string_lenght):
#     letters = string.ascii_letters
#     return "".join(random.choice(letters) for i in range(string_lenght))
#
# print(random_string(12))


# ### Random password generator (including atleast 2 uppercase, 1 digit, 1 punctuation)
# def random_password():
#     random_source = string.ascii_letters + string.digits + string.punctuation
#     password = random.sample(random_source, 6)
#     password += random.sample(string.ascii_uppercase, 2)
#     password += random.choice(string.digits)
#     password += random.choice(string.punctuation)
#
#     password_list = list(password)
#     random.SystemRandom().shuffle(password_list)
#     password = "".join(password_list)
#     return print("Generaed Password is:", password)


# a = random_password()
# print(a)


# ### Multiplication of two random floats
# first_random_float_num = random.random()
# print(first_random_float_num)
# second_random_float_num = random.uniform(9.5, 99.5)
# print(second_random_float_num)
# print(first_random_float_num * second_random_float_num)


# dice =[1, 2, 3, 4, 5, 6]
# for x in range(5):
#     random.seed(25)
#     print(random.choice(dice))

# def getRandomDate(startDate, endDate ):
#     print("Printing random date between", startDate, " and ", endDate)
#     randomGenerator = random.random()
#     dateFormat = '%d/%m/%Y'
#
#     startTime = time.mktime(time.strptime(startDate, dateFormat))
#     endTime = time.mktime(time.strptime(endDate, dateFormat))
#
#     randomTime = startTime + randomGenerator * (endTime - startTime)
#     randomDate = time.strftime(dateFormat, time.localtime(randomTime))
#     return randomDate
#
# print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))
#

#////Time exercises
# print((time.ctime()))
#
# print("//Module Loading Please Wait //")
# time.sleep(2.5)
# print("Module Loaded")

# while True:
#     local_time_tur = time.localtime()
#     time_tur = time.strftime("%I:%M:%S %p", local_time_tur)
#     print(time_tur, end="", flush=True)
#     print("\r", end="", flush=True)
#     time.sleep(1)

# BU NASIL CALISIYO?? sadece terminalde
# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result, end="", flush=True)
#   print("\r", end="", flush=True)
#   time.sleep(1)


# MultiThreading exercises
# def print_hello_three_times():
#     for i in range(4):
#         time.sleep(0.5)
#         print("Hello")
#
#
# def print_hi_three_times():
#     for i in range(4):
#         time.sleep(0.7)
#         print("Hi")
#
# t1 = threading.Thread(target=print_hello_three_times())
# t2 = threading.Thread(target=print_hi_three_times())
#
# t1.start()
# t2.start()



# result = time.gmtime(1545925769)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)
# print(time.localtime())
#
# t = (2020, 6, 14, 12, 54, 25, 3, 361, 0)
# manual_time = time.asctime(t)
# print(manual_time)
#
# t = (2020, 6, 14, 12, 54, 25, 362, 10, 35)
# manual_time = time.asctime(t)
# print(manual_time)
# local_time = time.mktime(t)
# print(local_time)


# t = (2019, 4, 23, 13, 43, 1, 2, 213, 6)
# locale_time = time.mktime(t)
# print(locale_time)
#
# named_tuple = time.localtime()
# time_string = time.strftime("%d/%m/%y, %H:%M:%S")
# print(time_string)


# timed_string = "21 JUNE, 2020"
# output = time.strptime(timed_string, "%d %B, %Y")
# print(output)