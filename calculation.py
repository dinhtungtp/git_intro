import math

def cal_circle_area(r):
    return math.pi * pow(r, 2)

def cal_rectangle_area(a, b):
    return a * b

if __name__ == '__main__':
    f = int(input("choose function: \n\
        1. cal_circle_area \n\
        2. cal_rectangle_area \nPlease enter an integer:"))

    if f == 1:
        r = int(input("Input value r: "))
        result = cal_circle_area(r)
    elif f == 2:
        a = int(input("Input value a: "))
        b = int(input("Input value b: "))
        result = cal_rectangle_area(a, b)
    
    else:
        result = "Wrong input"
    print(f"Result: {result}")
