'''
Author: 零到正无穷
Date: 2021-01-31 10:43:22
LastEditTime: 2021-01-31 12:22:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\5_3.py
'''
#todo if语句的使用
age = 19
if age >= 18:
    print("You are oold enough to vote!")
    print("Have you registered to vote yet?\n")

#todo if-else语句的使用
age = 19
if age >= 20:
    print("You are oold enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")

#todo if-elif-else
#!根据年龄段收费的游乐场第一版
age = 12

if age < 4:
    print("Your admission cost is $0.\n")
elif age < 18:
    print("Your admission cost is $25.\n")
else:
    print("Your admission cost is $40.\n")

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")