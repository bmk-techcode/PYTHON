class rectangle:
    __area = 0                                                            # Private attributes are conventionally denoted with a leading underscore.
    __perimeter = 0                                                      # In Python, attributes prefixed with double underscores (e.g., __length)
   
    
    def __init__(self,L,W):                                         #_init__ method is a special method,a constructor,automatically called when a new object (instance) of a class is created.
        self.__length= L
        self.__width = W
        
    def calcarea(self):
        self.__area = self.__length*self.__width
        print("Area is  :",self.__area)
        
        
    def __lt__(self,second):                                         #__lt__ method, the special method that implements the less-than comparison operation.
        if self.__area < second.__area:
            return True
        else:
            return False
    
length1= int(input("Enter length of the rectangle 1 : "))
width1 = int(input("Enter width of the rectangle  1 : "))
length2 = int(input("Enter length of the rectangle  2  : "))
width2 = int(input("Enter width of the rectangle  2 : "))

obj1 = rectangle(length1,width1)
obj2 = rectangle(length2,width2)
obj1.calcarea()
obj2.calcarea()

if obj1 < obj2:
        print("Rectangle two is large")
else:
        print("Rectangle one is large or these are equal")
