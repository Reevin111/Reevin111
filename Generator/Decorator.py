"""Decorator= a decorator is a design pattern that allows you to modify
the functionality of a function by wrapping it in another function."""
def add():
    a=10
    b=30
    c=a+b
    print("Addition",c)
fun=add
num=fun
num()