#Q1. Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Input from user

print("Enter details of Rectangle 1:")
l1 = float(input("Length: "))
b1 = float(input("Breadth: "))

print("\nEnter details of Rectangle 2:")
l2 = float(input("Length: "))
b2 = float(input("Breadth: "))

obj1 = Rectangle(l1, b1)
obj2 = Rectangle(l2, b2)

area1=obj1.area()
area2=obj2.area()
perimeter1=obj1.perimeter()
perimeter2=obj2.perimeter()

# Compare by area
if area1 > area2:
    print("\nRectangle 1 has larger area.")
elif area1 < area2:
    print("\nRectangle 2 has larger area.")
else:
    print("\nBoth rectangles have equal area.")
    

print("\nArea of Rectangle 1:", area1)
print("Perimeter of Rectangle 1:", perimeter1)

print("\nArea of Rectangle 2:", area2)
print("Perimeter of Rectangle 2:", perimeter2)
