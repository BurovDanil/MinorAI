import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ufc-fighters-statistics.csv')
df.sample(5)

# import matplotlib.pyplot as plt

# def add(x, y):
#     return x + y

# def substract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         raise ValueError('Cannot divide by zero!')
#     return x / y

# def logarithm(x):
#     return plt.log(x)

# def percentage(x, y):
#     return (x/y)*100

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# print("5. Logarithm")
# print("6. Percentage")

# while True:
#     choice = input("Enter choice(1/2/3/4/5/6): ")
    
#     if choice in ('1' , '2' , '3' , '4', '5', '6'):
#         try:
#             num1 = float(input ("Enter first number: "))
#             num2 = float(input ("Enter second number: "))
#         except ValueError:
#             print("Invalid input")
#             continue
#         if choice  == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#         elif choice == '2':
#             print(num1, "-", num2, "=", substract(num1, num2))
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#         elif choice == '4':
#             try:
#                 print(num1, "/", num2, "=", divide(num1, num2))
#             except ValueError as e:
#                 print(e)
#         elif choice == '5':
#             print("logarithm of ", num1, "=", logarithm(num1))
#         elif choice == '6':
#             print(num1, "is" , percentage(num1, num2), "percent of", num2)
            
#         nextInput = input("Do you want to continue? (yes/no): ")
#         if nextInput == 'no':
#                 break
#     else:
#         print("Invalid Input")
# import random

# cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

# values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# card_value_map = dict(zip(cards, values))

# # print(card_value_map)

# random.shuffle(cards)

# card1 = cards.pop()

# while True:

#     print("Your card is: ", card1)

#     choice = input("Higher or lower? (h/l): ")

#     if choice == 'h' and card_value_map[card1] < card_value_map[cards[-1]]:
#         print("You win!")
#         card1 = cards.pop()
#     elif choice == 'l' and card_value_map[card1] > card_value_map[cards[-1]]:
#         print("You win!")
#         card1 = cards.pop()
#     else:
#         print("You lose!")
#     secondChoice = input("Do you want to continue? (yes/no): ")
#     if secondChoice == 'no' or  secondChoice == 'n':
#         break
#     elif secondChoice == 'yes' or secondChoice == 'y':
#         continue
#     else:
#         print("Invalid Input")
#         break

