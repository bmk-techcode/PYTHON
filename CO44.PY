# Q4. Create a class Time with private attributes hour, minute, and second. Overload + operator to find sum of two time values.



class Time:
    def __init__(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def __add__(self, other):
        total_s = self.__s + other.__s
        total_m = self.__m + other.__m + total_s // 60
        total_h = self.__h + other.__h + total_m // 60
        total_s %= 60
        total_m %= 60
        return Time(total_h, total_m, total_s)

    def display(self):
        print(f"{self.__h:02}:{self.__m:02}:{self.__s:02}")


# Example usage
t1 = Time(2, 45, 50)
t2 = Time(1, 30, 25)
t3 = t1 + t2

print("First time: ", end="")
t1.display()
print("Second time:", end=" ")
t2.display()
print("Sum of times:", end=" ")
t3.display()
