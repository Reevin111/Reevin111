#Generator=A generator in Python is a special type of function that returns an iterator object.
# It appears similar to a normal Python function in that its definition .
def add():
    yield"Reena"
    yield"Anande"
    yield"Software Developer"

obj=add()
print(next(obj))
print(next(obj))
print(next(obj))