# Program to find square of N numbers using list

N = int(input("How many numbers? "))

numbers = []          # empty list
squares = []          # list to store squares

for i in range(N):
    num = int(input("Enter a number: "))
    numbers.append(num)
    squares.append(num ** 2)

print("Numbers:", numbers)
print("Squares:", squares)
