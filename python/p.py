#1
# number = int(input('number '))
# if number % 2 == 0:
#     print(number, 'is Even number')
# else:
#     print (number, 'is Odd number')

#2
# number = int(input('number '))
# if number % 7 == 0:
#     print (number, 'number is multiply 7')
# else:
#     print (number, 'number is not multiply 7')

#3
# num1 = int(input('number '))
# num2 = int(input('number '))
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

#4
# num1 = int(input('number '))
# num2 = int(input('number '))
# if num1 > num2:
#     print(num2)
# else:
#     print(num1)

#5
# num1 = int(input('number '))
# num2 = int(input('number '))
# sum = num1 + num2
# if num1 > num2:
#     min = num1 - num2
# else:
#     min = num2 - num1
# dub = num1 * num2
# if num1 > num2:
#     cut = num1 / num2
# else:
#     cut = num2 / num1
# arith = (num1 + num2) / 2
# print(sum)
# print(min)
# print(dub)
# print(cut)
# print(arith)

#Циклы
#1
# num1 = int(input('number '))
# num2 = int(input('number '))
# arith = (num1 + num2) / 2
# a = num1 + 1
# sum = 0
# while a < num2:
#     sum += a
#     a += 1
# print(sum, arith)

#2
number = int(input('number '))
sum = 1
# while sum < number:
#     sum += 1
for i in range(1, number + 1):
    sum *= i
print (sum)
