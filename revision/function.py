def fun():
    print("Hey this is a  example function")

def evenodd(x):
    if (x%2 == 00):
        return "Even"
    else:
        return "Odd"

def myfun(x , y =50):
    print("x: ", x)
    print("y :", y )

def student(fname , lname ):
    print(fname , lname)

def nameage(name , age ):
    print("Hi I am ", name)
    print("My age is ", age)

def f1():
    s = "I love myself"
    def f2():
        print(s)


#Anonymous function
def cube(x):
    return x*x*x
cube_l = lambda x : x*x*x


#return value type function
def square_value(num):
    return num**2

#pass by reference
def myfun(x):
    x[0] = 20

lst = [10,11,12,13]
myfun(lst)


def myfun2(x):
    x = 20

a = 10
myfun2(a)



#Recusive function

def factorial(n):
    if n == 0:
        return 1
    else:return n * factorial(n-1)

print(factorial(4))

