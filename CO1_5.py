n = int(input("How many numbers? "))

result = []

for i in range(n):
    num = int(input("Enter number: "))
    
    if num > 100:
        result.append("over")
    else:
        result.append(num)

print("Modified list:", result)
