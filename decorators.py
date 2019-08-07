import functools

def my_deco(func):  # In this func = my_func() func() is class my_func()
    @functools.wraps(func)
    def fuction_that_runs_func():
        print("Before the func")
        func()
        print("After the func")
    return fuction_that_runs_func

@my_deco     # My_func is parament for the my_deco()
def my_func():
    print("I'm in th fuction")

# my_func()

def decorators_paraments(number): # This get value for number is 11
    def my_deco(func):  # In this func = my_func_param() func() is class my_func_param()
        @functools.wraps(func)
        def fuction_that_runs_func(*args): # This gets parament for my_func_param
            print("Before the func")
            func(*args)
            print(number)
            print("After the func")
        return fuction_that_runs_func
    return my_deco

@decorators_paraments(11)
def my_func_param(x, y):
    print("Hello ",end="")
    print(x+y)

my_func_param(50, 60)
