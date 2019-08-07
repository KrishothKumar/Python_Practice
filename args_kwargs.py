

def my_args(*args):
    print(sum(args))
def my_args_kwargs(**kwargs):
    print(kwargs)

def methos(another):
    return another()

my_list=[1, 3, 8, 9, 7]

print(list(filter(lambda x: x != 3, my_list)))
# print (methos(lambda: 35 + 77))
#
# def f(x):
#     return x * 3
#
# f(5)

(lambda x: x * 3)(5) # This fuction equals to f(x)

# my_args(3, 2, 8, 9)
#
# my_args_kwargs(name = "Krishoth", location = "Chennai" )
