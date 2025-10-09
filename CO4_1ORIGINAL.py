class rectangle:
    __area = 0
    __perimeter = 0
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
        
    def calcarea(self):
        self.__area = self.__length*self.__width
        print("Area is  :",self.__area)
        return self.__area

    def calcperimeter(self):
        self.__perimeter = 2*(self.__length+self.__width)
        print("Perimeter is :",self.__perimeter)


length1 = int(input("Enter length of the FIRST rectangle : "))
width1= int(input("Enter width of the FIRST rectangle : "))
obj = rectangle(length1,width1)
    
obj.calcarea()
obj.calcperimeter()
    
length2 = int(input("Enter length of the SECOND rectangle : "))
width2 = int(input("Enter width of the SECOND rectangle : "))
obj2 = rectangle(length2,width2)
obj2.calcarea()
obj2.calcperimeter()

if obj.calcarea() >= obj2.calcarea():
           if obj.calcarea() == obj2.calcarea():
                print("Rectangles area are  equal")
           else:
                print("Rectangle one is large")
else:
            print("Rectangle Two is large")
    
