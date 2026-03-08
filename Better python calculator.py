import math
bold = "\033[1m"
green = "\033[92m"
reset = "\033[0m"



a = int(input("first number "))
b = int(input("second number "))
c = input("Operation ")
d = a + b
if c == "*" or c == "Multiply":
    print(a*b)
elif c == "/" or c == "Divide":
    print(a/b)
elif c == "-" or c == "substract":
    print(a-b)
elif c == "floor":
    print(a//b)
elif c == "square root":
    e = math.sqrt(d)
    print(f"{bold}{green}We added up the first and second number than found the square root of that number which is: {e}")
    print(f"{reset}ㅤ")
else:
    print(a+b)
