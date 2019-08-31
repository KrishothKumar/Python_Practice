# mod1.py
print("hi")
var1 = "None123"

def func1A():
    global var1
    var1 = 'A'
    import mod2
    mod2.func2()

def func1B():
    global var1
    print(var1)


if __name__ == '__main__':
    import sys
    _mod = sys.modules['mod1'] = sys.modules[__name__]
    func1A()

# _modname = os.path.splitext(os.path.basename(os.path.realpath(__file__)))[0]
# _mod = sys.modules[_modname] = sys.modules[__name__]
