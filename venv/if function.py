a=int(input("Insert 1st argument: "))
b=int(input("Insert 2nd argument: "))

def my_func(a,b):
    if b > a:
        print("Oh NO! 2nd is bigger one (((")
    elif a == b:
        print("Mm we have reached an equality that we didn't plan ... ")
    else:
        print("YEAHHHHH! We did that!")
my_func(a,b)
