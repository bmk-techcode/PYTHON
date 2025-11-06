

#NORMAL METHOD
numbers = [12, -7, 5, 64, -14]

positivelist = []      # empty list

for num in numbers:
    if num > 0:
        positivelist.append(num)

print("Positive List:", positivelist)



#LIST COMPREHENSIONS

numbers = [-2, -27, -5, 64, -14]

positive_list = [num for num in numbers if num > 0] 

print("Positive List:", positive_list)
