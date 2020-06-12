import pprint
import time

# def fizz_buzz(x):
#     result = ""
#     if x % 3 == 0:
#         result = "Fizz"
#     if x % 5 == 0:
#         result = f"({result}Buzz)"
#     return x if not result else result
#     # if result:
#     #     return result
#     #
#     # else:
#     #     return x
#
# t1 = time.time()
# a = fizz_buzz(25)
# print(a)
# t2 = time.time()
# print(t2 - t1)

# def show_numbers(limit):
#     i = 0
#     while i <= limit:
#         print(f"{i} EVEN")
#         i += 1
#         print(f"{i} ODD")
#         i += 1
#     return limit

# def stars(rows):
#     for i in range(1, rows):
#         print(i * "*")
#     return rows
# a = stars(7)

#print()

# def check(limit):
#     for Number in range(1, limit):
#         count = 0
#         for i in range(2, Number//2 + 1):
#             if Number % i == 0:
#                 count += 1
#                 break
#         if count == 0 and Number != 1:
#             print(Number)
#
# aasd = check(100)
# print(aasd)


# a = show_numbers(5)
# def func3(*numbers):
#     print(max(numbers))
#     print(numbers)
#     return max(numbers)
#
#
# func3(3, 5, 7, 9)

# def biglist():
#     listone = [3,6,9,12,15,18,21]
#     listtwo = [4,8,12,16,20,24,28]
#     listthree =[]
#     for i in listone + listtwo:
#         if i % 2 == 1:
#             listthree.append(i)
#         print(i)
#     return listthree
#
# fsd = biglist()
# print(fsd)
#
# def test_list(k):
#     list1 = [54, 44, 27, 79, 91, 41]
#     print(list1)
#     item = list1.pop(k)
#     print(f"list after removing index 4 {list1}")
#     list1.insert(2, item)
#     print(f"list after adding element at index 2 {list1}")
#     list1.append(item)
#     print(f"list after adding element at the end {list1}")
#     print(len(list1))
#
# test_list(4)
#
def dict1():
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {"John": 47, "Emma": 69, "Kelly": 76, "Jason": 97}
    roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
    print(roll_number)
    return roll_number

# print(dict1())
# roll_number = [47, 46, 459, 48, 48, 12]
# digit = str(roll_number[2])
# print(digit)
# print(type(digit))
#
#
#
# def fds():
#     speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
#     list = list(set(speed.values()))
#     print(list)
#     return list1
#
# asdsa = fds()
# print(asdsa)
#
# x = list(list_set)
# def type():
#     list3 = [10, 20, 33, 46, 55, 56, 98, 105, 111]
#     for items in list3:
#         if items % 5 == 0:
#             print(items)
#
# asdddd = type()
# print(asdddd)


def basicloop(limit):
    i = 1
    while i < limit:
        print(f"{i}"*i)
        i -= 1

def basicloop2(limit):
    for i in range(0, limit):
        print(f"{i}"*i)

basicloop2(10)
basicloop(10)

print("sdfasdf", "sgpkasf", sep="**")
integer = 1461
digit = str(integer)[1]
digit2 = str(integer)[-1]
if digit == digit2:
    print("true")
else:
    print("false")

def lellist():
    return [item for item in [10, 20, 23, 11, 17] if item % 2 == 1] \
           + [item for item in [13, 43, 24, 36, 12] if item % 2 == 0]



a = lellist()
print(a)


def print_values(*values):
    for value in values:
        print(value)
    return print_values


print_values(3, 5, 8)

sozluk = {
    "pc1": {
        "name": "dell",
        "ram": "32"
    },
    "pc2": {
        "name": "hp",
        "ram": "64"
    },
    "pc3": {
        "name": "cisco",
        "ram": "128"
    }
}
for x in sozluk:
    # asd = x["pc1"]
    print(x)
print(sozluk["pc1"].values(), sozluk["pc2"])

# list1 = ["asd", "dsa", "sad", "fsda", "sdfa", {"asdfsa": "fdfsfss"}]
# print(list1)
# for x in list1:
#     print(x["asdfsa"])
#
# pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(dict)



# dicts = [
#     {"name": "Tom", "age": 10},
#     {"name": "Mark", "age": 5},
#     {"name": "Pam", "age": 7},
#     {"name": "Dick", "age": 12}
# ]
#
#
# for x in gmp_results:
#     print(x["parsed_data"])
#     print(x["sent_parsed_data"])
