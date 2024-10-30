def my_decorator(func):
    def inner(v):
        result = func(v)
        if isinstance(result, int):
            result += 10
        return result
    return inner


@my_decorator
def my_function(value):
    print(type(value))
    return value


print(my_function(1))
print(my_function(1.))
